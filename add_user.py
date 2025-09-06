from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():
    user = User(username="admin", email="admin@example.com")
    db.session.add(user)
    db.session.commit()
    print("User added!")
