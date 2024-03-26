# BrevityLink - URL Shortener

BrevityLink is a simple Flask-based URL shortener that allows you to generate short and easy-to-share links.

## Features

- **Generate Short Links:** Easily create short links from long URLs.
- **Interactive Table:** A user-friendly table displays long URLs, their corresponding shortened versions, the number of clicks, and provides an option to delete entries.
- **Redirect Functionality:** Seamless redirection of users from short links to their original long URLs.
- **User Authentication:**
  - **Logging In:** Users can securely log in to their accounts.
  - **Signing Up:** New users can create accounts to manage and track their short links.

## Technologies Used

- **HTML, CSS**: Frontend technologies used to create the user interface.
- **Bootstrap**: A frontend framework used for styling and layout.
- **Flask**: A lightweight web framework for Python used to build the backend server.
- **Flask-SQLAlchemy**: Simplifying database management in Flask.
- **Flask-Login**: Handling user authentication and sessions in Flask.
- **Flask-WTF**: Simplifying form handling and providing CSRF protection in Flask applications.

## Getting Started

### Prerequisites

* Python 3.x

### Installation and Project Setup

* Clone the repository:

```bash
  git clone https://github.com/Irene1c/BrevityLink.git
```

* Go to the project directory

```bash
  cd BrevityLink
```

* Create a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `source venv/Scripts/activate`
```

* Install dependencies:

```bash
  pip install -r requirements.txt
```

#### Configuration

* Create a Configuration File:

In the root directory of your project, create a new file named `config.py`.
You can use the provided template `config_example.py` as a starting point:

```bash
  cp config_example.py config.py
```

Open config.py using your preferred text editor.
Set the values of the configuration variables for your app.
At the very least, make sure to set your `SECRET_KEY`.

By configuring the config.py file, you customize your application settings to suit your needs. Ensure that all necessary variables are appropriately set for the smooth functioning of your app.

### Database Setup
The app uses Flask-SQLAlchemy with SQLite as the default database. The database file will be created automatically when you run the app.

### Running the App

```bash
  python app.py
```

## Usage
1. **Accessing the Web Interface:**
   - Navigate to [http://localhost:5000](http://localhost:5000) to access the web interface.

2. **User Authentication**
   - Create an account or log in to the web interface to manage your shortened URLs, view statistics, and perform other actions.

3. **Shortening URLs:**
    - Enter the long URL you want to shorten into the provided form.
    - Click on the `Shorten URL` button to generate a short link.

4. **Managing Shortened URLs:**
   - To delete a shortened URL, find the entry in the table and click the `Delete` button.

5. **Redirecting:**
    -To redirect, simply visit the shortened URL using the following format:
    ```
    http://localhost:5000/<short_url>
    ```

    Replace `<short_url>` with the actual short code generated by the URL shortener.

6. **Viewing Click Count:**
   - After being redirected, you will see the updated click count on the page.
   - Note: The click count is currently updated on page reload. If you want to see the most recent count, consider refreshing the page.


## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework that made building this app a breeze.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Simplifying database management in Flask.
- [Flask-Login](https://flask-login.readthedocs.io/) - Handling user authentication and sessions in Flask.
- [Flask-WTF](https://flask-wtf.readthedocs.io/) - Simplifying form handling and providing CSRF protection in Flask applications.
- [email-validator](https://pypi.org/project/email-validator/) - A library used for validating email addresses in the application.
- [Werkzeug](https://werkzeug.palletsprojects.com/) - Used for password hashing in the application.

## Contributing

Thank you for considering contributing to BrevityLink! Contributions are welcomed and encouraged.

### Contribution Guidelines

#### Prerequisites

- Python 3.x
#### Getting Started

1. Fork the repository and clone it locally.
3. Set up the development environment by following the instructions in [Getting Started](#getting-started) section of the README.
4. Create a new branch for your feature or bug fix.

#### Issues

Please check the existing issues before creating a new one to avoid duplication.

#### Branching Strategy

Follow the [Git flow](https://nvie.com/posts/a-successful-git-branching-model/) branching strategy. Create feature branches off the `develop` branch.

#### Code Style and Conventions

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.

#### Submitting Changes

1. Create a pull request against the `develop` branch.
2. Include a detailed description of your changes and any relevant information.

#### Review Process

All contributions will be reviewed, and feedback will be provided. Once approved, your changes will be merged.

#### Acknowledgment

Thank you for contributing to BrevityLink!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
