# README : JavaScript DOM Manipulation

Bienvenue dans ce projet sur la **manipulation du DOM en JavaScript** !  
Ce README vous guidera sur les objectifs, contenus, exigences et bonnes pratiques pour exploiter au mieux ce dépôt.

## Objectifs du Projet

- Comprendre ce qu'est le DOM (*Document Object Model*) et comment il représente une page web.
- Savoir sélectionner, modifier, créer et supprimer des éléments du DOM avec JavaScript.
- Gérer les événements utilisateurs (clics, saisies clavier, etc.).
- Appliquer vos connaissances pour rendre une page web interactive.

## Prérequis

- Connaissances de base en HTML et CSS.
- Notions fondamentales en JavaScript (variables, fonctions, boucles).

## Contenus

Ce projet vous permettra de couvrir :

### 1. Sélection des éléments du DOM
- `getElementById`
- `getElementsByClassName`
- `getElementsByTagName`
- `querySelector` et `querySelectorAll`

### 2. Modification du DOM
- Modifier le texte (`.textContent`, `.innerText`, `.innerHTML`)
- Modifier les attributs (`.setAttribute`, `.getAttribute`)
- Modifier les styles (via `.style` ou ajout/suppression de classes)

### 3. Création et suppression d’éléments
- `createElement`, `appendChild`, `removeChild`, etc.

### 4. Gestion des événements
- Attacher des gestionnaires d’événements avec `addEventListener`
- Les types d’événements courants (click, mouseover, keyup...)

## Structure du Dépôt

```sh
.
├── 0-select_element.js
├── 1-modify_text.js
├── 2-add_event.js
├── 3-create_element.js
├── 4-remove_element.js
├── index.html
└── README.md
```

- **index.html** : Page de test pour vos scripts JavaScript.
- **X-*.js** : Fichiers d’implémentation, correspondant à chaque étape/exercice.

## Instructions

1. Ouvrez index.html dans votre navigateur.
2. Lisez et complétez chaque fichier JavaScript en respectant la consigne de l’exercice.
3. Rafraîchissez la page pour voir vos modifications et tester le comportement du DOM.
4. Utilisez `console.log()` pour vérifier vos résultats ou déboguer.

## Bonnes Pratiques

- Commentez votre code pour expliquer vos choix.
- N’utilisez **jamais** `document.write` ni des méthodes obsolètes.
- Privilégiez la manipulation avec `addEventListener` plutôt qu’en écrivant du JavaScript directement dans le HTML.
- Séparez bien le JS du HTML et du CSS.

## Quelques Liens Utiles

- [MDN Web Docs - Manipulation du DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction)
- [MDN Web Docs - addEventListener](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener)
- [MDN Web Docs - querySelector](https://developer.mozilla.org/fr/docs/Web/API/Document/querySelector)

## Auteurs

- Projet réalisé dans le cadre de **Holberton School**
- Rédigé par : Vivien Bernardot
