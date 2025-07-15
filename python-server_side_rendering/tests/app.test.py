from task_03_files import app

def test_items_page():
    with app.test_client() as client:
        response = client.get('/items')
        assert response.status_code == 200
        assert b'Items List' in response.data   # Vérifie que le titre s'affiche
