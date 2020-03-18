# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:49:54 2020

@author: Mathieu Reine
"""

param = [] #On init le tableau param

def Definition_parametre(x,r):
    x = float(x)#Au cas où x et r ne sont pas des float
    r = float(r)
    param.append(x)#param = [x,r]
    param.append(r)
    return(param)#On retourne les paramètres
  
    