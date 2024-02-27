# Django Login App.

## Introduction.
This Django app offers customers a simple login feature. Users may create an account, log in, and then log out. It also handles errors for duplicate usernames and email addresses during sign-up and guarantees that only authenticated users may access certain sites.

## Features.
- User signup: Users may establish a new account by entering a unique username, first and last name, email address, and password.
- User login: Registered users can sign in with their username and password.
- User logout: Users can safely log out of their accounts.
- Error handling: The software manages issues such as duplicate usernames and emails. 


## Installation
1. Clone the repository to your local machine:

```
git clone <repository-url>
```

2. Navigate to the project directory:

```
cd django-login-app
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Apply migrations to set up the database:

```
python manage.py migrate
```

5. Run the development server:

```
python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage
1. Sign Up: Navigate to the signup page (`/signup`) and fill out the registration form with your details.
2. Sign In: After signing up, you can log in to your account using the login page (`/signin`).
3. Access Protected Pages: Certain pages may require authentication. After logging in, you can access these protected pages.
4. Sign Out: To log out of your account, click on the "Sign Out" button.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README file with additional information specific to your Django login app.
