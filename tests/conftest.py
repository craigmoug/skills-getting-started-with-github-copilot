import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for API testing"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before and after each test"""
    # Store original state
    original = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Practice team play and compete in friendly basketball games",
            "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu", "nina@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Improve swimming techniques and train for swim meets",
            "schedule": "Tuesdays and Fridays, 3:00 PM - 4:30 PM",
            "max_participants": 18,
            "participants": ["sam@mergington.edu", "mia@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore painting, drawing, and mixed media art projects",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["lily@mergington.edu", "henry@mergington.edu"]
        },
        "Drama Society": {
            "description": "Develop acting skills and perform school theater productions",
            "schedule": "Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["maya@mergington.edu", "ethan@mergington.edu"]
        },
        "Debate Team": {
            "description": "Build public speaking skills and compete in debate competitions",
            "schedule": "Mondays, 5:00 PM - 6:30 PM",
            "max_participants": 16,
            "participants": ["zoe@mergington.edu", "jack@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Work on science challenges and prepare for academic competitions",
            "schedule": "Wednesdays and Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 22,
            "participants": ["noah@mergington.edu", "ava@mergington.edu"]
        }
    }
    
    # Reset before test
    activities.clear()
    activities.update(original)
    
    yield
    
    # Restore after test
    activities.clear()
    activities.update(original)
