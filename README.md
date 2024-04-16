# Project Title

![Project Logo/Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinnaxis.com%2F%3Fk%3Dexpense-manager-app-how-to-use-it-small-business-ee-PPwj1Qty&psig=AOvVaw3HueNtTApI3ej2i4rl5ycq&ust=1713377240355000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOihwuOpx4UDFQAAAAAdAAAAABAJ)

A Django REST Framework backend for managing job earnings and expenses, with user registration and login functionality.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

This project provides a backend solution for managing earnings from different job categories and types. Users can register and log in to the system to track their earnings and expenses. Future plans include adding expense management features for items such as fuel, parking, food, and tools. The frontend will display charts to visualize earnings and expenses over time.

## Features

- User registration and login
- Management of job earnings based on category and type
- Planned: Expense tracking for fuel, parking, food, tools, etc.
- Planned: Visualization of earnings and expenses through charts

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lucasfpac/jobsAPI
    ```

2. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    - Rename the `.env.example` file to `.env`.
    - Add necessary environment variables like database credentials, secret key, etc.

4. Run database migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Register a new user using the `/api/register/` endpoint.
2. Log in with the registered user using the `/api/login/` endpoint to obtain an authentication token.
3. Use the provided API endpoints to manage job earnings and expenses.
4. For frontend integration, use the provided API documentation or generate API clients.

## API Documentation

[Link to API documentation (if available)]

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) before submitting pull requests or reporting issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please contact [lucasfortunato1@gmail.com](mailto:lucasfortunato1@gmail.com).
