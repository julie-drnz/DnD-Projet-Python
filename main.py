import os
import time
import random
import data
import actions

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

def choisir_personnage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- PREPARATION DU COMBAT ---")
    print("\nL'Oracle vous présente les héros :")
    liste_heros = list(data.personnages.values())
    for i, h in enumerate(liste_heros):
        print(f"{i + 1}. {h.nom} ({h.pv_max} PV)")
    choix_heros = input("\nQuel héros choisissez-vous ? (entrez le numéro) : ")
    while not (choix_heros.isdigit() and 1 <= int(choix_heros) <= len(liste_heros)):
        choix_heros = input("Choix invalide. Entrez le numéro de votre héros : ")
    heros = liste_heros[int(choix_heros) - 1]
    return heros

def lancer_jeu():
    heros = choisir_personnage()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- PREPARATION DU COMBAT ---")
        print("\nL'Oracle invoque un monstre en adversaire...")
        key_monstre = random.choice(list(data.creatures.keys()))
        monstre = data.creatures[key_monstre]
        print(f"\n{monstre.nom} apparait avec ses {monstre.pv_max} PV !")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n--- LE COMBAT COMMENCE : {heros.nom} VS {monstre.nom} ! ---")
        heros.sorts_restants = heros.sorts_max
        monstre.sorts_restants = monstre.sorts_max
        while heros.pv > 0 and monstre.pv > 0:
            print("\n" + "="*40)
            actions.afficher_stat(heros)
            actions.afficher_stat(monstre)
            print("="*40)
            print("\nC'est votre tour. Actions disponibles :")
            print("1. Attaque physique")
            if heros.sorts_restants > 0:
                print(f"2. Sort : {heros.nom_sort} ({heros.sorts_restants} restant(s))")
            else:
                print(f"2. Sort : {heros.nom_sort} (Épuisé)")
                
            action = input("Votre action (1-2) : ")
            print("")
            if action == "1":
                actions.attaque_physique(heros, monstre)
            elif action == "2":
                if heros.sorts_restants > 0:
                    actions.sort(heros, monstre)
                    heros.sorts_restants -= 1
                else:
                    print(f"Vous n'avez plus d'énergie pour lancer {heros.nom_sort} ! Vous perdez votre tour...")
            else:
                print(f"{heros.nom} hésite et manque son attaque !")
            if monstre.pv <= 0:
                print(f"\nVICTOIRE ! {monstre.nom} a été terrassé par {heros.nom}.")
                break 
            print("\nTour de l'ennemi...")
            time.sleep(1.5)
            if random.choice([True, False]) and monstre.sorts_restants > 0:
                actions.sort(monstre, heros)
                monstre.sorts_restants -= 1
            else:
                actions.attaque_physique(monstre, heros)   
            if heros.pv <= 0:
                print(f"\nDÉFAITE... {heros.nom} a succombé face à {monstre.nom}.")
                break  
            time.sleep(1.5)
            
        est_mort = heros.pv <= 0
        
        heros.pv = heros.pv_max
        monstre.pv = monstre.pv_max
        heros.sorts_restants = heros.sorts_max
        monstre.sorts_restants = monstre.sorts_max
        if est_mort:
            print("\nVotre aventure s'arrête ici.")
            input("Appuyez sur Entrée pour revenir au menu principal...")
            break
        print("\nLe combat est terminé.")
        print("1. Combattre un nouvel adversaire avec ce héros")
        print("2. Partir explorer avec ce héros")
        print("3. Revenir au menu principal")
        
        while True:
            choix_fin = input("Que voulez-vous faire ? (1-3) : ")
            if choix_fin in ["1", "2", "3"]:
                break 
        if choix_fin == "1":
            continue
        elif choix_fin == "2":
            explorer_monde()
            break
        else:
            break


def explorer_monde():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- LES VISIONS DE L'ORACLE ---")
    zones_affichees = random.sample(data.zones, 3)
    print("\nL'Oracle vous propose trois destinations :")
    for i, z in enumerate(zones_affichees):
        print(f"{i+1} - {z}")
    choix = input("\nVotre choix (1, 2 ou 3) : ")
    if choix in ["1", "2", "3"]:
        zone_choisie = zones_affichees[int(choix) - 1]
        couleur = data.couleurs[zone_choisie]
        texte = data.descriptions[zone_choisie]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===================================")
        print(f"{couleur}ZONE : {zone_choisie.upper()}{data.RESET}")
        print("-" * 35)
        print(f"{couleur}{texte}{data.RESET}")
        print("===================================\n")
        
        print("Trois coffres antiques apparaissent...")
        print("1 - Coffre ancien | 2 - Coffre mysterieux | 3 - Coffre dore")
        input("\nAppuyez sur Entree pour revenir au menu...")
    else:
        print("\nChoix invalide.")
        time.sleep(1.5)
if __name__ == "__main__":
    menu_principal()