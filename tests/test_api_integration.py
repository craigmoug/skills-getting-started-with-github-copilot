"""Integration tests for the Activities API using AAA (Arrange-Act-Assert) pattern"""
import pytest


# ============ GET /activities ============

def test_get_activities_returns_all_activities(client, reset_activities):
    """Test retrieving all activities"""
    # Arrange
    expected_activities = ["Chess Club", "Programming Class", "Gym Class"]
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    
    # Assert
    assert response.status_code == 200
    assert isinstance(activities, dict)
    for activity in expected_activities:
        assert activity in activities


def test_get_activities_includes_participant_details(client, reset_activities):
    """Test that activities include participant information"""
    # Arrange
    activity_name = "Chess Club"
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    chess_club = activities[activity_name]
    
    # Assert
    assert response.status_code == 200
    assert "participants" in chess_club
    assert "michael@mergington.edu" in chess_club["participants"]
    assert "max_participants" in chess_club


# ============ GET / (Root redirect) ============

def test_root_redirects_to_static_index(client):
    """Test that root path redirects to static index.html"""
    # Arrange
    # (no setup needed)
    
    # Act
    response = client.get("/", follow_redirects=True)
    
    # Assert
    assert response.status_code == 200


# ============ POST /activities/{activity_name}/signup ============

def test_signup_new_participant_success(client, reset_activities):
    """Test successful signup of a new participant"""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    activities = client.get("/activities").json()
    
    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    assert email in activities[activity_name]["participants"]


def test_signup_duplicate_participant_fails(client, reset_activities):
    """Test that duplicate signup is rejected"""
    # Arrange
    activity_name = "Chess Club"
    email = "duplicate@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_nonexistent_activity_fails(client):
    """Test that signup for non-existent activity fails"""
    # Arrange
    activity_name = "NonExistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


# ============ DELETE /activities/{activity_name}/remove ============

def test_remove_participant_success(client, reset_activities):
    """Test successful removal of a participant"""
    # Arrange
    activity_name = "Chess Club"
    email = "removable@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Act
    response = client.delete(f"/activities/{activity_name}/remove?email={email}")
    activities = client.get("/activities").json()
    
    # Assert
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]
    assert email not in activities[activity_name]["participants"]


def test_remove_nonexistent_participant_fails(client, reset_activities):
    """Test that removing a non-existent participant fails"""
    # Arrange
    activity_name = "Chess Club"
    email = "nonexistent@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity_name}/remove?email={email}")
    
    # Assert
    assert response.status_code == 404
    assert "Participant not found" in response.json()["detail"]


def test_remove_from_nonexistent_activity_fails(client):
    """Test that removing from non-existent activity fails"""
    # Arrange
    activity_name = "NonExistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity_name}/remove?email={email}")
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


# ============ Integration flow tests ============

def test_full_signup_and_removal_flow(client, reset_activities):
    """Test complete flow: signup then removal"""
    # Arrange
    activity_name = "Programming Class"
    email = "flow@mergington.edu"
    
    # Act - Signup
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    activities = client.get("/activities").json()
    
    # Assert - Signup
    assert signup_response.status_code == 200
    assert email in activities[activity_name]["participants"]
    
    # Act - Removal
    remove_response = client.delete(f"/activities/{activity_name}/remove?email={email}")
    activities = client.get("/activities").json()
    
    # Assert - Removal
    assert remove_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
