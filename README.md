# 🎲 L'Échiquier de l'Oracle - Projet POO Python (DnD)

## 📜 Description du Projet
Ce projet est un système de jeu de combat RPG simplifié inspiré de l'univers de Donjons & Dragons et de la mythologie grecque. Il a été développé dans le cadre d'un projet académique visant à mettre en pratique les concepts de Programmation Orientée Objet (POO) en Python, avec une attention particulière portée sur la création de classes (`Entities`, `Objects`), l'encapsulation des données et la séparation modulaire des responsabilités.

## 👥 L'Équipe
Ce projet a été réalisé par un groupe de 4 personnes :
- Adel REDJEMI
- Julie DI RENZO
- Nicolas RABIAN
- Ilian ULLOA

**Planification du projet :**
- https://trello.com/b/6FCdLHUc/projet-transversal-poo

## 🛠️ Prérequis
Pour exécuter ce projet, vous aurez besoin de :
- **Python 3.x** installé sur votre machine.
- Aucun module externe n'est requis (le projet utilise uniquement des bibliothèques standards ou _built-in_ de Python telles que `os`, `time`, et `random`).

## 🚀 Comment lancer le jeu
1. Ouvrez un terminal.
2. Clonez ce dépôt ou naviguez vers le dossier du projet via la console :
   ```bash
   cd chemin/vers/DnD-Projet-Python
   ```
3. Exécutez le script principal avec la commande suivante :
   ```bash
   python main.py
   ```
   *(ou `python3 main.py` selon votre système d'exploitation)*

## ✨ Fonctionnalités du Programme

### 1. Système de Combat (Jouer)
- Implémentation du rôle d'un Maître du Jeu (MJ) qui gère les rencontres.
- Préparation des combats en sélectionnant deux héros et choix de monstre aléatoire.
- Les entités du jeu (Héros et Monstres) mythologiques tels qu'Achille, Artémis, Le Minotaure, Méduse ou Polypheme (définis dans `data.py`) possèdent des statistiques propres (Points de vie, plages de dégâts d'attaque classique, sorts spéciaux, dégats de zone, buff, soin).


### 2. Exploration (Fonctionnalité Supplémentaire)
- **Les visions de l'Oracle :** Une fonctionnalité d'exploration textuelle ajoutée indépendamment des prérequis de base.
- Permet au joueur sélectionnant cette option de découvrir 3 zones aléatoires (parmi 20 zones mythologiques uniques comme *Le Mont Olympe*, *Les Enfers d'Hadès*, etc.).
- Affichage dynamique stylisé par des codes couleurs CLI dans le terminal.
- Découverte de coffres (Ancien, Mystérieux, Doré) censés renfermer des objets variés classés par rareté (Commun, Rare, Légendaire).

## 🏗️ Architecture Technique (POO)
Le projet utilise un découpage modulaire respectant les concepts fondamentaux de la Programmation Orientée Objet :
- `main.py` : Point d'entrée du programme et boucle principale du jeu (Menu REPL).
- `data.py` : Base de données instanciant les différentes `Entities` (personnages, créatures) et `Objects` (armes, loot). Contient également les listes de zones et de raretés.
- `actions.py` : Logique de combat, gestion des lancers de dés (d4, d6, d8, d20...) et fonctions de résolution des attaques physiques et magiques.

## 🎮 Jouabilité
Plongez dans les mythes grecs ! Incarnez des figures de légende et affrontez les monstres les plus redoutables de l'histoire antique. Le Maître du Jeu utilise cette interface console pour gérer le flot du récit et lancer les dés pour dicter le destin des joueurs.

---
*Projet réalisé dans le cadre du cours Advanced 2 - POO Python.*
