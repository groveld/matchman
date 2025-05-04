"""Test health check."""

# Import necessary modules
from matchman import create_app

# Setup the Flask application for testing
app = create_app()


def test_health_check():
    """Test health check."""
    # Use the test client to send a request to the application
    with app.test_client() as client:
        response = client.get("/health")

        # Assert the status code and response content
        assert response.status_code == 200
        assert "Service is up and running" in response.data.decode()
