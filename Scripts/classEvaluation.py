# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:55:16 2020

@author: Mathieu Reine
"""

"""Dans cette partie de code nous allons définir la classe Evaluation, 
notamment pour permettre l'implémentation des onthologies,
ainsi que les différentes fonctions qu'on appelera à travers l'interface."""



#Cette partie de code permet de créer un jeu de d'évaluations rapidement sans passer par l'interface afin de faire
#Le but principal était essentiellement de pouvoir faire un nombre important de test pour corriger le code

Evaluations = []

#Partie de code permettant de créer rapidement une ontologie
"""
Couleur= Evaluation()
Couleur.change_nom('Couleur')

Math= Evaluation()
Math.change_nom('Math')

Geographie= Evaluation()
Geographie.change_nom('Geographie')
Geographie.add_requirement(Math)
Geographie.add_requirement(Couleur)


Histoire= Evaluation()
Histoire.change_nom('Histoire')
Histoire.add_requirement(Geographie)
Histoire.add_requirement(Math)
"""






class Evaluation(): #Ici on définit la classe Evaluation pour la création des onthologies 
                    #Elle est composée de son nom, de ceux qu'il requière et de ceux dont il est requis
                    #dernier attribut est peu util mais bien pour voir si erreur
                    
    
    
    def __init__(self): #Son initialisation
        self.nom = 'àdef'
        self.isArequirementTo = [[],] #Toutes les évaluations qui requièrent celle-ci et à quelle distance
        self.requires = [[],]#Toutes les évaluations qui ont comme requierement celle-ci et à quelle distance
        Evaluations.append(self)#On garde un historique de toutes les évalutations du système
        
        
    def change_nom(self,new_nom): #La méthode permettant de changer de nom
        self.nom =new_nom
    
    def add_requirement(self,evaluation): # La méthode permettant la création des requirements
        
        self.requires.append([evaluation,1])
        self.requires[0].append(evaluation.nom)
        
        evaluation.isArequirementTo.append([self,1])
        evaluation.isArequirementTo[0].append(self.nom)

#Remarque : pour les attributs requires et isArequirementTo* : on a choisi la structure suivante :
# [[Liste des requis/* de l'évaluation], Liste des tuples [Evaluation requise/*, distance]]
# Exemple : Histoire.requires = [['Math','Géographie'],[charabia1,2],[charabia2,1]] 
# Histoire requiert ici Math et Géographie ; Math à une distance de 2 , Géographie à une distance de 1

"""Autre remarque importante : cette structure peut sembler inutilement compliquée (ce sentiment est renforcé
par la solution proposée pour la propagation des requirements) ; mais au vue des possibles futures focntionnalités
l'outil j'ai décidé de garder cette structure ici si elle s'avère plus efficasse que le tableau construit en partie
propagation""" 

def name(x):#Fonction qui retourne le nom
    return(x.nom)
 
namer = lambda x: name(x) #Fonction applicable à une liste


def reco(Evaluations,nom):#On retrouve une eval par son nom
    for eval in Evaluations:
        if eval.nom == nom:
            return(eval)

def createEvaluation(nom_eval): #Fonction qui permet de créer une évaluation
    if nom_eval in list(map(namer, Evaluations)): #On se sert de notre namer sur tous les éléments de la liste
        erreur_deja_fait() #Si l'évaluation existe déjà, on le fait savoir à l'user 
        return()#sans créer l'évaluation
    evaluation = Evaluation()#Sinon, on créer l'évaluation
    evaluation.change_nom(nom_eval)#On redéfinie son nom de 'adef' au nom que l'on a indiquer (à terme celui rentrer dans l'interface)
    done()
    return(evaluation)#On retourne l'évaluation
    
def createRequirement(nom_eval,nom_eval_required): ##Fonction qui permet de créer un lien requirement entre 2 évaluations
    for x in Evaluations: #On cherche les 2 evaluations concernées
        if x.nom == nom_eval:#Si c'est celui qui requiert
            boss=x
        if x.nom == nom_eval_required:#Si c'est celui qui est requis
            required=x
    if nom_eval_required not in list(map(namer, Evaluations)): #Si l'évaluation requise non créer alors on la créer
        createEvaluation(nom_eval_required)#Sans créer le lien ! (c'est facultatif ou perfectible comme approche)
    if boss.nom in reco(Evaluations,nom_eval_required).isArequirementTo[0] : #Si il fait déjà parti de nos requis
        erreur_deja_fait()#On l'indique à l'utilisateur
        return()#On ne fait rien de plus
    boss.add_requirement(required) #Sinon on ajoute le lien
    done()
    return(nom_eval,nom_eval_required)#On retourne les 2 evaluations
    
 
#Ces fonctions ne fonctionnent pas/que partiellement, plus simple de passer par des bases SQL

def SuppEval(Evaluations,nom_eval):#Fonction suppression d'éval : ne fonctionne pas
    for i in range(len(Evaluations)) :
        if Evaluations[i].nom == nom_eval :
            print('see')
            del(Evaluations[i])
            break
        
    for i in range(len(Evaluations)) :
        for k in range(len(Evaluations[i].requires[0])):
            if Evaluations[i].requires[0][k] == nom_eval :
                del(Evaluations[i].requires[0][k])
                break
                
        for k in range(len(Evaluations[i].requires[1:])):
            print(Evaluations[i].requires[1:][k][0].nom)
            if Evaluations[i].requires[1:][k][0].nom == nom_eval:
                print('hello')
                print(Evaluations[i].requires[1:][k])
                del(Evaluations[i].requires[1:][k]) #Ne marche pas
                break
                
        for k in range(len(Evaluations[i].isArequirementTo[0])):
            if Evaluations[i].isArequirementTo[0][k] == nom_eval :
                del(Evaluations[i].isArequirementTo[0][k])
                break
                
        for k in range(len(Evaluations[i].isArequirementTo[1:])):
            if Evaluations[i].isArequirementTo[1:][k][0].nom == nom_eval:
                del(Evaluations[i].isArequirementTo[1:][k]) #Ne marche pas
                break
                
    return(Evaluations)
    
def Supplien(Evaluations,nom_eval1,nom_eval2): #Fonction qui supprime un lien : ne fonctionne pas
        
    for i in range(len(Evaluations)) :
        for k in range(len(Evaluations[i].requires[0])):
            if Evaluations[i].requires[0][k] in [nom_eval1, nom_eval2] :
                del(Evaluations[i].requires[0][k])
                break
                
        for k in range(len(Evaluations[i].isArequirementTo[1:])):
            if len(Evaluations[i].isArequirementTo[1:]) == 0:
                break
            if Evaluations[i].isArequirementTo[1:][k][0].nom == nom_eval1:
                del(Evaluations[i].isArequirementTo[1:][k]) #Ne marche pas
                break
                
        for k in range(len(Evaluations[i].requires[1:])):
            if len(Evaluations[i].requires[1:]) == 0:
                break
            if Evaluations[i].requires[1:][k][0].nom == nom_eval2:
                del(Evaluations[i].requires[1:][k]) #Ne marche pas
                break
                
    return(Evaluations)
    

