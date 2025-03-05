## Structure generale du projet

hbnb/
├── app/
│   ├── api/                     # Gestion des endpoints API
│   │   ├── v1/                   # Version 1 de l'API
│   │   │   ├── users_endpoints.py  # Endpoints liés aux utilisateurs
│   │   │   ├── places_endpoints.py # Endpoints liés aux hébergements
│   │   │   ├── reviews_endpoints.py # Endpoints liés aux avis
│   │   │   ├── amenities_endpoints.py # Endpoints liés aux équipements
│   ├── models/                  # Modèles de données
│   │   ├── base_model.py         # Modèle de base abstrait
│   │   ├── user_model.py         # Modèle pour les utilisateurs
│   │   ├── place_model.py        # Modèle pour les hébergements
│   │   ├── review_model.py       # Modèle pour les avis
│   │   ├── amenity_model.py      # Modèle pour les équipements
│   ├── services/                 # Logique métier
│   │   ├── user_service.py       # Service pour gérer les utilisateurs
│   │   ├── place_service.py      # Service pour gérer les hébergements
│   │   ├── review_service.py     # Service pour gérer les avis
│   │   ├── amenity_service.py    # Service pour gérer les équipements
│   │   ├── app_facade.py         # Façade principale pour centraliser les services
│   ├── persistence/              # Gestion de la persistance des données
│   │   ├── repository.py         # Interface générique pour interagir avec la base de données
│   │   ├── gateways/             # Accès aux systèmes externes
│   │   │   ├── user_gateway.py   # Intégration externe pour les utilisateurs
│   │   │   ├── place_gateway.py  # Intégration externe pour les hébergements
│   │   │   ├── review_gateway.py # Intégration externe pour les avis
│   │   │   ├── amenity_gateway.py # Intégration externe pour les équipements
│   ├── tests/
│   │   ├── manual_tests/
│   │   │   ├── test_amenity.md    # Test manuel pour amenités 
│   │   │   ├── test_user.md       # Test manuel pour users
│   │   │   ├── test_review.md     # Test manuel pour reviews
│   │   │   ├── test_place.md      # Test manuel pour places
│   │   ├── test_api_amenities.py  # Unittest pour amenities
│   │   ├── test_api_users.py      # Unittest pour users
│   │   ├── test_api_reviews.py    # Unittest pour reviews
│   │   ├── test_api_places.py     # Unittest pour places
├── run.py                        # Point d'entrée principal de l'application
├── config/                       # Configuration du projet
├── tests/                        # Tests unitaires et d'intégration
└── requirements.txt               # Dépendances Python

##  Explication des Composants Clés

### 1 API (app/api/)

- Utilise Flask-RESTx pour gérer les routes de l'API REST.
- Les différentes versions sont contenues dans des sous-dossiers (v1/).
- Chaque entité importante (utilisateurs, places, avis, équipements) a ses propres endpoints.

### 2 Modèles (app/models/)

- Définissent la structure des données et les interactions avec la base de données.
- base_model.py sert de classe parent pour factoriser les comportements communs.
- Chaque entité (User, Place, Review, etc.) a son propre modèle.

### 3 Services (app/services/)

- Contient la logique métier de l'application.
- Sépare la gestion des données de la couche API pour plus de flexibilité.
- app_facade.py sert de point central pour orchestrer les services.

### 4 Persistence & Gateways (app/persistence/)

- repository.py est une interface générique pour interagir avec la base de données.
- Le dossier gateways/ permet d'intégrer des services externes (ex : API de paiement, services de localisation).

### 5 Configuration (config/)

- Centralise les paramètres selon l'environnement : développement, test, production.
- Permet une adaptation facile sans modifier directement le code source.

### 6 Tests (tests/)

- Contient des tests unitaires pour chaque service et modèle.
- Permet d'assurer la robustesse du code avant chaque mise en production.

🛑 **Attention** : 

La fonction utiliser pour vérifier la validité d'une adresse e-mail vérifie également l'existance du nom de domaine
(une adresse comme xxxx@example.com ne fonctionnera pas utiliser plutôt une adresse comme xxxx@gmail.com)
