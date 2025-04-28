
# PersonalFinanceApp

A full-stack personal finance management application built with **Django**, **Django REST Framework**, and **React**, containerized using **Docker**.  
Easily track your expenses, categorize transactions, and manage your finances through a modern web interface.

---

## ✨ Features

- User authentication and registration (`dj-rest-auth`, `djoser`)
- Secure token-based authentication
- Create, update, and delete financial transactions
- Categorize expenses
- View transaction history
- Fully containerized with Docker
- Responsive React frontend
- RESTful API backend built with Django

---

## 🛠️ Tech Stack

**Backend**
- Django
- Django REST Framework
- PostgreSQL (via `psycopg2-binary`)
- django-extensions
- django-cors-headers
- dj-rest-auth
- djoser

**Frontend**
- React
- Axios
- React Router

**DevOps**
- Docker
- Docker Compose

---

## ⚙️ Local Installation

### Backend Setup (Django)

1. **Clone the repository**
   ```bash
   git clone https://github.com/inanh360/PersonalFinanceApp.git
   cd PersonalFinanceApp/backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install backend dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the `backend/` directory:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://your_user:your_password@localhost:5432/your_database
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Django server**
   ```bash
   python manage.py runserver
   ```

### Frontend Setup (React)

1. **Navigate to the frontend folder**
   ```bash
   cd ../frontend
   ```

2. **Install frontend dependencies**
   ```bash
   npm install
   ```

3. **Start the React development server**
   ```bash
   npm start
   ```

Frontend will run at [http://localhost:3000](http://localhost:3000).

---

## 🐳 Running with Docker

> You can spin up the full stack (backend, frontend, and database) easily using Docker Compose.

1. **Clone the repository**
   ```bash
   git clone https://github.com/inanh360/PersonalFinanceApp.git
   cd PersonalFinanceApp
   ```

2. **Build and start the containers**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Backend API: [http://localhost:8000](http://localhost:8000)
   - Frontend App: [http://localhost:3000](http://localhost:3000)

4. **Stop the containers**
   ```bash
   docker-compose down
   ```

---

## 📋 API Overview

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/registration/` | User registration |
| GET | `/api/transactions/` | List all transactions |
| POST | `/api/transactions/` | Create a transaction |
| PUT | `/api/transactions/{id}/` | Update a transaction |
| DELETE | `/api/transactions/{id}/` | Delete a transaction |

Authentication uses token-based methods provided by `dj-rest-auth` and `djoser`.

---

## 🔥 Project Structure

```
PersonalFinanceApp/
├── backend/
│   ├── manage.py
│   ├── backend/          # Django project settings
│   └── finance/          # Django app
├── frontend/
│   ├── public/
│   └── src/
├── docker-compose.yml
├── Dockerfile (backend and/or frontend)
├── requirements.txt
├── README.md
```

---

## 🚀 Future Enhancements

- Filter and search transactions
- Financial reporting dashboard
- Export transactions (CSV, Excel)
- Budget setting and alerts
- Dark mode for frontend
- Production deployment (Render, AWS, Vercel)
