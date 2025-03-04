# Résultats Test Manuels - API HBnB
## Test 1 : Création d'une review valide
### Description:
Vérification création review via une requête POST avec les informations nécessaires.
### Requête CURL:
```bash
curl -X POST http://127.0.0.1:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{"text": "hjifihrei", "rating": 8, "user_id": "c267695e-9741-4a79-ac03-00f423a5724e", "place_id": "caacf2d0-b880-4af3-8877-f94bc2bfcf6f"}'
```
### Résultat
```json
{

}
// 201 CREATED
```