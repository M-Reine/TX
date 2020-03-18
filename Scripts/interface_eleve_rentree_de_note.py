# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:31:29 2020

@author: Mathieu Reine
"""

"""Partie interface qui s'occupera de l'ajout d'évaluation pour un élèves donnné"""


"""window = Tk() création fenêtre

Label(window, text='blabla') création texte blabla dans window
Entry(window, text='blabla') création du champs blabla dans window
Button(window, text='blabla' command = funct()) création texte blabla dans window, si on clique dessus on utilise funct()

"%s" %entry_1.get() permet de récupérer le contenu du champs entry_1

Truc.pack() permet de mettre à la suite dans la fenetre (.grid() et d'autre existent, permettent de se placer différement)
window.mainloop() permet l'ouverture de la fenêtre"""

from tkinter import*



def erreur_deja_fait(): #Cette fonction permet de montrer à l'utilisateur
    label_deja_fait=Label(window,text="Deja Fait !")# Les erreurs de type : "tu as déjà fait la même action"
    label_deja_fait.pack()
    
    
def done(): #Cette fonction permet de montrer à l'utilisateur
    label_fait=Label(window,text="Effectué")# Les erreurs de type : "tu as déjà fait la même action"
    label_fait.pack()
    
    
def Creer_Requierement(window_ont): #Fonction utilisée quand on appuie sur le bouton pour créer un requirement
    lab_Requirement_1=Label(window_ont,text = "Celui qui requiert") #Pour indiquer à l'utilisateur que le premier champs est pour celui qui requiert
    lab_Requirement_1.pack() 
    entry_Requirement_1=Entry(window_ont,text = "Rentrer l'évaluation") #Le champs pour celui qui requiert
    entry_Requirement_1.pack()
    lab_Requirement_2=Label(window_ont,text = "Celui qui est requis")#Pour indiquer à l'utilisateur que le deuxieme champs est pour celui qui est requis
    lab_Requirement_2.pack()
    entry_Requirement_2=Entry(window_ont,text = "Rentrer le requis") #Le champs pour celui qui est requis
    entry_Requirement_2.pack()
    button_create_requirement = Button(window_ont,text="Creer le requirement",command=lambda: createRequirement("%s" %entry_Requirement_1.get(),"%s" % entry_Requirement_2.get()))
    button_create_requirement.pack() #Bouton pour confirmer la création du lien
    
def creationMode():#Ouvfre une fenêtre qui permet de créer des évaluations pour l'élève actif
    
    window_crea = Tk()
    window_crea.title('Créer Evaluation pour ' + "%s" %entry_Eleve.get())
    txt1 = Label(window_crea, text ='Compétence évaluée :')
    txt2 = Label(window_crea, text ='Note Evaluation :')
    txt3 = Label(window_crea, text ='Date Evaluation (format dd/mm/yyyy) :')
    entr1 = Entry(window_crea,text='')
    entr2 = Entry(window_crea,text='')
    entr3 = Entry(window_crea,text='')
    
    txt1.grid(row =1, sticky =E)
    txt2.grid(row =2, sticky =E)
    txt3.grid(row =3, sticky =E)
    
    entr1.grid(row =1, column =2)
    entr2.grid(row =2, column =2)
    entr3.grid(row =3, column =2)

    
    button_create_eval_note = Button(window_crea,text="Créer l'évaluation",command= lambda : createEvaluation_note("%s"%entr1.get(),"%s"%entr2.get(),datetime.strptime("%s"%entr3.get(), '%d/%m/%Y')))
    button_create_eval_note.grid(row=4,column=3)
    
    window_crea.mainloop()
   
    
    
def suppMode_Eval(Evaluations):#Ouvre une fenêtre qui permet de supprimer des compétences pour la constructuction d'ontologie, ne marche pas entièrement
    
    window_supp = Tk()
    
    #Personnalisation de la fenêtre :
    window_supp.title('Supprimer une compétence')
    window_supp.geometry('540x360')
    window_supp.minsize(240,180)
    window_supp.config(background = '#41B77F')
    
    #Ajouter un texte :
    label_title = Label(window_supp, text = "La compétence à Supprimer")
    label_title.pack()
    
    entry_supp = Entry(window_supp)
    entry_supp.pack()
    
    button_supp_eval = Button(window_supp,text='Supprimer',command = lambda  : SuppEval(Evaluations,'%s'%entry_supp.get()))
    button_supp_eval.pack()
    
    
def suppMode_Link(Evaluations):#Ouvre une fenêtre qui permet de supprimer des liens pour la constructuction d'ontologie, ne marche pas entièrement
    
    window_supp = Tk()
    
    #Personnalisation de la fenêtre :
    window_supp.title('Supprimer un lien')
    window_supp.geometry('540x360')
    window_supp.minsize(240,180)
    window_supp.config(background = '#41B77F')
    
    #Ajouter un texte :
    label_title1 = Label(window_supp, text = "La compétence qui requiert")
    label_title1.pack()
    
    entry_supp1 = Entry(window_supp)
    entry_supp1.pack()
    
    label_title2 = Label(window_supp, text = "La compétence qui est requise")
    label_title2.pack()
    
    entry_supp2 = Entry(window_supp)
    entry_supp2.pack()
    
    button_supp_link = Button(window_supp,text='Supprimer',command = lambda  : Supplien(Evaluations,'%s'%entry_supp1.get(),'%s'%entry_supp2.get()))
    button_supp_link.pack()
    
def Show_ont(Evaluations):#Ouvre une fenêtre qui permet de voir les compétences et les liens pour la constructuction d'ontologie
    evalus_names = []
    evalus_links = []
    for evalu in Evaluations:
        evalus_names.append(evalu.nom)
        try:
            for evalu_sub in evalu.requires[0]:
                evalus_links.append(evalu.nom+' requiert '+evalu_sub)
        except :
            pass
    
    window_show = Tk()
    
    #Personnalisation de la fenêtre :
    window_show.title('Evaluations_ontologie')
    window_show.geometry('540x360')
    window_show.minsize(240,180)
    window_show.config(background = '#41B77F')
    
    #Ajouter un texte :
    label_title = Label(window_show, text = "etat actuel de l'ontologie")
    label_title.pack()
    
    label_names = Label(window_show,text="Les compétences")
    label_names.pack()
    for i in range(len(evalus_names)):
        label_name = Label(window_show,text = evalus_names[i])
        label_name.pack()
        
    label_space = Label(window_show,text=' ')
    label_space.pack()
        
    label_links = Label(window_show,text = "Les liens :")
    label_links.pack()
    for i in range(len(evalus_links)):
        label_link = Label(window_show,text = evalus_links[i])
        label_link.pack()
        
    button_delete_eval = Button(window_show, text = 'Supprimer une compétence', command = lambda : suppMode_Eval(Evaluations))    
    button_delete_eval.pack(side=LEFT)
    
    button_delete_eval = Button(window_show, text = 'Supprimer un lien', command = lambda : suppMode_Link(Evaluations))    
    button_delete_eval.pack(side=RIGHT)
    
    #Afficher
    window_show.mainloop()
    
    
def Show_eleve(Eleves):#Ouvre une fenêtre qui permet de voir les élèves et leurs evaluations créés durant cette session
    eleves_names = []
    evaluations = []
    for eleve in Eleves:
        eleves_names.append(eleve.nom)
        evaluations.append(' ')
        evaluations.append(eleve.nom)
        try:
            for eleve_evaluation in eleve.Evaluations_note_date:
                evaluations.append(str(eleve_evaluation.type_ev)+' '+str(eleve_evaluation.note)+' '+str(eleve_evaluation.date))
        except :
            pass
    
    window_show_eleve = Tk()
    
    #Personnalisation de la fenêtre :
    window_show_eleve.title('Eleves et leurs evaluations')
    window_show_eleve.geometry('540x360')
    window_show_eleve.minsize(240,180)
    window_show_eleve.config(background = '#41B77F')
    
    #Ajouter un texte :
    label_title = Label(window_show_eleve, text = "Etats actuel du systeme")
    label_title.pack()
    
    label_names = Label(window_show_eleve,text="Les Eleves")
    label_names.pack()
    for i in range(len(eleves_names)):
        label_name = Label(window_show_eleve,text = eleves_names[i])
        label_name.pack()
        
    label_space = Label(window_show_eleve,text=' ')
    label_space.pack()
        
    label_links = Label(window_show_eleve,text = "Les évaluations des eleves :")
    label_links.pack()
    for i in range(len(evaluations)):
        label_link = Label(window_show_eleve,text = evaluations[i])
        label_link.pack()
        
    #Ajouter fonction supp
    
    #Afficher
    window_show_eleve.mainloop()
    
def ontologieMode():#Ouvre une fenêtre qui permet d'effectuer les différentes actions rattachées à la création d'une ontologie
    
    window_ont = Tk()
    
    #Personnalisation de la fenêtre :
    window_ont.title('Evaluations_ontologie')
    window_ont.geometry('540x360')
    window_ont.minsize(240,180)
    window_ont.config(background = '#41B77F')
    
    #Ajouter un texte :
    label_title = Label(window_ont, text = 'Champs pour créer une compétence')
    label_title.pack()
    
    #Ajouter un input pour l'user : Présentation des entry + le champs pour la création d'une évaluation dans le système
    entry_Evaluation = Entry(window_ont, text = "Rentrer une evaluation")
    entry_Evaluation.pack()
    
    #Ajouter un bouton pour l'utilisateur : Presentation des bouton + le bouton pour créer une evaluation dans le système
    button_create_eval = Button(window_ont,text="Creer la compétence",command=lambda: createEvaluation("%s" %entry_Evaluation.get()))
    button_create_eval.pack()
    
    #Ce bouton permettra de passer en mode création de requirement : il affiche les champs et boutons nécessaires
    button_test = Button(window_ont, text="Je veux créer des requirements !", command=lambda : Creer_Requierement(window_ont))
    button_test.pack()
    
    #Ce bouton permettra de finaliser la créatin des ontologie en se servant de la propagation
    button_finish = Button(window_ont, text = 'Finish ontologie !', command= lambda : Finish_Onthologie(Evaluations))
    button_finish.pack(side=RIGHT)
    
    #Ce bouton sert à show le contenu d'Evaluations:
    button_show = Button(window_ont,text = 'Show !', command= lambda : Show_ont(Evaluations))
    button_show.pack(side=LEFT)
    
    #Afficher
    window_ont.mainloop()
    
    
    """Voici la fenetre principale qui contient des boutons qui soit vont s'appuyer 
    sur les fonctions backends que l'on a défini dans d'autre script,
    soit il créeront d'autre fenêtre qui elle même suivront le même schéma"""
    
window = Tk()

Eleves = []
Evaluations = []
rep_principal = os.getcwd ()
#Personnalisation de la fenêtre :
window.title('Evaluations_élève_création')
window.geometry('1080x720')
window.minsize(600,400)
window.config(background = '#41B77F')
              
label_title = Label(window, text = 'Champs pour créer un élève')
label_title.pack()

entry_Eleve = Entry(window, text = "Créer/Sélectionner une eleve")
entry_Eleve.pack()

button_create_eleve = Button(window,text="Créer/Sélectionner l'élève",command=lambda: createEleve("%s" %entry_Eleve.get()))
button_create_eleve.pack()


param = []

label_param1 = Label(window, text = 'Paramètre x')
label_param1.pack()

entry_param1 = Entry(window, text = "Paramètre x")
entry_param1.pack()


label_param2 = Label(window, text = 'Paramètre r')
label_param2.pack()

entry_param2 = Entry(window, text = "Paramètre r")
entry_param2.pack()

button_def_param = Button(window,text="Définir les paramètres",command=lambda: Definition_parametre("%s" %entry_param1.get(),"%s" %entry_param2.get()))
button_def_param.pack()



button_eval_now = Button(window, text = 'Prêt à rentrer des évaluations ',command= lambda: creationMode())
button_eval_now.pack()

button_finish = Button(window, text = 'Finish entrée évaluation !', command= lambda : Finish_Create_Eval(Eleves))
button_finish.pack(side=RIGHT)

label_alpha = Label(window, text = 'Champs pour créer les prédictions parametre alpha')
label_alpha.pack()

entry_alpha = Entry(window, text = "Créer alpha")
entry_alpha.pack()

button_create_preds = Button(window,text="Créer les prédictions au parametre alpha",command=lambda: Prop_Masses(Eleves,"%s" %entry_alpha.get()))
button_create_preds.pack()

button_ont_now = Button(window, text = 'Prêt à faire une ontologie ',command= lambda: ontologieMode())
button_ont_now.pack(side = LEFT)

button_show_eleve = Button(window, text = 'Show eleves ',command= lambda: Show_eleve(Eleves))
button_show_eleve.pack(side = LEFT)


window.mainloop()