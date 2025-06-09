
# restful-api

API RESTful de gestion de ressources — Exemple de projet

## Description

Ce projet propose une implémentation d’API web RESTful conforme aux bonnes pratiques modernes. Il s’appuie sur les principes de REST (Representational State Transfer) : manipulation de ressources via des URI, utilisation des méthodes HTTP standards (`GET`, `POST`, `PUT`, `DELETE`), et échanges de données au format JSON.

L’API est conçue pour être indépendante de la plateforme, faiblement couplée et facilement extensible. Elle permet, par exemple, la gestion d’une collection de ressources (utilisateurs, tâches, articles, etc.) à travers des endpoints clairs et intuitifs.

---

## Fonctionnalités principales

- **CRUD** complet sur les ressources (Create, Read, Update, Delete)
- Utilisation des méthodes HTTP standard
- Réponses structurées avec des codes d’état HTTP appropriés
- Échange de données au format JSON
- Respect du modèle sans état (stateless)
- Organisation claire des URI autour des ressources

---

## Structure type d’une API RESTful

```
/resources          # Collection de ressources (ex: /users, /tasks)
/resources/{id}     # Ressource individuelle (ex: /users/123)
/resources/{id}/subresources # Sous-ressources éventuelles
```

Exemple d’URI :  
`GET /users/5` → récupère l’utilisateur avec l’ID 5.

---

## Exemples de requêtes

### Récupérer la liste des ressources

```http
GET /tasks
```

### Créer une nouvelle ressource

```http
POST /tasks
Content-Type: application/json

{
  "title": "Lire la documentation REST",
  "done": false
}
```

### Modifier une ressource

```http
PUT /tasks/42
Content-Type: application/json

{
  "title": "Lire la documentation REST (mis à jour)",
  "done": true
}
```

### Supprimer une ressource

```http
DELETE /tasks/42
```

---

## Principales méthodes HTTP

| Méthode | Description                            | Exemple d’usage                      |
|---------|----------------------------------------|--------------------------------------|
| GET     | Lire une ou plusieurs ressources       | `GET /users`                         |
| POST    | Créer une nouvelle ressource           | `POST /users`                        |
| PUT     | Remplacer entièrement une ressource    | `PUT /users/5`                       |
| PATCH   | Modifier partiellement une ressource   | `PATCH /users/5`                     |
| DELETE  | Supprimer une ressource                | `DELETE /users/5`                    |

---

## Codes d’état HTTP courants

| Code | Signification             | Scénario typique                                 |
|------|--------------------------|--------------------------------------------------|
| 200  | OK                       | Requête réussie, données retournées              |
| 201  | Created                  | Ressource créée avec succès                      |
| 204  | No Content               | Suppression réussie, pas de contenu à renvoyer   |
| 400  | Bad Request              | Erreur de syntaxe dans la requête                |
| 401  | Unauthorized             | Authentification requise                         |
| 403  | Forbidden                | Accès refusé                                     |
| 404  | Not Found                | Ressource inexistante                            |
| 500  | Internal Server Error    | Erreur inattendue côté serveur                   |

---

## Bonnes pratiques de conception

- Utiliser des noms de ressources au pluriel pour les collections (`/users`, `/tasks`)
- Éviter les verbes dans les URI (préférer `/tasks` à `/create-task`)
- Retourner des codes d’état HTTP adaptés à chaque situation
- Fournir une documentation claire et à jour

---

## Exemple d’appel à une API REST publique

Appel à l’API Wikipédia pour obtenir un extrait d’article :

```
GET https://fr.wikipedia.org/w/api.php?action=query&titles=Terre&prop=extracts&exchars=500&explaintext&utf8&format=json
```

---

## Pour aller plus loin

- [Meilleures pratiques RESTful (Microsoft)](https://learn.microsoft.com/fr-fr/azure/architecture/best-practices/api-design)
- [Exemples d’API REST (OpenClassrooms)](https://openclassrooms.com/fr/courses/6573181-adoptez-les-api-rest-pour-vos-projets-web/6824631-definissez-la-structure-de-votre-api-rest)

---

## Auteur

Projet réalisé dans le cadre d’un apprentissage ou d’un développement professionnel autour des API RESTful.
# Vivien Bernardot student Holberton school Dijon(21)(C26)

---
