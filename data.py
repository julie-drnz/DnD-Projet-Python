import random

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

LISTE_HEROS = []
LISTE_MONSTRES = []