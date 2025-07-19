# Flask Todo Application

A simple yet functional Todo task management application built with Flask and SQLAlchemy. This project demonstrates fundamental Flask concepts including routing, templating, database integration, and CRUD operations.

## 🚀 Features

- **Task Management**: Create, read, update, and delete todo tasks
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **Responsive UI**: Bootstrap-powered responsive design
- **Flash Messages**: User feedback for successful operations and errors
- **Timestamp Tracking**: Automatic timestamp recording for task creation
- **Form Validation**: Client and server-side validation for task content

## 📋 Requirements

- Python 3.7 or higher
- Flask 2.0.3
- Flask-SQLAlchemy 2.5.1
- SQLite (included with Python)

## 🛠️ Installation

1. Clone or navigate to the project directory:

```bash
cd Python_Flask
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the Flask application:

```bash
python tryFlask.py
```

2. Open your web browser and navigate to:

```text
http://localhost:5000
```

3. Start managing your tasks:

   - **Add Task**: Enter task description and click "Add Task"
   - **Update Task**: Click "Update" next to any existing task
   - **Delete Task**: Click "Delete" to remove a task
   - **View Tasks**: All tasks are displayed in a table format

## 📊 Project Structure

```text
Python_Flask/
├── tryFlask.py             # Main Flask application
├── requirements.txt        # Python dependencies
├── test.db                 # SQLite database file
├── templates/              # HTML templates
│   ├── base.html          # Base template with common layout
│   ├── index.html         # Main todo list page
│   └── update.html        # Task update form
├── static/                 # Static files (CSS, JS, images)
│   └── css/               # Custom stylesheets
└── flask/                 # Flask framework files
```

## 🗄️ Database Schema

The application uses a simple SQLite database with one table:

### Todo Model

- **id**: Primary key (Integer, Auto-increment)
- **content**: Task description (String, max 200 characters, required)
- **date_created**: Creation timestamp (DateTime, auto-generated)

## 🎯 Key Features Explained

### CRUD Operations

- **Create**: Add new tasks via POST request to home route
- **Read**: Display all tasks on the main page
- **Update**: Modify existing tasks through dedicated update route
- **Delete**: Remove tasks via dedicated delete route

### Error Handling

- Database transaction management with rollback capability
- Flash message system for user feedback
- Form validation for empty task content
- 404 error handling for non-existent tasks

### UI/UX Features

- Bootstrap integration for responsive design
- Flash message system for operation feedback
- Clean table layout for task display
- Intuitive action buttons for task management

## 🔧 Technical Implementation

### Flask Routes

- `GET/POST /`: Home page with task list and creation form
- `GET /delete/<id>`: Delete task by ID
- `GET/POST /update/<id>`: Update task form and processing

### Database Configuration

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
```

### Template Engine

- Jinja2 templating with template inheritance
- Bootstrap CSS framework integration
- Dynamic content rendering with Flask context

## 🧪 Testing

To test the application:

1. Start the Flask development server
2. Test CRUD operations through the web interface:
   - Create several tasks
   - Update existing tasks
   - Delete tasks
   - Verify data persistence across sessions

## 📈 Example Usage

### Adding a Task

1. Navigate to the home page
2. Enter task description in the input field
3. Click "Add Task" button
4. Task appears in the task list with timestamp

### Updating a Task

1. Click "Update" button next to desired task
2. Modify the task content in the form
3. Click "Update Task" to save changes
4. Redirected to home page with updated task

### Deleting a Task

1. Click "Delete" button next to desired task
2. Task is immediately removed from the list
3. Success message confirms deletion

## 🔄 Development Notes

### Database Initialization

The database is automatically created when the application first runs. The SQLite file `test.db` will be generated in the project root directory.

### Debug Mode

The application runs in debug mode by default, providing:

- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

### Session Management

- Secret key configured for session security
- Flash messages stored in session
- Database session management with proper commit/rollback

## 🚀 Possible Enhancements

- **User Authentication**: Add user registration and login
- **Task Categories**: Organize tasks by categories or tags
- **Due Dates**: Add deadline functionality with notifications
- **Task Priority**: Implement priority levels for tasks
- **Search Functionality**: Add task search and filtering
- **REST API**: Create API endpoints for mobile app integration
- **Task Completion**: Add status tracking (completed/pending)
- **Export Features**: Export tasks to CSV or PDF

## 🔒 Security Considerations

- Secret key should be moved to environment variables in production
- Input validation implemented for task content
- SQL injection protection through SQLAlchemy ORM
- Session management for flash messages

## 📚 Learning Objectives

This project demonstrates:

- Flask application structure and organization
- SQLAlchemy ORM for database operations
- Template inheritance and rendering
- Form handling and validation
- Error handling and user feedback
- RESTful route design
- Database modeling and relationships

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

---

**A practical Flask application demonstrating web development fundamentals with Python**
