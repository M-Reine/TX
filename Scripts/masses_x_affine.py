# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:38:26 2020

@author: Mathieu Reine
"""

"""Définition de la fonction de masse des évaluation de manière affine"""

import numpy as np



def masses_x(note,param): #champs : ma, mna, mi, mc
    
    m = x = float(param[0]) #au cas où param[0] n'est pas un float
    r = float(param[1]) #au cas où param[1] n'est pas un float
    note = float(note) #au cas où note n'est pas un float
    if note<=(x-r): #si note < x-r
        mna=1 #Clairement non acquis
        ma=mi=mc=0
    elif note>=(x+r): #si note > x+r
        ma=1 #Clairement acquis
        mna=mi=mc=0
    elif note<=x:#si entre x-r et x
        mna = m/r - (1/r)*note #m(nona) = x/r - (1/r)*note
        mi = (r-m)/r + (1/r)*note #m(i) = (r-x)/r + (1/r)*note
        ma=mc=0
    else: #si entre x et x+r
        mi = r-m/r - (1/r)*note #m(i) = (r-x)/r -(1/r)*note
        ma = -m/r + (1/r)*note #m(a) = (-x)/r + (1/r)*note
        mna=mc=0
    Masses=[ma,mna,mi,mc]
    return(Masses) #On retourne les masses
    