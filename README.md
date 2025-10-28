## Key libraries and frameworks

1. [`Python`](https://www.python.org/downloads/).
2. [`Django`](https://www.djangoproject.com/) -> ORM, Django admin, Fast and secure.
3. [`DRF`](https://www.django-rest-framework.org/) -> powerful for building web APIs.
4. [`drf_spectacular`](https://drf-spectacular.readthedocs.io/en/latest/) - API documentation -> Generates cleaner, more standards-compliant (OpenAPI 3.0+) schema.
5. `PostgreSQL` - Database.
6. [`rest_framework_simplejwt`](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) - authentication -> stateless, easy for mobile/web clients.
7. [`uv`](https://pypi.org/project/uv/) - package manager -> fast, dependency resolution.
   - Install `uv` with [`homebrew`](https://formulae.brew.sh/formula/uv) (recommended).
   - or simply use pip for installing dependencies

## Design Choice
The project is organized into three separate apps to improve modularity and maintainability:

1. User Account: Manages solar panel installers and system users.

2. Customer: Handles creation and management of customer data.

3. Loan Offer: Manages loan offers, associated details, and installment plans.

## Running the application
1. Create and activate virtual environment.
   ```sh
       python -m venv venv
       uv venv venv
       source venv/bin/activate
   ```
2. Install dependencies using `uv`.
   ```sh
       uv pip compile requirements.in -o requirements.txt (optional)
       uv pip install -r requirements.in
       pip install -r requirements.txt
   ```
3. Create a postgreSQL database and add required environment variables to `.env` file in root dir for the database.
    ```sh
       DB_USER=<db_user>
       DB_HOST=<db_host>
       DB_NAME=<db_name>
       DB_PORT=<db_port>
    ``` 
4. Run migrations & start server use:
   ```sh
       python manage.py makemigrations (optional)
       python manage.py migrate
       python manage.py runserver  
   ```
5. Create a superuser if required:
   ```sh
       python manage.py createsuperuser
   ```
6. You can test the APIs using http://localhost:8000/swagger and Django admin panel using http://localhost:8000/admin if you have created a superuser using the command in step 4.

7. Run tests using:
   ```sh
       python manage.py test  
   ```

### future-proof considerations
AS this take home task has time constraints, everything that would normally be presented in a production-ready environment has not been implemented.
below are something worth considering in a production ready setup.

#### Containerization
Using Docker and docker compose for containerize and isolate the application and all its dependencies to ensure it runs the same way across different environments.

#### Social authentication
for users (solar panel installers) to be able to use their social account for registeration and login. (django-allauth - handles registration, social, email verification)

#### Linter
Using linters (for example ruff) for code formatting.

#### Soft delete
With the given scenario, having soft delete is more beneficial than hard deleting the entities.

#### Notification
System should be able to notify customers of their loans by any tools necessary.(like sending them email before their next bill due date)

#### Paginination and Filtering
It is better to add filtering and pagination to the list endpoints.

#### Data encryption
Encryption for sensitive fields as needed