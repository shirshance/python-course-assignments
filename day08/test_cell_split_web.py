from fastapi.testclient import TestClient
from cell_split_web import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Cell Splitting Calculator" in response.text


def test_calculate_page():
    response = client.post(
        "/calculate",
        data={
            "total_volume": "10",
            "split_ratio": "10"
        }
    )

    assert response.status_code == 200
    assert "Take 1.00 mL of cells" in response.text
    assert "Add 9.00 mL of fresh medium" in response.text


def test_invalid_split_ratio():
    response = client.post(
        "/calculate",
        data={
            "total_volume": "10",
            "split_ratio": "1"
        }
    )

    assert response.status_code == 200
    assert "Split ratio must be greater than 1" in response.text
