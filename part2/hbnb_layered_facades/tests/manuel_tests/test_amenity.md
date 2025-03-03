# Résultats Test Manuels - API HBnB
## Test 1 : Création d'une amenity valide
### Description:
Vérification création amenity via une requête POST avec les informations nécessaires.
### Requête CURL:
```bash
curl -X POST "http://127.0.0.1:5000/api/v1/amenities/" \
-H "Content-Type: application/json" \
-d '{"name": "piscine"}'
```
### Résultat
```json
{
    "id": "f6f51b56-5006-4e30-aaeb-5c2ada4ff06b",
    "name": "piscine"
}
// 201 CREATED
```
## Test 2 : Récupération liste amenity
### Description:
Vérification création amenity via une requête POST avec les informations nécessaires.
### Requête CURL:
```bash
curl GET 'http://127.0.0.1:5000/api/v1/amenities/'
```
### Résultat
```json
[
    {
        "id": "f6f51b56-5006-4e30-aaeb-5c2ada4ff06b",
        "name": "piscine"
    }
]
// 200 OK
```