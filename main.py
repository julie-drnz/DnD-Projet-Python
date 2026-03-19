import os
import time
import random
import copy
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
    print("\nChoisissez vos héros :")
    liste_heros = list(data.personnages.values())
    for i, h in enumerate(liste_heros):
        print(f"{i + 1}. {h.nom} ({h.pv_max} PV)")
    
    def get_choix(prompt, exclude=None):
        while True:
            c = input(prompt)
            if c.isdigit() and 1 <= int(c) <= len(liste_heros):
                choix = int(c)
                if exclude is not None and choix == exclude:
                    print("Ce héros est déjà dans votre équipe, choisissez-en un autre !")
                    continue
                return choix
    choix1 = get_choix("\nQuel est votre premier héros ? (entrez le numéro) : ")
    choix2 = get_choix("Quel est votre deuxième héros ? (entrez le numéro) : ", exclude=choix1)
    return [copy.deepcopy(liste_heros[choix1 - 1]), copy.deepcopy(liste_heros[choix2 - 1])]

def lancer_jeu():
    heros_list = choisir_personnage()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- PREPARATION DU COMBAT ---")
        print("\nL'Oracle invoque des monstres en adversaire...")
        
        if random.choice([True, False]):
            monstres_list = [copy.deepcopy(data.creatures["Polypheme"])]
            print(f"\n{monstres_list[0].nom} apparait avec ses {monstres_list[0].pv_max} PV !")
        else:
            monstres_list = [copy.deepcopy(data.creatures["minotaure"]), copy.deepcopy(data.creatures["meduse"])]
            print(f"\n{monstres_list[0].nom} et {monstres_list[1].nom} apparaissent ensemble !")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n--- LE COMBAT COMMENCE ! ---")
        for h in heros_list:
            h.sorts_restants = h.sorts_max
        for m in monstres_list:
            m.sorts_restants = m.sorts_max
        while any(h.pv > 0 for h in heros_list) and any(m.pv > 0 for m in monstres_list):
            print("\n" + "="*40)
            for h in heros_list:
                if h.pv > 0: actions.afficher_stat(h)
            print("-" * 20)
            for m in monstres_list:
                if m.pv > 0: actions.afficher_stat(m)
            print("="*40)
            for heros in heros_list:
                if heros.pv <= 0 or not any(m.pv > 0 for m in monstres_list):
                    continue
                print(f"\nC'est le tour de {heros.nom}. Actions disponibles :")
                print("1. Attaque physique")
                if heros.sorts_restants > 0:
                    print(f"2. Sort : {heros.nom_sort} ({heros.sorts_restants} restant(s))")
                else:
                    print(f"2. Sort : {heros.nom_sort} (Épuisé)")
                action = input("Votre action (1-2) : ")
                cibles_vivantes = [m for m in monstres_list if m.pv > 0]
                cible_choisie = None
                if action in ["1", "2"]:
                    if action == "2" and heros.nom.lower() == "asclépios":
                        cibles_potentielles = [h for h in heros_list if h.pv > 0]
                        prompt_cible = "Qui soignez-vous ? "
                        entete_cibles = "Alliés :"
                    elif action == "2" and heros.nom.lower() == "achille":
                        cibles_potentielles = [h for h in heros_list if h.pv > 0]
                        cible_choisie = cibles_potentielles
                    else:
                        cibles_potentielles = [m for m in monstres_list if m.pv > 0]
                        prompt_cible = "Qui visez-vous ? "
                        entete_cibles = "Cibles :"
                    if action == "2" and heros.nom.lower() == "achille":
                        pass
                    elif len(cibles_potentielles) > 1:
                        print(entete_cibles)
                        for i, c in enumerate(cibles_potentielles):
                            print(f"{i+1}. {c.nom} ({c.pv} PV)")
                        choix_cible = input(prompt_cible)
                        while not (choix_cible.isdigit() and 1 <= int(choix_cible) <= len(cibles_potentielles)):
                            choix_cible = input("Choix invalide. " + prompt_cible)
                        cible_choisie = cibles_potentielles[int(choix_cible)-1]
                    elif len(cibles_potentielles) > 0:
                        cible_choisie = cibles_potentielles[0]
                print("")
                if action == "1" and cible_choisie:
                    actions.attaque_physique(heros, cible_choisie)
                elif action == "2" and cible_choisie:
                    if heros.sorts_restants > 0:
                        actions.sort(heros, cible_choisie)
                        heros.sorts_restants -= 1
                    else:
                        print(f"Vous n'avez plus d'énergie pour lancer {heros.nom_sort} ! Vous perdez votre tour...")
                else:
                    print(f"{heros.nom} hésite et manque son attaque !")
                    
                if not any(m.pv > 0 for m in monstres_list):
                    print(f"\nVICTOIRE ! Tous les monstres ont été terrassés.")
                    break 
            if not any(m.pv > 0 for m in monstres_list):
                break
            print("\nTour des ennemis...")
            time.sleep(1.5)
            for monstre in monstres_list:
                if monstre.pv <= 0 or not any(h.pv > 0 for h in heros_list):
                    continue
                heros_vivants = [h for h in heros_list if h.pv > 0]
                cible_hero = random.choice(heros_vivants)
                if random.choice([True, False]) and monstre.sorts_restants > 0:
                    if monstre.nom.lower() == "polypheme":
                        print(f"{monstre.nom} hurle et lance une attaque devastatrice!")
                        actions.sort(monstre, heros_vivants)
                    else:
                        actions.sort(monstre, cible_hero)
                    monstre.sorts_restants -= 1
                else:
                    actions.attaque_physique(monstre, cible_hero)
            if not any(h.pv > 0 for h in heros_list):
                print(f"\nDÉFAITE... Vos héros ont succombé.")
                break  
            time.sleep(1.5)
            for h in heros_list:
                if h.duree_bonus > 0:
                    h.duree_bonus -= 1
                    if h.duree_bonus == 0:
                        h.bonus_degats = 0
                        print(f"Le buff de {h.nom} a expiré.")
        est_mort = not any(h.pv > 0 for h in heros_list)
        for h in heros_list:
            h.pv = h.pv_max
            h.sorts_restants = h.sorts_max
            h.bonus_degats = 0
            h.duree_bonus = 0
        if est_mort:
            print("\nVotre aventure s'arrête ici.")
            input("Appuyez sur Entrée pour revenir au menu principal...")
            break  
        print("\nLe combat est terminé.")
        print("1. Combattre un nouvel adversaire avec ces héros")
        print("2. Partir explorer avec ces héros")
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