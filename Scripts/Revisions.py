# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:46:39 2020

@author: Mathieu Reine
"""

"""Dans cette partie de code nous définissons la fonction de révisions des évaluations"""

#Remarques générales : il faut se placer dans le repertoire de travail,
# il faut faire un tableau csv pour chaque eleve dans un dossier 'eleves' dans le repertoire de travail
# il faut également créer un dossier 'eleves_masses_rev'

#Définition des fonctions de révisions, avec les 2 modèles
        
#Positif

def revision_pos(masse_now,masse_ant): #Masse now : masse de la nouvelle note, masse ant : masse d'avant
    masse_rev=[0,0,0,0]
    masse_rev[0]=((masse_now[2]*masse_now[0])/(masse_ant[0]+masse_ant[1]+masse_ant[2]))+masse_now[0]
    masse_rev[1]=((masse_now[2]*masse_now[1])/(masse_ant[0]+masse_ant[1]+masse_ant[2]))+masse_now[1]
    masse_rev[2]=masse_ant[2]*masse_now[2]
    masse_rev[3]=1-masse_rev[0]-masse_rev[1]-masse_rev[2]
    return(masse_rev)

#Négatif
    
def revision_neg(masse_now,masse_ant):#Masse now : masse de la nouvelle note, masse ant : masse d'avant
    masse_rev=[0,0,0,0]
    masse_rev[0]=(masse_now[0]+masse_ant[0])/2
    masse_rev[1]=(masse_now[1]+masse_ant[1])/2
    masse_rev[2]=(masse_now[2]+masse_ant[2])/2
    masse_rev[3]=1-masse_rev[0]-masse_rev[1]-masse_rev[2]
    return(masse_rev)

#Définition de quel modèle utiliser en fonction des 2 notes

def revision(masse_now,masse_ant):#Masse now : masse de la nouvelle note, masse ant : masse d'avant
    if (masse_now[0]==1 or masse_now[1]==1) and (masse_ant[0]!=1 and masse_ant[1]!=1): #Passage de zone incertaine à zone de certitude
        return(revision_pos(masse_now,masse_ant))#On utilise la révision positive
    elif ((masse_now[0]>=masse_ant[0]) or ((masse_now[0]==0 and masse_ant[0]==0) and (masse_now[2]>=masse_ant[2]))):#On ne passe pas à une zone plus certaine mais l'évaluation est meilleure
        return(revision_pos(masse_now,masse_ant))#On utilise la révision positive
    else :#Sinon : pas de passage à zone certitude et résultat moins bon
        return(revision_neg(masse_now,masse_ant))#On utilise la révision négative
        
#Remarque : Fonction utilisée en fonction de la zone des 2 évaluations comme vu sur le modèle
        
    
#Fonction finale : transformation des datas en dataframe, calcul des révisions et réécriture en csv
def revision_masses_df(df,nom_eleve):
    rep_principal = os.getcwd()
    df.sort_values(by=['date'])    #On trie par date pour que les revisions se fasse bien dans le temps
    evals = [] #Afin de ne réviser que sur les évaluations faites au moins 2 fois, on stocke les évaluations déjà vues
    evals_masses = []#Pour stocker l'historique des évaluations et leurs masses déjà effectuées (savoir les masses de la dernière révision de chacune des évaluations)
    df['compte'] = df['matiere'].apply(lambda x:x.capitalize())# Init de la colonne compte
    df['durée'] = df['date']#on initialise la durée à la date
    try: #En fonction de la fonction choisie
        df['revision'] = df['note'].apply(lambda x:masses_x(x,param)) #On défintit par défaut la première révision par la masse
        df['masses'] = df['note'].apply(lambda x:masses_x(x,param))
    except :
        df['revision'] = df['note'].apply(lambda x:masses_cgt(x,param))#On défintit par défaut la première révision par la masse
        df['masses'] = df['note'].apply(lambda x:masses_cgt(x,param))
    for u in range(len(df)):#Pour toutes les évaluations
        df['compte'] = df['matiere'][0:u].eq(df['matiere'][u]).sum() #fonction compte (ne marche pas)
        if df['matiere'][u] not in evals :#Si on a pas encore vu cette évaluation alors il ne sagit pas d'une révision, 
            evals.append(df['matiere'][u])# on stocke l'information pour que la prochaine itération soit une révision
            evals_masses.append([df['matiere'][u],df['masses'][u],df['date'][u]])#On stocke les infos de cette dernière révision
        else :#Si on a déjà vu cette évaluation alors il s'agit d'une révision
            for k in range(len(evals)):#On cherche la bonne évaluation sur laquelle on va faire une révision
                if evals[k]==df['matiere'][u]:#C'est la même compétence, c'est donc la dernière révision
                    id_ant=k#On mémorise sa place pour remplassez la valeur de la dernière révision
                    anterieur = evals_masses[k][1]#On récupère la dernière révision
                    df['revision'][u]=revision(df['masses'][u],anterieur)#On met à jour la valeur de la révision
                    evals_masses[id_ant][1]=df['revision'][u]#On met la valeur de la revisions en mémoire pour réviser la prochaine itération de l'évaluation par rapport à la dernière révision
                    df['durée'][u] = datetime.strptime(df['date'][u], '%Y-%m-%d %H:%M:%S')-datetime.strptime(evals_masses[id_ant][2], '%Y-%m-%d %H:%M:%S')#On calcule la durée depuis la derniere révision
                    evals_masses[id_ant][2] = df['date'][u]#On stocke la date de la dernière révision
    os.chdir(rep_principal+'\\eleves_masses_rev')#On définie le répertoire de travail comme le dossier eleves_masses_rev
    df.to_csv(nom_eleve+'_masses_rev.csv', sep = ';',index = False) #On créer un tableau csv avec les masses révisées
    os.chdir(rep_principal) # on retourne dans le répertoire de travail
    

