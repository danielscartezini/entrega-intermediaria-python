import pytest
from unittest.mock import patch, Mock
import requests # Adicionado: Importar o módulo requests
from main import fetch_posts

def test_fetch_posts_success():
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"},
            {"userId": 1, "id": 2, "title": "qui est esse", "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"}
        ]
        mock_get.return_value = mock_response

        posts = fetch_posts()
        assert posts is not None
        assert len(posts) == 2
        assert posts[0]["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

def test_fetch_posts_error():
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Test connection error")

        posts = fetch_posts()
        assert posts is None
