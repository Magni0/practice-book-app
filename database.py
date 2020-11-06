from flask_sqlalchemy import SQLAlchemy
import os

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://app:{os.getenv('DB_PASSWORD')}@localhost:5432/library_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db

# import psycopg2
# import os


# connection = psycopg2.connect(
#     database="library_api",
#     user="app",
#     password=os.getenv("DB_PASSWORD"),
#     host="localhost"
# )

# cursor = connection.cursor()

# cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
# connection.commit()
