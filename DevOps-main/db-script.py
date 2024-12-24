from app import db
from models import User, Role

admin_role = Role(role_name='Admin', description='Administrator role')
moder_role = Role(role_name='Moderator', description='Moderator role')
db.session.add_all([admin_role, moder_role])
db.session.commit()

admin_user = User(
    login='admin',
    password_hash='hashed_password', # User.set_password()
    last_name='Admin',
    first_name='User',
    middle_name='Test',
    form='Дневная',
    date=2024,
    group='A',
    role_id=admin_role.id
)
admin_user.set_password('Apass')
db.session.add(admin_user)
db.session.commit()
