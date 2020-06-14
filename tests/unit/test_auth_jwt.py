from unittest.mock import patch
from jwt import encode, decode
from app.api.auth import authenticate

FAKE_EMAIL = 'test@example.org'
FAKE_AUTH_HEADER = "Bearer " + encode({'email': 'test@example.org'}, open(".dev/dev-jwt-key").read(), algorithm='RS256').decode('utf-8')
# FAKE_BAD_AUTH = "Bearer " + encode({'email': 'test@example.org'}, "bogus-key", algorithm='RS256').decode('utf-8')

def test_authenticate_failure(module_client, function_empty_db):
    # Arrange
    def callback(*args, **kwargs):
        return 1

    # Act
    wrapper = authenticate(callback)
    with patch('app.api.auth.request') as fake_request:
        fake_request.headers = {
            'authorization': 'bogus'
        }
        result = wrapper()

    # Assert
    assert result[1] == 401


# def test_invalid_signature_failure(module_client, function_empty_db):
#     # Arrange
#     def callback(*args, **kwargs):
#         return 1

#     # Act
#     wrapper = authenticate(callback)
#     with patch('app.api.auth.request') as fake_request:
#         fake_request.headers = {
#             'authorization': FAKE_BAD_AUTH
#         }
#         result = wrapper()

#     # Assert
#     assert result[1] == 401


def test_authenticate_success(module_client, function_empty_db):
    # Arrange
    def callback(*args, **kwargs):
        return 1

    # Act
    wrapper = authenticate(callback)
    with patch('app.api.auth.request') as fake_request:
        fake_request.headers = {
            'authorization': FAKE_AUTH_HEADER
        }
        result = wrapper()

    # Assert
    assert result == 1
