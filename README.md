# Sweet Shop Kata

A full-stack web application for managing a sweet shop inventory, built with FastAPI (backend) and React (frontend). This project demonstrates CRUD operations, user authentication, and role-based access control.

## Features

- **User Authentication**: Register and login with JWT-based authentication
- **Role-Based Access**: Admin and regular user roles with different permissions
- **Sweet Inventory Management**: View, search, add, update, and delete sweets
- **Responsive UI**: Modern React frontend with Tailwind CSS
- **API Documentation**: Automatic API docs via FastAPI

## Tech Stack

### Backend

- **FastAPI**: High-performance web framework for building APIs
- **SQLAlchemy**: ORM for database interactions
- **SQLite**: Database for development
- **JWT**: Token-based authentication
- **CORS**: Cross-origin resource sharing support

### Frontend

- **React**: JavaScript library for building user interfaces
- **Vite**: Fast build tool and development server
- **Axios**: HTTP client for API requests
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework

## Project Structure

```
sweet-shop-kata/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── auth.py          # Authentication utilities
│   ├── database.py      # Database configuration
│   ├── requirements.txt # Python dependencies
│   └── test_main.py     # Tests
├── frontend/
│   ├── src/
│   │   ├── api.js       # API client configuration
│   │   ├── App.jsx      # Main React component
│   │   ├── components/  # Reusable components
│   │   ├── pages/       # Page components
│   │   └── ...
│   ├── .env             # Environment variables
│   ├── package.json     # Node dependencies
│   └── ...
└── README.md
```

## Setup Instructions

### Prerequisites

- **Python 3.8+**: For the backend
- **Node.js 16+**: For the frontend
- **Git**: For cloning the repository

### Backend Setup

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**:

   ```bash
   python main.py
   ```

   The backend will start on `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

### Frontend Setup

1. **Navigate to the frontend directory**:

   ```bash
   cd frontend
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Configure environment variables**:
   Create a `.env` file in the `frontend` directory with the following content:

   ```
   VITE_API_URL=http://localhost:8000
   ```

4. **Run the development server**:

   ```bash
   npm run dev
   ```

   The frontend will start on `http://localhost:5173`.

## Usage

1. **Start both servers** (backend and frontend) as described above.

2. **Access the application**:

   - Frontend: Open `http://localhost:5173` in your browser
   - Backend API: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

3. **Register a new user** or use existing credentials to log in.

4. **Explore the features**:
   - View sweets inventory
   - Search and filter sweets
   - Add to cart (if implemented)
   - Admin panel for managing inventory (admin role required)

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token

### Sweets Management

- `GET /api/sweets` - Get all sweets (authenticated)
- `GET /api/sweets/search` - Search sweets with filters (authenticated)
- `POST /api/sweets` - Create a new sweet (admin only)
- `PUT /api/sweets/{sweet_id}` - Update a sweet (admin only)
- `DELETE /api/sweets/{sweet_id}` - Delete a sweet (admin only)

## Development

### Running Tests

```bash
cd backend
python -m pytest test_main.py
```

### Building for Production

```bash
# Frontend
cd frontend
npm run build

# Backend (using uvicorn for production)
pip install uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Troubleshooting

### Common Issues

1. **Frontend can't connect to backend**:

   - Ensure the backend is running on `http://localhost:8000`
   - Check that `VITE_API_URL` in `frontend/.env` is set correctly
   - Verify CORS settings in the backend

2. **Database issues**:

   - The SQLite database (`sweetshop.db`) is created automatically on startup
   - If you encounter issues, delete the database file and restart the backend

3. **Authentication problems**:
   - Ensure you're sending the JWT token in the Authorization header
   - Check token expiration (tokens are valid for a limited time)

### Environment Variables

- **Backend**:

  - `FRONTEND_URL`: Frontend URL for CORS (defaults to `http://localhost:5173`)

- **Frontend**:
  - `VITE_API_URL`: Backend API URL (defaults to `http://localhost:8000`)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
