# data.py
# Fichier de données géré par le Joueur 1 (Collaborateur)

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
    "Le Mont Olympe": "Tu gravis lentement les pentes du Mont Olympe. Selon les anciennes légendes, c'est ici que résident Zeus et les autres dieux de l'Olympe. Les nuages tourbillonnent autour des colonnes de marbre géantes. L'air semble chargé d'une énergie divine.",
    "Les Enfers d'Hadès": "Tu franchis une porte de pierre ancienne et l'air devient soudain glacial. Devant toi s'étend le royaume des morts gouverné par Hadès. Des murmures lointains résonnent dans l'obscurité.",
    "Le Labyrinthe du Minotaure": "Les murs gigantesques du labyrinthe se dressent autour de toi. Construit autrefois par Dédale, ce dédale de pierre était destiné à enfermer le terrible Minotaure.",
    "Le Temple de Poséidon": "Les vagues frappent violemment les falaises près du temple. Les colonnes blanches se dressent face à l'océan infini. On raconte que Poséidon lui-même pouvait apparaître ici.",
    "La Forêt d'Artémis": "Une forêt dense et mystérieuse s'étend devant toi. Ce territoire sacré appartient à Artémis, déesse de la chasse. Les arbres sont anciens et immenses.",
    "La Caverne de Méduse": "La caverne est sombre et froide. Autour de toi se dressent des statues humaines figées dans la pierre. Quiconque croisait le regard de Méduse était pétrifié.",
    "L'Île des Sirènes": "Le vent transporte un chant envoûtant au-dessus des vagues. Les marins racontaient que les sirènes attiraient les voyageurs avec leur voix.",
    "Le Palais d'Athéna": "Des colonnes majestueuses entourent ce palais antique dédié à Athéna, déesse de la sagesse et de la stratégie. Les murs sont couverts de fresques mythiques.",
    "Le Champ de Bataille d'Arès": "Le sol est marqué par les traces de guerres anciennes. Des armes brisées et des boucliers abandonnés reposent encore ici, honorant le dieu de la guerre.",
    "Le Jardin d'Héra": "Un jardin magnifique rempli de plantes rares et d'arbres sacrés. Selon les légendes, Héra y faisait pousser des fruits divins réservés aux dieux.",
    "La Forge d'Héphaïstos": "Un grondement métallique résonne dans la montagne. C'est ici qu'Héphaïstos créait les armes légendaires des dieux.",
    "Le Sanctuaire d'Apollon": "Le soleil illumine ce sanctuaire sacré dédié à Apollon. Les anciens venaient ici pour écouter les prophéties des oracles.",
    "Le Temple de Déméter": "Les champs fertiles entourent ce temple consacré à Déméter, déesse de l'agriculture. L'air est paisible mais chargé de mystère.",
    "La Vallée de Dionysos": "Des vignes couvrent toute la vallée. Dionysos, dieu du vin et des fêtes, était célébré ici lors de grandes célébrations.",
    "La Cité Perdue de Troie": "Les ruines de Troie se dressent devant toi. Cette ville légendaire fut le théâtre d'une guerre mythique entre héros et rois.",
    "Le Fleuve Styx": "Les eaux sombres du Styx séparent le monde des vivants et celui des morts. Les âmes doivent le traverser pour rejoindre les Enfers.",
    "La Prison des Titans": "Un lieu ancien où les Titans furent enfermés après leur défaite contre les dieux de l'Olympe.",
    "Le Royaume des Cyclopes": "Dans ces montagnes vivent les Cyclopes, géants possédant un seul œil et une force immense.",
    "Le Sommet Sacré de Delphes": "Les prêtresses de Delphes rendaient ici les prophéties d'Apollon. Les rois venaient consulter l'oracle.",
    "Le Port Antique d'Ithaque": "C'est depuis ce port que le héros Ulysse partit pour son long voyage à travers les mers."
}



# --- Section pour le Joueur 3 (Toi) ---
# Ces listes seront remplies plus tard avec les Héros et Monstres créés par le Joueur 1
LISTE_HEROS = []
LISTE_MONSTRES = []