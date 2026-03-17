# Listes d'objets : vos catalogues d'armes et de monstres
import random

class Entities:
    def __init__(self, nom, pv,atk_range, sort_range, nom_sort):
        self.nom = nom
        self.pv = pv
        self.pv_max = pv
        self.atk_range = atk_range
        self.sort_range = sort_range
        self.nom_sort = nom_sort

personnages = {
    "achille": Entities(
        nom="Achille",
        pv_max=150,
        atk_range=(12, 18),
        sort_range=(20, 30),
        nom_sort="Colère du Péléide"
    ),
    "artemis": Entities(
        nom="Artémis",
        pv_max=80,
        atk_range=(15, 35),
        sort_range=(40, 60),
        nom_sort="Flèche d'Argent"
    ),
    "asclepios": Entities(
        nom="Asclépios",
        pv_max=110,
        atk_range=(8,12),
        sort_range=(30, 50),
        nom_sort="Souffle de Vie"
    )
}


creatures = {
    "minotaure": Entities(
        nom="Le Minotaure",
        pv_max=180,
        atk_range=(10, 15),
        sort_range=(15, 25),
        nom_sort="Frénésie"
    ),
    "meduse": Entities(
        nom="Méduse",
        pv_max=90,
        atk_range=(5, 15),
        sort_range=(45, 70),
        nom_sort="Regard de Pierre"
    )
}

RESET = "\033[0m"

couleurs = {
    "Le Mont Olympe": "\033[93m",
    "Les Enfers d'Hadès": "\033[91m",
    "Le Labyrinthe du Minotaure": "\033[90m",
    "Le Temple de Poséidon": "\033[94m",
    "La Forêt d'Artémis": "\033[92m",
    "La Caverne de Méduse": "\033[95m",
    "L'Île des Sirènes": "\033[96m",
    "Le Palais d'Athéna": "\033[94m",
    "Le Champ de Bataille d'Arès": "\033[91m",
    "Le Jardin d'Héra": "\033[92m",
    "La Forge d'Héphaïstos": "\033[33m",
    "Le Sanctuaire d'Apollon": "\033[93m",
    "Le Temple de Déméter": "\033[92m",
    "La Vallée de Dionysos": "\033[95m",
    "La Cité Perdue de Troie": "\033[33m",
    "Le Fleuve Styx": "\033[90m",
    "La Prison des Titans": "\033[31m",
    "Le Royaume des Cyclopes": "\033[37m",
    "Le Sommet Sacré de Delphes": "\033[93m",
    "Le Port Antique d'Ithaque": "\033[96m"
}

zones = list(couleurs.keys())

descriptions = {
    "Le Mont Olympe": "Tu gravis lentement les pentes du Mont Olympe. Selon les anciennes légendes, c'est ici que résident Zeus et les autres dieux de l'Olympe. Les nuages tourbillonnent autour des colonnes de marbre géantes. L'air semble chargé d'une énergie divine, comme si chaque pas que tu fais était observé par les immortels.",
    
    "Les Enfers d'Hadès": "Tu franchis une porte de pierre ancienne et l'air devient soudain glacial. Devant toi s'étend le royaume des morts gouverné par Hadès. Des murmures lointains résonnent dans l'obscurité et le fleuve Styx coule lentement non loin. Ici, les âmes perdues errent pour l'éternité.",
    
    "Le Labyrinthe du Minotaure": "Les murs gigantesques du labyrinthe se dressent autour de toi. Construit autrefois par Dédale, ce dédale de pierre était destiné à enfermer le terrible Minotaure. Chaque couloir semble identique et les échos de tes pas résonnent comme si quelque chose te suivait dans l'ombre.",
    
    "Le Temple de Poséidon": "Les vagues frappent violemment les falaises près du temple. Les colonnes blanches se dressent face à l'océan infini. On raconte que Poséidon lui-même pouvait apparaître ici pour calmer ou déchaîner les mers.",
    
    "La Forêt d'Artémis": "Une forêt dense et mystérieuse s'étend devant toi. Ce territoire sacré appartient à Artémis, déesse de la chasse. Les arbres sont anciens et immenses, et les animaux semblent t'observer silencieusement entre les branches.",
    
    "La Caverne de Méduse": "La caverne est sombre et froide. Autour de toi se dressent des statues humaines figées dans la pierre. Selon les mythes, quiconque croisait le regard de Méduse était immédiatement pétrifié.",
    
    "L'Île des Sirènes": "Le vent transporte un chant envoûtant au-dessus des vagues. Les marins racontaient que les sirènes attiraient les voyageurs avec leur voix avant de les mener à leur perte.",
    
    "Le Palais d'Athéna": "Des colonnes majestueuses entourent ce palais antique dédié à Athéna, déesse de la sagesse et de la stratégie. Les murs sont couverts de fresques racontant d'anciennes batailles et des exploits héroïques.",
    
    "Le Champ de Bataille d'Arès": "Le sol est marqué par les traces de guerres anciennes. Des armes brisées et des boucliers abandonnés reposent encore ici. Arès, dieu de la guerre, était honoré dans ce lieu où les combats faisaient rage.",
    
    "Le Jardin d'Héra": "Un jardin magnifique rempli de plantes rares et d'arbres sacrés. Selon les légendes, Héra protégeait cet endroit et y faisait pousser des fruits divins réservés aux dieux.",
    
    "La Forge d'Héphaïstos": "Un grondement métallique résonne dans la montagne. C'est ici qu'Héphaïstos, dieu forgeron, créait les armes légendaires des dieux et des héros.",
    
    "Le Sanctuaire d'Apollon": "Le soleil illumine ce sanctuaire sacré dédié à Apollon. Les anciens venaient ici pour écouter les prophéties et demander conseil aux oracles.",
    
    "Le Temple de Déméter": "Les champs fertiles entourent ce temple consacré à Déméter, déesse de l'agriculture. L'air est paisible mais chargé de mystère.",
    
    "La Vallée de Dionysos": "Des vignes couvrent toute la vallée. Dionysos, dieu du vin et des fêtes, était célébré ici lors de grandes célébrations.",
    
    "La Cité Perdue de Troie": "Les ruines de Troie se dressent devant toi. Cette ville légendaire fut le théâtre d'une guerre mythique entre héros et rois.",
    
    "Le Fleuve Styx": "Les eaux sombres du Styx séparent le monde des vivants et celui des morts. Les âmes doivent le traverser pour rejoindre les Enfers.",
    
    "La Prison des Titans": "Un lieu ancien où les Titans furent enfermés après leur défaite contre les dieux de l'Olympe.",
    
    "Le Royaume des Cyclopes": "Dans ces montagnes vivent les Cyclopes, géants possédant un seul œil et une force immense.",
    
    "Le Sommet Sacré de Delphes": "Les prêtresses de Delphes rendaient ici les prophéties d'Apollon. Les rois et héros venaient consulter l'oracle.",
    
    "Le Port Antique d'Ithaque": "C'est depuis ce port que le héros Ulysse partit pour son long voyage à travers les mers et les dangers mythologiques."
}


Coffre = {
    "Coffre ancien",
    "Coffre mystérieux",
    "Coffre doré"
}

class Objects:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

objets = {
    "Flèches d'Artémis": Objects(
        nom="Flèches d'Artémis",
        description="Des flèches enchantées par la déesse de la chasse, capables de percer n'importe quelle armure."
    ),
    "Épée d'Arès": Objects(
        nom="Épée d'Arès",
        description="Une épée légendaire forgée par Héphaïstos, symbole de la puissance de la guerre."
    ),

    "Oeil de Cyclope": Objects(
        nom="Oeil de Cyclope",
        description="Un œil unique d'un Cyclope, réputé pour conférer une force surhumaine à celui qui le possède."
    ),
    "Ambroisie": Objects(
        nom="Ambroisie",
        description="Un nectar divin qui confère l'immortalité aux dieux et aux héros."
    ),
    "Plume d'Icar": Objects(
        nom="Plume d'Icar", 
        description="Une plume provenant des ailes d'Icar, une des responsables de sa chute. N'essayez pas de l'utiliser."
    ),
    "Fruits d'Héra": Objects(
        nom="Fruits d'Héra",
        description="Des fruits rares cultivés dans le jardin d'Héra, réputés pour leur capacité à restaurer la santé et la vitalité."
    ),
    "Vent en bouteille": Objects(
        nom="Vent en bouteille",
        description="Un vent capturé dans une bouteille, capable de propulser son porteur à grande vitesse ou de créer une tempête dévastatrice."
    ),
    "Sang de chimère": Objects(
        nom="Sang de chimère",
        description="Le sang d'une chimère, une créature mythique composée de plusieurs animaux."
    )

}

objects_disponibles = {
        "Commun":["Oeil de Cyclope", "Vent en bouteille"],
        "Rare":["Ambroisie","Sang de chimère","Fruits d'Héra"],
        "Légendaire":["Flèches d'Artémis", "Épée d'Arès","Plume d'Icar"]
    }
    
#à copier autre part je pense, genre dans le truc de loot
raretes = ["Commun", "Rare", "Légendaire"]
probabilites = [60, 30,10]
