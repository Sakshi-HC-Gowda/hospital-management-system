import os
from datetime import datetime

from app import create_app
from app.extensions import db
from app.models import User


def create_admin_user():
    app = create_app()

    username = os.environ.get("ADMIN_USERNAME", "admin")
    email = os.environ.get("ADMIN_EMAIL", "admin@hospital.com")
    password = os.environ.get("ADMIN_PASSWORD", "admin123")

    with app.app_context():
        admin = User.query.filter_by(username=username).first()

        if admin is None:
            admin = User(
                username=username,
                email=email,
                first_name="Admin",
                last_name="User",
                role="admin",
                is_active=True,
                date_created=datetime.utcnow(),
            )
            db.session.add(admin)
        else:
            admin.email = email
            admin.role = "admin"
            admin.is_active = True

        admin.set_password(password)
        db.session.commit()

    print("Admin user is ready.")
    print(f"Username: {username}")
    print(f"Password: {password}")


if __name__ == "__main__":
    create_admin_user()
