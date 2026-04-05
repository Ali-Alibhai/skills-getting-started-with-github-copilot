from src.app import activities


def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants?email={email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    endpoint = "/activities/Unknown%20Club/participants?email=student@mergington.edu"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_non_registered_participant(client):
    # Arrange
    activity_name = "Art Studio"
    email = "not.registered@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants?email={email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"