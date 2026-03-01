# Quick DB check script: prints usernames from the configured PostgreSQL database.
# Run from the project root: python3 check_db.py

from loginapp import app
from loginapp import db

if __name__ == '__main__':
    with app.app_context():
        try:
            with db.get_cursor() as cur:
                cur.execute("SELECT username FROM users;")
                rows = cur.fetchall()
                if not rows:
                    print('No users found in the `users` table.')
                else:
                    print('Users in DB:')
                    for r in rows:
                        # psycopg2 RealDictCursor returns dicts
                        print('-', r.get('username'))
        except Exception as e:
            print('Error connecting to database or executing query:')
            print(e)
