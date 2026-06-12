"""Unit tests for activity data model using AAA (Arrange-Act-Assert) pattern"""
import pytest
from src.app import activities


def test_activity_has_required_fields(reset_activities):
    """Test that each activity has all required fields"""
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}
    
    # Act & Assert
    for activity_name, activity_data in activities.items():
        for field in required_fields:
            assert field in activity_data, f"{activity_name} missing field: {field}"


def test_participants_is_list(reset_activities):
    """Test that participants field is always a list"""
    # Arrange
    # (setup in reset_activities fixture)
    
    # Act & Assert
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_data["participants"], list), \
            f"{activity_name} participants should be a list"


def test_max_participants_is_positive_integer(reset_activities):
    """Test that max_participants is a positive integer"""
    # Arrange
    # (setup in reset_activities fixture)
    
    # Act & Assert
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_data["max_participants"], int), \
            f"{activity_name} max_participants should be an integer"
        assert activity_data["max_participants"] > 0, \
            f"{activity_name} max_participants should be positive"


def test_no_duplicate_participants_in_activity(reset_activities):
    """Test that no activity has duplicate participants"""
    # Arrange
    # (setup in reset_activities fixture)
    
    # Act & Assert
    for activity_name, activity_data in activities.items():
        participants = activity_data["participants"]
        assert len(participants) == len(set(participants)), \
            f"{activity_name} has duplicate participants"


def test_description_is_string(reset_activities):
    """Test that description is a non-empty string"""
    # Arrange
    # (setup in reset_activities fixture)
    
    # Act & Assert
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_data["description"], str), \
            f"{activity_name} description should be a string"
        assert len(activity_data["description"]) > 0, \
            f"{activity_name} description should not be empty"


def test_schedule_is_string(reset_activities):
    """Test that schedule is a non-empty string"""
    # Arrange
    # (setup in reset_activities fixture)
    
    # Act & Assert
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_data["schedule"], str), \
            f"{activity_name} schedule should be a string"
        assert len(activity_data["schedule"]) > 0, \
            f"{activity_name} schedule should not be empty"
