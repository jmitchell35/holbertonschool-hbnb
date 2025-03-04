import unittest
from app import create_app
from flask import json

class TestPlaceEndpoints(unittest.TestCase):
    """Tests des endpoints API places"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        """Test: création d'un lieu"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Villa Paradiso",
            "description": "paradisiac",
            "price": 120.0,
            "latitude": 40.0,
            "longitude": 70.0,
            "owner_id": "12345"
        })
        self.assertEqual(response.status_code, 201)

        data = response.get_json()
        self.assertEqual(data["name"], "Villa Paradiso")

    def test_get_place(self):
        """Test: récupérer un lieu existant"""
        create_response = self.client.post('/api/v1/places/', json={
            "title": "Cabane en forêt",
            "description": "mousseux",
            "price": 80.0,
            "latitude": 40.0,
            "longitude": 70.0,
            "owner_id": "12345"
        })
        place_id = create_response.get_json().get("id")

        get_response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(get_response.status_code, 200)

        data = get_response.get_json()
        self.assertEqual(data["name"], "Cabane en forêt")

    def test_get_all_places(self):
        """Test: obtenir toutes les places"""
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
        places = response.get_json()
        self.assertIsInstance(places, list)  # Vérifie que réponse est une liste
        if places:  # Vérifie que si places existent, ont bien les bons champs
            for place in places:
                self.assertIn('title', place)
                self.assertIn('description', place)
                self.assertIn('price', place)
                self.assertIn('latitude', place)
                self.assertIn('longitude', place)
                self.assertIn('owner_id', place)

    def test_update_place(self):
        """Test: mise à jour d'une place"""
        # Création d'une place
        create_response = self.client.post('/api/v1/places/', json={
            "title": "Appartement 1 chambre",
            "description": "Confortable et spacieux",
            "price": 100,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": "12345"
        })
        place_data = create_response.get_json()
        place_id = place_data.get("id")

        # Mise à jour de la place
        update_response = self.client.patch(f'/api/v1/places/{place_id}',
                                            json={
            "title": "Appartement 2 chambres",
            "description": "Plus grand et mieux situé",
            "price": 150,
            "latitude": 48.8584,
            "longitude": 2.2945,
            "owner_id": "12345"
        })
        self.assertEqual(update_response.status_code, 200)

        updated_data = update_response.get_json()
        self.assertEqual(updated_data["title"], "Appartement 2 chambres")
        self.assertEqual(updated_data["price"], 150)

    def test_update_nonexistent_place(self):
        """Test: mise à jour d'une place inexistante"""
        response = self.client.patch('/api/v1/places/99999', json={
            "title": "Appartement 3 chambres",
            "description": "Spacieux et moderne",
            "price": 200,
            "latitude": 48.8600,
            "longitude": 2.2950,
            "owner_id": "12345"
        })
        self.assertEqual(response.status_code, 404)

    def test_update_place_invalid_data(self):
        """Test: tentative de mise à jour avec des données invalides"""
        # Création d'une place
        create_response = self.client.post('/api/v1/places/', json={
            "title": "Appartement 1 chambre",
            "description": "Confortable et spacieux",
            "price": 100,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": "12345"
        })
        place_id = create_response.get_json().get("id")

        # Tentative de mise à jour avec un prix négatif
        update_response = self.client.patch(f'/api/v1/places/{place_id}',
                                            json={
            "title": "Appartement 2 chambres",
            "description": "Plus grand et mieux situé",
            "price": -150,
            "latitude": 48.8584,
            "longitude": 2.2945,
            "owner_id": "12345"
        })
        self.assertEqual(update_response.status_code, 400)

if __name__ == '__main__':
    unittest.main()