# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:07:25 2020

@author: Mathieu Reine
"""

"""Autres idées pour la propagation"""

import pandas as pd #Nécessaires à la création d'un dataframe, utilisé plus loin
import numpy as np

def applicable(Evaluations):    #Cette fonction retourne la liste des évaluations qui requiert d'autre compétence
    applicable=[]               #Les autres n'ont pas besoin de passer dans la plupart des boucles de la suite
    for ev in Evaluations:
        if ev.requires != [[]]: #Si la liste des compétences requises n'est pas vide
            applicable.append(ev) #Evaluation dans applicable
    return(applicable) #On retourne la liste applicable

def Lier(Evaluations,a): #Cette fonction retourne un tableau des liaisons du système des évaluations
    Liaisons = []       # sous la forme : [Celui qui requiert, Celui qui est requis, Distance]
    for evalu in Evaluations:
        if evalu in a :# Si on a besoin de l'analyser (il requiert une ou des evaluations)
            for req in evalu.requires[1:]: # On récupère les evaluations requises
                Liaisons.append ([evalu,req[0],req[1]]) #On construit le tableau comme définit plus haut
    return(Liaisons) #On retourne le tableau
                

def Extend_Lier(Liaisons,a): #Cette fonction retourne le tableau des liaisons en connectant à une distance de +1
    for Liai in Liaisons :
        stock_new_Liai = [] #On s'apprête à stocker de nouvelles liaisons
        one_who_requires = Liai[0] #Pour plus de lisibilité
        one_that_is_required = Liai[1]
        if one_that_is_required in a: #Si celui que l'on dont on a besoin a également besoin de quelqu'un alors
            for Liai2 in Liaisons : #Pour chaque liaison
                if one_that_is_required == Liai2[0]: #Si c'est l'une de ses liaisons
                    stock_new_Liai.append([one_who_requires,Liai2[1],Liai[2]+1]) #On ajoute la nouvelle liaison 
        if len(stock_new_Liai)>0:               #[Celui qui requiert, Celui que requiere celui qui est requis, distance+1]
            Liaisons.extend(stock_new_Liai) #On ajoute à Liaisons
    return(Liaisons)#On retourne le nouveau tableau
             
def Minimize_Dist(Liaisons):    #Cette fonction fait en sorte de ne garder que la distance minimale de chacune des liaisons
    ar = np.array(Liaisons)
    df = pd.DataFrame(ar, columns = ['one_who_requires', 'one_that_is_required', 'distance']) #Transformations en data frame
    df1 = df.drop_duplicates(subset=['one_who_requires','one_that_is_required'], keep='first')#On élimine les doublons
    try : 
        df1['one_who_requires'] = df1['one_who_requires'].apply(lambda x : x.nom)#On prend le nom de l'évaluation
        df1['one_that_is_required'] = df1['one_that_is_required'].apply(lambda x : x.nom)
    except:
        pass
    
    df1.to_csv('eval_ontologie.csv', sep = ';',index = False)#On stocke l'ontologie dans un tableau csv
    Liaisons=df1.values.tolist()#On retransforme en tableau
    return(Liaisons)#On le retourne
    
#Remarque : keep = first assure le minimum car on ajoute à la suite les distances supérieur dans Extend_Lier


def Finish_Onthologie(Evaluations):#Fonction finale de la création des onthologies
    a = applicable(Evaluations)#On créer la liste des applicables
    Liaisons = Lier(Evaluations,a)#On créer le tableau des liaisons
    for i in range(len(Evaluations)):#On fait un nombre de tours raisonnable
        Liaisons = Extend_Lier(Liaisons,a)#On descend d'un cran dans les liaisons
        Liaisons = Minimize_Dist(Liaisons)#On garde le chemin optimal pour chacune des liaisons
    return(Liaisons)#On retourne le tableau final
    
#Remarque : on fait len(Evaluations) tours car la plus grande distance possible est len(Evaluations)-1 
#Dans le cas d'un graphe en ligne

#Finish_Onth = Finish_Onthologie(Evaluations)#On récupère le tableau final
