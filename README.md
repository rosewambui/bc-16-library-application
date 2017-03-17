### bc-16-library-application

  A library web application using flask framework.

### Getting started:

- Install requirements:

      $  pip install -r requirements.txt

- Init Sqlite DB

      $ rm db.db # delete any existing db
      $ python init_db.py

- Register an admin user

      $ python make_admin.py username password

- Run App

      $ python library.py
