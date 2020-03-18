# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:55:14 2020

@author: Mathieu Reine
"""

"""Définition de la fonction de masse des évaluation de manière affine
 en opérant un changement de variable (globalement rend des résultats plus souvent entiers)"""


import numpy as np


def masses_cgt(note,param):#champs : ma, mna, mi, mc
    for truc in param:
        truc = float(truc) #au cas ou l'entrée ne soit pas du type float, (si passé par l'interface)
    note = float(note)# même chose
    if note<=(param[0]-param[1]):#si moins de x-r
        mna=1
        ma=mi=mc=0#Clairement non acquise
    elif note>=(param[0]+param[1]): #Si plus que x+r
        ma=1
        mna=mi=mc=0 #Clairement acquis
    elif note<=param[0]: #si entre x-r et x
        mna = (1/2) - (note-(param[0]-(param[1]/2)))/param[1] #m(nona) = 0.5 - (note -(x-r/2))/r
        mi = (1/2) + (note-(param[0]-(param[1]/2)))/param[1] #m(i) = 0.5 + (note -(x-r/2))/r
        ma=mc=0
    else: #si entre x et x+r
        mi = (1/2) - (note-(param[0]+(param[1]/2)))/param[1]#m(i) = 0.5 -(note -(x+r/2))/r
        ma = (1/2) + (note-(param[0]+(param[1]/2)))/param[1]#m(a) = 0.5 +(note -(x+r/2))/r
        mna=mc=0
    Masses=[ma,mna,mi,mc]
    return(Masses)#On retourne les masses
    

    
    
