# 📝 FastNotes

FastNotes is a lightweight and efficient note-taking web application that allows users to quickly create, edit, and delete notes in an easy-to-use interface. It uses **FastAPI** as the backend framework and **MongoDB** for storing notes.

🚀 **Live Demo**: [Click here to try FastNotes](https://fastnotes-oih9.onrender.com)

---

## ✨ Features

- 🔹 **Add Notes** with title, description, and importance flag
- ✏️ **Edit Notes Inline** directly on the same page
- 🗑️ **Delete Notes** instantly
- ⭐ **Mark Notes as Important** with visual emphasis
- 📱 **Responsive Design** — works on all screen sizes
- ⚡ **FastAPI Backend** with clean and structured REST routes
- 🌐 **Deployed on Render**
- ☁️ **MongoDB Atlas Integration** for persistent storage
- 📁 **Modular Codebase** with separate folders for routes, models, and static files

---

## 🧠 Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Backend     | [FastAPI](https://fastapi.tiangolo.com/) |
| Database    | [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) |
| Frontend    | [HTML + CSS + JS](https://developer.mozilla.org/en-US/docs/Learn) |
| Styling     | [Bootstrap 5](https://getbootstrap.com/) |
| Templates   | [Jinja2](https://jinja.palletsprojects.com/) |
| Deployment  | [Render](https://render.com/) |

---

## 📂 Project Structure

```
FastNotes/
│
├── venv/                     # Virtual environment
├── main.py                   # Main FastAPI app
├── routes/                   # Routes for note operations (add, update, delete)
│   └── note.py
├── templates/                # HTML templates
│   └── index.html            # Main HTML page rendered via Jinja2
├── static/                   # Static files (CSS, JS)
│   └── style.css             # Custom styles and Bootstrap customizations
│   └── script.js             # JavaScript for handling inline editing
├── models/                   # MongoDB models
│   └── note.py
├── schemas/                  # Pydantic schemas for validation
│   └── note.py
├── config/                   # Configuration files
│   └── db.py                 # Database connection configuration
└── requirements.txt          # List of dependencies
```

---

## 📦 Installation

### Prerequisites

Make sure you have **Python 3.7+** installed on your system.

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FastNotes.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FastNotes
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the project root and add your MongoDB connection URI:

   ```
   MONGO_URI=mongodb+srv://<your-db-username>:<your-db-password>@cluster0.mongodb.net/FastNotes?retryWrites=true&w=majority
   ```

7. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

8. Open your browser and navigate to:

   ```
   http://127.0.0.1:8000
   ```

   ---

## 🌐 Deployment

This application is deployed on **Render** and can be accessed live at:

```
https://fastnotes-oih9.onrender.com
```

---

## 💬 Feedback & Contributions

Found a bug? Want to suggest a feature? Open an issue or submit a pull request!

---
