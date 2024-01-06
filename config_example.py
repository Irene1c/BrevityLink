"""Configuration"""
import os


class ConfigClass:
    # A secret key for cryptographic functions.
    # Replace 'your_secret_key' with a secure key.
    SECRET_KEY = 'your_secret_key'

    # BASE_DIR is the absolute path to the
    # directory containing this configuration file.
    # It is commonly used to construct other
    # absolute paths within the application.
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Example for SQLite database:
    # If using SQLite, the URI should be in the format:
    # 'sqlite:///' + absolute_path_to_database_file
    # Here, we're joining the base directory,
    # 'server' folder, and the database filename.
    # Adjust the path based on your project structure.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
            BASE_DIR, 'server', 'database.db')

    # For other databases, replace the URI accordingly.
    # Example for PostgreSQL: 'postgresql://user:password@localhost/dbname'
    # Example for MySQL: 'mysql://user:password@localhost/dbname'

    # Disable Flask-SQLAlchemy modification tracking for better performance.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
