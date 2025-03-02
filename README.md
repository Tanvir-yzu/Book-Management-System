# Book Management System

This is a Django-based Book Management System that allows users to manage a collection of books. The system includes features such as adding, editing, viewing, and deleting books. It also integrates Tailwind CSS for styling.

## Features

- Add new books with details such as title, author, ISBN, publication date, genre, description, cover image, rating, and status.
- Edit existing book details.
- View detailed information about each book.
- Delete books from the collection.
- Search for books by title, author, ISBN, or genre.
- Responsive design using Tailwind CSS.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd bookmanager
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install Node.js dependencies for Tailwind CSS:
    ```sh
    cd themes/static_src
    npm install
    cd ../../
    ```

5. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser for accessing the Django admin panel:
    ```sh
    python manage.py createsuperuser
    ```

## Usage

1. Start the Tailwind CSS build process:
    ```sh
    python manage.py tailwind start
    ```

2. Run the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your web browser and go to `http://127.0.0.1:8000/` to access the Book Management System.

4. Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage books and other data.

## License

This project is licensed under the MIT License.