from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI and secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

class Todo(db.Model):
    """Model representing a Todo task."""
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each task
    content = db.Column(db.String(200), nullable=False)  # Content of the task
    date_created = db.Column(db.DateTime, default=datetime.now())  # Timestamp of task creation

    def __repr__(self):
        """Return a string representation of the Todo object."""
        return f'<Task {self.id}>'

def commit_session():
    """Commit the current database session and handle exceptions."""
    try:
        db.session.commit()  # Commit the session
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        flash(f'An error occurred: {str(e)}', 'error')  # Flash an error message

@app.route("/", methods=['GET', 'POST'])
def index():
    """Render the index page and handle task creation."""
    if request.method == 'POST':
        task_content = request.form.get('content', '').strip()  # Get task content from form
        if not task_content:
            flash('Task content cannot be empty!', 'error')  # Flash error if content is empty
            return redirect('/')
        
        new_task = Todo(content=task_content)  # Create a new Todo object
        db.session.add(new_task)  # Add the new task to the session
        commit_session()  # Commit the session
        flash('Task added successfully!', 'success')  # Flash success message
        return redirect('/')
    
    tasks = Todo.query.order_by(Todo.date_created).all()  # Retrieve all tasks ordered by creation date
    return render_template('index.html', tasks=tasks)  # Render the index template with tasks

@app.route('/delete/<int:id>')
def delete(id):
    """Delete a task by its ID."""
    task_to_delete = Todo.query.get_or_404(id)  # Get the task or return a 404 error
    db.session.delete(task_to_delete)  # Delete the task from the session
    commit_session()  # Commit the session
    flash('Task deleted successfully!', 'success')  # Flash success message
    return redirect('/')  # Redirect to the index page

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    """Update a task by its ID."""
    task_to_update = Todo.query.get_or_404(id)  # Get the task or return a 404 error
    if request.method == 'POST':
        task_content = request.form.get('content', '').strip()  # Get updated task content from form
        if not task_content:
            flash('Task content cannot be empty!', 'error')  # Flash error if content is empty
            return redirect(url_for('update', id=id))  # Redirect back to the update page
        
        task_to_update.content = task_content  # Update the task content
        commit_session()  # Commit the session
        flash('Task updated successfully!', 'success')  # Flash success message
        return redirect('/')  # Redirect to the index page
    
    return render_template('update.html', task=task_to_update)  # Render the update template with the task

if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode