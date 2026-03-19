import random

def d4():
    return random.randint(1, 4)

def d6():
    return random.randint(1, 6)

def d8():
    return random.randint(1, 8)

def d10():
    return random.randint(1, 10)

def d12():
    return random.randint(1, 12)

def d20():
    return random.randint(1, 20)

DES_PERSONNAGE = {
    "achille": {"physique": d6, "sort": d8},
    "artémis": {"physique": d8, "sort": d12},
    "asclépios": {"physique": d4, "sort": d12},
    "le minotaure": {"physique": d8, "sort": d6},
    "méduse": {"physique": d4, "sort": d20}
}
def attaque_physique(atk_entity, cible):
    """Attaque physique avec dé fixe selon personnage"""
    degats = DES_PERSONNAGE[atk_entity.nom.lower()]["physique"]() + atk_entity.atk_range[0]
    cible.pv -= degats
    print(f"{atk_entity.nom} attaque {cible.nom} et inflige {degats} dégâts")
    if cible.pv <= 0:
        print(f"{cible.nom} est mort")
def sort(atk_entity, cible):
    """Sort spécial avec dé fixe selon personnage"""
    degats = DES_PERSONNAGE[atk_entity.nom.lower()]["sort"]() + atk_entity.sort_range[0]
    if atk_entity.nom.lower() == "asclépios":
        atk_entity.pv += degats
        if atk_entity.pv > atk_entity.pv_max:
            atk_entity.pv = atk_entity.pv_max
        print(f"{atk_entity.nom} utilise {atk_entity.nom_sort} et se soigne de {degats} pv")
    else:
        cible.pv -= degats
        print(f"{atk_entity.nom} utilise {atk_entity.nom_sort} sur {cible.nom} et inflige {degats} dégâts")
        if cible.pv <= 0:
            print(f"{cible.nom} est mort")
def afficher_stat(entity):
    print(f"{entity.nom} : {entity.pv}/{entity.pv_max} pv")