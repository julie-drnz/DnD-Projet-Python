# # Le fichier à lancer (Boucle de jeu principale)

import os
import time
# Importations des autres fichiers (à créer par tes camarades)
# from models import Heros, Monstre
# from actions import combat_tour_par_tour
# from utils import effacer_ecran

def afficher_titre():
    print("="*50)
    print("           L'ÉCHIQUIER DE L'ORACLE ")
    print("="*50)

def menu_principal():
    while True:
        # effacer_ecran() # Utilise la fonction de ton camarade Joueur 1/4 ici
        afficher_titre()
        print("\nBienvenue, Maître du Jeu.")
        print("1.   Jouer")
        print("2.   Explorer")
        print("3.   Quitter")
        
        choix = input("\nQue souhaitez-vous faire ? (1-3) : ")

        if choix == "1":
            lancer_jeu()
        elif choix == "2":
            explorer_monde()
        elif choix == "3":
            print("Fermeture du temple... À bientôt, mortel.")
            break
        else:
            print("❌ Choix invalide.")
            time.sleep(1.5)

def lancer_jeu():
    print("\n--- PRÉPARATION DU COMBAT ---")
    # C'est ici que tu appelleras les fonctions pour :
    # 1. Choisir les héros (Achille, Hercule...)
    # 2. Choisir les monstres (Minotaure, Méduse...)
    # 3. Lancer la boucle de combat
    input("\nAppuyez sur Entrée pour revenir au menu...")

def explorer_monde():
    print("\n--- EXPLORATION DES TERRES GRECQUES ---")
    print("1. Le Mont Olympe")
    print("2. Les Enfers d'Hadès")
    print("3. La Mer Égée")
    # Logique d'exploration à étoffer plus tard
    input("\nAppuyez sur Entrée pour revenir au menu...")

# Lancement du programme
if __name__ == "__main__":
    menu_principal()