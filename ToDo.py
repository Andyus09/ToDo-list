import json
import os


liste = [ ]
# Json file read 
fichier = os.path.dirname(__file__)
chemin = os.path.join(fichier, "liste.json")
if os.path.exists(chemin):
    with open(chemin , "r") as f:
        liste = json.load(f)
else:
    liste = [ ]
######################################################
print("\n-------------------- LISTE ------------------------\n")

affichage = """
Choisissez une option:

    \t1: Ajoutez un élement
    \t2: Enlevez un élement
    \t3: Affichez la liste
    \t4: Videz la liste
    \t5: Terminer
"""

# Function remove
def removed(str):
    if choix_1 == "Y":
        retrait = input("retirez votre élement: ").capitalize()
        if retrait in liste :
            liste.remove(retrait)
            print(f"L'élement {retrait} vient d'être retiré. \nLa liste contient maintenant les éléments suivants: {liste}")
    else: print("Okay!")


print(affichage) # Afficher les options


while True:

    choix = input("Votre choix 👉🏾 : ")

    if choix == "1" :
        ajout = input("ajoutez votre élement: ").capitalize()
        if ajout in liste:
            print("L'élement est déjà dans la liste.")
        else:
            liste.append(ajout)
            liste.sort()
            print(f"L'élement {ajout} a bien été ajouté.")
            
    elif choix == "2" :
        retrait = input("retirez votre élement: ").capitalize()
        if retrait in liste :
            liste.remove(retrait)
            print(f"L'élement {retrait} vient d'être retiré. \nLa liste contient maintenant les éléments suivants: {liste}")
        else:
            print(f"L'élement {retrait} n'est pas dans la liste. \nLa liste contient les éléments suivants: {liste}")
            choix_1 = input("Voulez-vous retirer à nouveau un élement comprit dans la liste? (Y/N) \n").capitalize()
            removed(choix_1) # Function remove

    elif choix == "3":
        if liste:
            print("\nVotre liste: \n ")
            for index, element in enumerate(liste,1):
                print(f"{index}. {element} \n ")
        else:
            print("Votre liste ne contient aucun élément")

    elif choix == "4":
        liste.clear()
        print("La liste vient d'être vidé. ")

    elif choix == "5" :
        # Ecrire ds le Json
        with open(chemin , "w") as f:
            json.dump(liste,f)
        ##########################################
        print("À bientôt!")
        exit()

    else:
        print("Veuillez entrer un choix valide!!") 
       
        
    

