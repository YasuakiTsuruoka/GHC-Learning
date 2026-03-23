def test_root_endpoint(client):
    """Test the root endpoint of the FastAPI app."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Mergington High School API!"}