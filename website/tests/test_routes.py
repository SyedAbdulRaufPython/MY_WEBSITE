Created website/tests/test_routes.py with comprehensive test coverage for all Flask routes including:
- Home, about, chat, login, pricing, success, and cancel pages
- GET and POST request handling for chat and ask-ai endpoints
- Invalid route handling (404 errors)
- Pytest fixtures for test client setup

The test suite uses pytest and Flask's test client to verify all application routes are accessible and return appropriate status codes.