# README: Application de Cryptage et Décryptage

## Description
Cette application Python offre une interface graphique (Tkinter) permettant de :

1. Crypter plusieurs messages en utilisant une clé générée aléatoirement.
2. Décrypter des messages cryptés en fournissant une clé valide.

Le cryptage repose sur un remplacement aléatoire de caractères basé sur une clé unique générée pour chaque session. Cette clé est essentielle pour le décryptage.

Cette application peut également être utilisée pour crypter des mots de passe avant de les stocker ou de les transmettre de manière sécurisée.

**Note importante :** Pour garantir la sécurité des mots de passe, **ne jamais envoyer le mot de passe et la clé de décryptage dans le même message**. Utilisez deux moyens de communication différents pour transmettre ces informations.

---

## Fonctionnalités principales

### 1. Cryptage des messages
- L'utilisateur peut choisir le nombre de messages à crypter.
- Chaque message est transformé en supprimant les espaces et en mettant la lettre suivante en majuscule.
- Les messages sont cryptés en utilisant une clé aléatoire.
- La clé de cryptage est affichée pour être sauvegardée.

### 2. Décryptage des messages
- L'utilisateur peut décrypter plusieurs messages cryptés en utilisant la clé générée lors du cryptage.
- La clé est analysée et validée avant le décryptage.

---

## Prérequis

- **Python 3.7 ou supérieur**
- Bibliothèques Python :
  - `tkinter` (intégré avec Python)
  - `random` (intégré avec Python)

---

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers source.
   ```bash
   git clone <URL_DU_DEPOT>
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd <NOM_DU_REPERTOIRE>
   ```

---

## Utilisation

### Lancer l'application
1. Exécutez le fichier principal :
   ```bash
   python cryptage.py
   ```
2. Une interface graphique s'ouvre avec les options :
   - Crypter des messages
   - Décrypter des messages

### Instructions
#### Cryptage :
1. Cliquez sur "Crypter des messages".
2. Entrez le nombre de messages à crypter.
3. Remplissez les champs avec vos messages ou mots de passe.
4. Une clé unique sera générée avec les messages cryptés.

#### Décryptage :
1. Cliquez sur "Décrypter des messages".
2. Entrez le nombre de messages à décrypter.
3. Fournissez les messages cryptés et la clé.
4. Les messages originaux seront affichés si la clé est valide.

---

## Structure du projet

```
Projet
├── cryptage.py             # Fichier principal
├── README.md               # Documentation
```

---

## Exemple de Clé
Une clé générée pourrait ressembler à ceci :
```
a:/,b:Y,c:7,d:!,e:E,...
```
Assurez-vous de sauvegarder cette clé pour le décryptage.

---

## Auteurs
- **Luc Valette**

---

## Licence
Ce projet est distribué sous licence **MIT**.

### À propos de la licence MIT
La licence MIT est une licence open-source permissive qui permet :
- L'utilisation commerciale et personnelle du logiciel.
- La modification et la redistribution du code source.
- L'inclusion du code dans des projets propriétaires.

**Obligations de l'utilisateur :**
- Inclure une copie de la licence dans toutes les redistributions.
- Mentionner l'auteur original du logiciel.

Pour plus d'informations, consultez le fichier `LICENSE` ou rendez-vous sur [Open Source Initiative - MIT License](https://opensource.org/licenses/MIT).

