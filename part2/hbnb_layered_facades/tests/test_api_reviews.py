import unittest
from app import create_app
from flask import json

class TestReviewEndpoints(unittest.TestCase):
    """Tests des endpoints API reviews"""

    def setUp(self):
        """Initialisation du client de test"""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        """Test: création d'une review"""
        # Création d'une review
        response = self.client.post('/api/v1/reviews/', json={
            "place_id": 1,
            "user_id": 1,
            "text": "Super séjour dans cet appartement !",
            "rating": 5
        })
        self.assertEqual(response.status_code, 201)
        review_data = response.get_json()
        self.assertEqual(review_data["text"], "Super séjour dans cet appartement !")
        self.assertEqual(review_data["rating"], 5)

    def test_get_all_reviews(self):
        """Test: obtenir toutes les reviews"""
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
        reviews = response.get_json()
        self.assertIsInstance(reviews, list)

    def test_get_reviews_by_place(self):
        """Test: obtenir les reviews d'une place spécifique"""
        place_id = 1  # Remplace par l'ID d'une place existante
        response = self.client.get(f'/api/v1/places/{place_id}/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = response.get_json()
        self.assertIsInstance(reviews, list)
        for review in reviews:
            self.assertEqual(review["place_id"], place_id)

    def test_delete_review(self):
        """Test: suppression d'une review"""
        # Création d'une review
        create_response = self.client.post('/api/v1/reviews/', json={
            "place_id": 1,
            "user_id": 1,
            "text": "Super séjour dans cet appartement !",
            "rating": 5
        })
        review_data = create_response.get_json()
        review_id = review_data["id"]

        # Suppression de la review
        delete_response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(delete_response.status_code, 200)
        delete_data = delete_response.get_json()
        self.assertTrue(delete_data["deleted"])

        # Vérification que la review a bien été supprimée
        get_response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(get_response.status_code, 404)

    def test_delete_nonexistent_review(self):
        """Test: suppression d'une review inexistante"""
        response = self.client.delete('/api/v1/reviews/99999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()