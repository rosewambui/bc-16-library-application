import sys
from sqlalchemy.exc import IntegrityError
from app.models import User, db

if len(sys.argv) != 3:
    print('python make_admin.py username password')
    exit()

username = sys.argv[1]
password = sys.argv[2]

user = User(username, password, True)

try:
    db.session.add(user)
    db.session.commit()
except IntegrityError, e:
    print(e)
