from app import create_app
from app.extensions import db
from app.models import User

# Create app and push context
app = create_app()
app.app_context().push()

# Fetch all users
users = User.query.all()

if not users:
    print("No users yet!")
else:
    print("Users in database:")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
