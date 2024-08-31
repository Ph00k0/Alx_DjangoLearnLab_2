test

## Custom Permissions and Groups

This project defines the following custom permissions for the `CustomUser` model:
- `can_view`: Allows users to view instances.
- `can_create`: Allows users to create instances.
- `can_edit`: Allows users to edit instances.
- `can_delete`: Allows users to delete instances.

Groups and their assigned permissions:
- **Editors**: can create and edit instances.
- **Viewers**: can view instances.
- **Admins**: can view, create, edit, and delete instances.


# Authentication and Permissions Guide

## Authentication
To obtain a token, send a POST request to `/api-token-auth/` with your username and password. Use the returned token in the `Authorization` header for authenticated requests.

Example:
```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'
