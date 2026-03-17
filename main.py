import os
import time
import random

# IMPORTATION DES DONNEES
from data import couleurs, descriptions, zones, RESET, LISTE_HEROS, LISTE_MONSTRES

def afficher_titre():
    print("="*50)
    print("           L'ECHIQUIER DE L'ORACLE ")
    print("="*50)

def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        afficher_titre()
        print("\nBienvenue, Maitre du Jeu.")
        print("1. Jouer (Lancer un combat)")
        print("2. Explorer (Les visions de l'Oracle)")
        print("3. Quitter")
        
        choix = input("\nQue souhaitez-vous faire ? (1-3) : ")

        if choix == "1":
            lancer_jeu()
        elif choix == "2":
            explorer_monde()
        elif choix == "3":
            print("\nL'Oracle ferme ses yeux... A bientot, mortel.")
            break
        else:
            print("\nChoix invalide.")
            time.sleep(1.5)

def lancer_jeu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- PREPARATION DU COMBAT ---")
    
    nb_h = input("\nCombien de heros l'Oracle voit-il ? : ")
    nb_m = input("Combien de creatures s'opposent a eux ? : ")

    print(f"\nDestin scelle : {nb_h} heros contre {nb_m} monstres.")
    print("\n[En attente des noms des personnages dans data.py...]")
    
    input("\nAppuyez sur Entree pour revenir au menu...")

def explorer_monde():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- LES VISIONS DE L'ORACLE ---")

    # Tirage aléatoire de 3 zones
    zones_affichees = random.sample(zones, 3)

    print("\nL'Oracle vous propose trois destinations :")
    for i, z in enumerate(zones_affichees):
        print(f"{i+1} - {z}")

    choix = input("\nVotre choix (1, 2 ou 3) : ")

    if choix in ["1", "2", "3"]:
        zone_choisie = zones_affichees[int(choix) - 1]
        couleur = couleurs[zone_choisie]
        texte = descriptions[zone_choisie]

        os.system('cls' if os.name == 'nt' else 'clear')
        print("===================================")
        print(f"{couleur}ZONE : {zone_choisie.upper()}{RESET}")
        print("-" * 35)
        print(f"{couleur}{texte}{RESET}")
        print("===================================\n")
        
        print("Trois coffres antiques apparaissent...")
        print("1 - Coffre ancien | 2 - Coffre mysterieux | 3 - Coffre dore")
        input("\nAppuyez sur Entree pour revenir au menu...")
    else:
        print("\nChoix invalide.")
        time.sleep(1.5)

if __name__ == "__main__":
    menu_principal()