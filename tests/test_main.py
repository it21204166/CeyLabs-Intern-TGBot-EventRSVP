import pytest
import json
from src.utils.event_info import get_event_info
from src.utils.registration import register_user, get_user_by_email
from src.main import handle_responses

# Test for get_event_info function
def test_get_event_info():
    event_info = get_event_info()
    assert "Event Name: Parinamaya Live In Concert" in event_info
    

# Test for handle_responses function
def test_handle_responses():
    response1 = handle_responses("hello")
    assert "Hey there!" in response1
    assert "/start" in response1
    assert "/register" in response1
    assert "/help" in response1

    response2 = handle_responses("random message")
    assert "I do not understand what you wrote.." in response2

# Test for user registration
def test_register_user():
    # Test case 1: Register a new user
    user1 = register_user("John Doe", "john@example.com", 2)
    assert user1 is not None
    assert user1["name"] == "John Doe"
    assert user1["email"] == "john@example.com"
    assert user1["tickets"] == 2

    # Test case 2: Register an existing user
    existing_user = register_user("John Doe", "john@example.com", 2)
    assert existing_user is None

# Test for get_user_by_email function
def test_get_user_by_email():
    # Test case 1: User exists
    user1 = get_user_by_email("john@example.com")
    assert user1 is not None
    assert user1["name"] == "John Doe"
    assert user1["email"] == "john@example.com"

    # Test case 2: User does not exist
    non_existing_user = get_user_by_email("nonexistent@example.com")
    assert non_existing_user is None
