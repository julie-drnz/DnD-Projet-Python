import os
import time
import random

# IMPORTATION DES DONNÉES DU JOUEU
from data import couleurs, descriptions, zones, RESET, LISTE_HEROS, LISTE_MONSTRES

def afficher_titre():
    print("="*50)
    print("           L'ÉCHIQUIER DE L'ORACLE ")
    print("="*50)

def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        afficher_titre()
        print("\nBienvenue, Maître du Jeu.")
        print("1. ⚔️  Jouer (Lancer un combat)")
        print("2. 🏛️  Explorer (Les visions de l'Oracle)")
        print("3. 🚪  Quitter")
        
        choix = input("\nQue souhaitez-vous faire ? (1-3) : ")

        if choix == "1":
            lancer_jeu()
        elif choix == "2":
            explorer_monde()
        elif choix == "3":
            print("\nL'Oracle ferme ses yeux... À bientôt, mortel.")
            break
        else:
            print("\n Choix invalide.")
            time.sleep(1.5)

def lancer_jeu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- ⚔️ PRÉPARATION DU COMBAT ⚔️ ---")
    
    # Étape 1 : Demander le nombre de héros
    nb_h = input("\nCombien de héros l'Oracle voit-il ? : ")
    
    # Étape 2 : Demander le nombre de monstres
    nb_m = input("Combien de créatures s'opposent à eux ? : ")

    print(f"\nDestin scellé : {nb_h} héros contre {nb_m} monstres.")
    
    # Note : La sélection précise des noms se fera quand Joueur 1 
    # aura rempli LISTE_HEROS dans data.py
    print("\n[En attente des noms des personnages pour la sélection...]")
    
    input("\nAppuyez sur Entrée pour revenir au menu...")

def explorer_monde():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- 🏛️ LES VISIONS DE L'ORACLE ---")

    # Sélection aléatoire de 3 zones parmi les 20 de data.py
    zones_affichees = random.sample(zones, 3)

    print("\nL'Oracle vous propose trois destinations :")
    for i, z in enumerate(zones_affichees):
        print(f"{i+1} - {z}")

    choix = input("\nOù souhaitez-vous envoyer vos héros ? (1, 2 ou 3) : ")

    if choix in ["1", "2", "3"]:
        # On récupère la zone choisie
        zone_choisie = zones_affichees[int(choix) - 1]
        
        # On récupère la couleur et la description associées dans data.py
        couleur_zone = couleurs[zone_choisie]
        description_zone = descriptions[zone_choisie]

        os.system('cls' if os.name == 'nt' else 'clear')
        print("===================================")
        print(f"{couleur_zone}📍 {zone_choisie.upper()}{RESET}")
        print("-" * 35)
        print(f"{couleur_zone}{description_zone}{RESET}")
        print("===================================\n")
        
        print("Trois coffres antiques apparaissent devant toi...")
        print("1 - Coffre ancien | 2 - Coffre mystérieux | 3 - Coffre doré")
        
        input("\nAppuyez sur Entrée pour ouvrir le coffre et repartir...")
    else:
        print("\n❌ Choix invalide. L'Oracle perd sa vision.")
        time.sleep(1.5)

if __name__ == "__main__":
    menu_principal()