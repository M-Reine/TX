# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:29:34 2020

@author: Mathieu Reine
"""

"""Partie de code qui sert à la fonction de propagaton des masses en fonction des prérequis d'une compétence"""



rep_principal = os.getcwd()




def retab_list_str(stre):#Pour récupérer les masses de revision ont doit repasser le str de la liste "[1,2]" et le transformer en ['1','2']
    stre=stre.replace('[','').replace(']','').replace(' ','').split(",")#C'est exactement ce que cette instruction fait
    return(stre)#On retourne la liste
    



def prop_masses(masse,distance,alpha):#Définition de la fonction de propagation de masse
    new_masse=[0,0,0,0]#On initialise
    distance = int(distance)#On passe distance en integer
    alpha = float(alpha)#On passe alpha en flottant
    new_masse[0]=(1-alpha)**distance*float(masse[0])#On calcule les nouvelles masses selon le modèle
    new_masse[1]=(1-alpha)**distance*float(masse[1])
    new_masse[2]=1+(1-alpha)**distance*float(masse[2])-(1-alpha)**distance
    new_masse[3]=1-float(new_masse[0])-float(new_masse[1])-float(new_masse[2])
    return(new_masse)#On retourne les nouvelles masses


def Prop_Masses(Eleves,alpha):#Cette fonction effectue la prédiction en fonction de la dernière révision de la compétence qui requiert, et ceux pour tous les eleves d'Eleves
    df_ont = pd.read_csv(rep_principal+'\\eval_ontologie.csv',sep=';')#On récupère les informations de l'ontologie
    for eleve in Eleves:#Pour tous les eleves
        preds = []#On stocke les predictions
        #df_eval = pd.read_csv(rep_principal='\\eleves'+eleve.nom+'.csv',sep = ';') #*a passer en non commentaire si non revisée
        df_eval = pd.read_csv(rep_principal+'\\eleves_masses_rev\\'+eleve.nom+'_masses_rev.csv',sep = ';')#On charge le dataframe des évaluation utilisant la revision
        """try :
            df_masses = df_eval['note'].apply(lambda x:masses_x(x,param))
        except:
            df_masses = df_eval['note'].apply(lambda x:masses_cgt(x,param))"""#*a passer en non commentaire si non revisée 
        df_masses = df_eval['revision'].apply(lambda x: retab_list_str(x))#On recupère les masses revisées
        for i in range(len(df_eval['note'])):#pour toute les evaluation du dataframe de cet eleve
            for k in range(len(df_ont['distance'])):#pour tous les liens de l'ontologie
                if df_ont['one_who_requires'][k]==df_eval['matiere'][i]:#On regarde si cette compétence en requiert une autre
                    preds.append([df_ont['one_who_requires'][k],str(df_masses[i]),df_ont['one_that_is_required'][k],str(prop_masses(df_masses[i],df_ont['distance'][k],alpha)),df_eval['date'][i]])
                    #On stocke la prediction avec les informations utiles, quelle compétence on a évalué, quelle evaluation on a predit, les masses, la date de l'évaluation
        try :#Si prédiction n'est pas vide (cela est possible)
            ar = np.array(preds)#on stocke le résultat dans un tableau csv dans le dossier eleve_masses_preds
            df_preds = pd.DataFrame(ar, columns = ['Evalué','ses masses évaluées', 'Prédit', 'ses masses prédites','date'])
            df_preds.to_csv(rep_principal+'\\eleves_masses_preds\\'+eleve.nom+'_masses_preds_'+str(alpha)+'.csv', sep = ';',index = False)
        except:
            pass#Sinon on passe à l'élève suivant

"""
def prop_masses(masse,distance,alpha):
    new_masse=[0,0,0,0]
    distance = int(distance)
    alpha = float(alpha)
    new_masse[0]=(1-alpha)**distance*masse[0]
    new_masse[1]=(1-alpha)**distance*masse[1]
    new_masse[2]=(1-alpha)**distance*masse[2]
    new_masse[3]=1-new_masse[0]-new_masse[1]-new_masse[2]
    return(new_masse) """ 
