# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:33:45 2020

@author: Mathieu Reine
"""



from datetime import date
from datetime import datetime
import pandas as pd
import numpy as np
import os

def name(x):
    return(x.nom)
 
namer = lambda x: name(x) #Fonction applicable à une liste

Eleves = []#On initialise l'état du système (pas d'élève sur la session)


eleve_actif = ['None']

class Eleve(): #Ici on définit la classe Evaluation pour la création des onthologies 
                    #Elle est composée de son nom, de ceux qu'il requière et de ceux dont il est requis
                    #dernier attribut est peu util mais bien pour voir si erreur
                    
    def __init__(self): #Son initialisation
        self.nom = 'àdef'#Nom de l'eleve
        self.Evaluations_note_date=[]#l'ensemble des évaluations de l'eleve, l'évaluation sera définie dans la classe Evaluation_note_date
        Eleves.append(self)#On garde un historique de toutes les évalutations du système
        
        
    def change_nom(self,new_nom): #La méthode permettant de changer de nom
        self.nom =new_nom
    


class Evaluation_note_date():#Ici on définit la classe qui est déjà utilisée à l'intérieur de l'attribut 
                            #Evaluations_note_date de la classe Eleve ; cette dernière regroupe l'ensemble des évaluation d'un élève
                            #Elle est composé de son id unique, de l'élève associé, de la compétence associée, de la note obtenue et de la date de l'évaluation                                    
    def __init__(self): #Son initialisation
        self.eleve = eleve_actif[0]
        self.eleve.Evaluations_note_date.append(self)
        self.id = len(eleve_actif[0].Evaluations_note_date)
        self.type_ev = 'none'
        self.note = 0
        self.date = date.today().strftime('%d/%m/%Y')
        
    
    def change_type(self,new_type_ev): #La méthode permettant de changer de nom
        self.type_ev =new_type_ev
        
    def change_id(self,new_id): #La méthode permettant de changer de nom
        self.id =new_id
    
    def change_note(self,new_note):
        self.note = new_note
        
    def change_date(self,new_date):
        self.date= new_date
        

def createEleve(nom_eleve): #Fonction qui permet de créer un élève qui aura pour nom ; nom_eleve
    if nom_eleve in list(map(namer, Eleves)): #Elle permet également de rendre l'élève actif (un seul peut l'etre à la fois) si cet eleve est déjà créer
        for eleve in Eleves:    #Cette fonctionalité est surtout utile dans le cadre de l'utilisation de l'interface
            if eleve.nom == nom_eleve:
                eleve_actif[0]=eleve
                try :
                    txt1 = Label(window, text ='Elève créé')
                except:
                    eleve_actif[0]=eleve
                return(eleve)
    eleve = Eleve()
    eleve.change_nom(nom_eleve)
    eleve_actif[0]=eleve
    done()
    return(eleve)
        
    
    
def createEvaluation_note(type_ev_init,note,date):#Céer une évaluation pour l'élève actif, elle définit la compétence associé, sa note et la date
    evalution_note = Evaluation_note_date()
    evalution_note.change_type(type_ev_init)
    evalution_note.change_note(note)
    evalution_note.change_date(date)
    try :
        done()
    except:
        evalution_note.change_note(note)
    return(evalution_note)
    

rep_principal = os.getcwd ()

def Finish_Create_Eval(Eleves):#Programme final qui s'appuie sur toutes les fonctions backend afin de créer tous les tableaux csv mentionnés dans les précedents scripts
    for eleve in Eleves :
        booly = True#Permet de voir si l'élève avait déjà du contenue dans le système (afin d'update et non d'écraser)
        f = rep_principal+'\\eleves\\'+eleve.nom+'.csv'
        try:
            df = pd.read_csv(f,sep=';')#Si on arrive à charger le dataframe alors l'elève a deja du contenu
        except:
            booly = False#L'élève n'a pas de contenue
        if len(eleve.Evaluations_note_date) != 0:#Si l'élève a du contenu sur cette session
            ar = []
            for eval in eleve.Evaluations_note_date:
                ar.append([str(eval.type_ev), str(eval.date), str(eval.note)])
            df1 =  pd.DataFrame(ar, columns = ['matiere', 'date', 'note'])#On créer un dataframe des infos de cette session
            if booly == False:#Si premier contenu pour cet eleve
                df1 = df1.reset_index(drop = True)
                df1.to_csv(f, sep = ';',index = False)
                df1 = df1.sort_values(by=['date'])
                df = df1.reset_index(drop=True)
                print(f)
                revision_masses_df(df1,eleve.nom)#On fait tourner le backend et on renvoie tout de suite les infos de la session
            else : #Sinon
                df_max = pd.concat([df,df1])#On concatene le dataframe de l'existant et des infos de la session
                df_max.reset_index(drop = True)
                df_max.to_csv(f, sep = ';',index = False)
                df_max = df_max.sort_values(by=['date'])
                df_max = df_max.reset_index(drop=True)
                print(f)
                revision_masses_df(df_max,eleve.nom)#On fait tourner le backend et on renvoie tout de suite les infos existante plus session
            os.chdir(rep_principal)
            masses_file(eleve.nom+'.csv')#Dans tous les cas on update le tableau csv des masses
            os.chdir(rep_principal)
            done()
            print(eleve.nom)
            
            

       
        

            
            

