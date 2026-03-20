import random
from data import creatures, personnages

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
    "artémis": {"physique": [d8, d8, d6], "sort": [d20, d20, d20, d20]},
    "asclépios": {"physique": d8, "sort": d20},
    "le minotaure": {"physique": d8, "sort": d6},
    "méduse": {"physique": d10, "sort": d20},
    "polypheme": {"physique": d10, "sort": [d8, d6]}
}

def lancer_des(des):
    if isinstance(des, list):
        return sum(d() for d in des)
    return des()


def est_une_creature(entity):
    noms_creatures = [creature.nom.lower() for creature in creatures.values()]
    return entity.nom.lower() in noms_creatures


def attaque_physique(atk_entity, cible):
    base = atk_entity.atk_range[0]
    des = DES_PERSONNAGE[atk_entity.nom.lower()]["physique"]
    de = lancer_des(des)
    degats = base + de + atk_entity.bonus_degats
    
    cible.pv -= degats
    bonus_str = f" + Bonus: {atk_entity.bonus_degats}" if atk_entity.bonus_degats > 0 else ""
    print(f"{atk_entity.nom} attaque {cible.nom} et inflige {degats} dégâts (Base: {base} + Dé: {de}{bonus_str})")
    if cible.pv <= 0:
        print(f"{cible.nom} est mort")


def sort(atk_entity, cible):
    base = atk_entity.sort_range[0]
    des = DES_PERSONNAGE[atk_entity.nom.lower()]["sort"]
    de = lancer_des(des)
    degats = base + de + atk_entity.bonus_degats
    
    if atk_entity.nom.lower() == "asclépios":
        c = cible[0] if isinstance(cible, list) else cible
        c.pv += degats
        if c.pv > c.pv_max:
            c.pv = c.pv_max
        if c.nom == atk_entity.nom:
            print(f"{atk_entity.nom} utilise {atk_entity.nom_sort} et se soigne de {degats} pv (Base: {base} + Dé: {de})")
        else:
            print(f"{atk_entity.nom} utilise {atk_entity.nom_sort} et soigne {c.nom} de {degats} pv (Base: {base} + Dé: {de})")
    elif atk_entity.nom.lower() == "achille":
        cibles = cible if isinstance(cible, list) else [cible]
        for c in cibles:
            c.bonus_degats = 20
            c.duree_bonus = 3
            print(f"{atk_entity.nom} utilise {atk_entity.nom_sort} ! {c.nom} gagne +20 dégâts pour 3 tours.")
    else:
        cibles = cible if isinstance(cible, list) else [cible]
        bonus_str = f" + Bonus: {atk_entity.bonus_degats}" if atk_entity.bonus_degats > 0 else ""
        for c in cibles:
            c.pv -= degats
            print(f"{atk_entity.nom} utilise {atk_entity.nom_sort} sur {c.nom} et inflige {degats} dégâts (Base: {base} + Dé: {de}{bonus_str})")
            if c.pv <= 0:
                print(f"{c.nom} est mort")

def afficher_stat(entity):
    print(f"{entity.nom} : {entity.pv}/{entity.pv_max} pv")