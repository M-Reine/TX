# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:08:45 2020

@author: Mathieu Reine
"""

"""Application de la fonction de masse sur tout un tableau csv, sous la méthode affine avec changement de variable"""


import numpy as np
import pandas as pd
import os

rep_principal = os.getcwd ()


def masses_file(f): #Fonction qui prend un fichier f et qui effectue la transformation de masses sur chacune des évaluations
    os.chdir(rep_principal+'\\eleves')#On va dans le dossier des élèves
    df = pd.read_csv(f,sep=';')#On créer un dataframe grâce au tableau csv
    df.astype({'note': 'float'}) #Si non float alors il devient un float
    
    df['masses'] = df['note'].apply(lambda x:masses_cgt(x,param)) #On applique à la colonne des notes la fonction de transformation de masses choisie
    df = df.sort_values(by=['date'])#On classe les évaluations dans l'ordre de date
    df = df.reset_index(drop=True)#On reset les index
    os.chdir(rep_principal+'\\eleves_masses')#On se place dans le dossier des masses des élèves
    df.to_csv(f[:-4]+'_masses.csv', sep = ';',index = False)#On créer un tableau csv avec les masses
    os.chdir(rep_principal)#On retourne dans le repertoire de travail


