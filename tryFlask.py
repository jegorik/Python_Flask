from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = 'your_secret_key'  # Needed for flash messages
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

def commit_session():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'error')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('content', '').strip()
        if not task_content:
            flash('Task content cannot be empty!', 'error')
            return redirect('/')
        
        new_task = Todo(content=task_content)
        db.session.add(new_task)
        commit_session()
        flash('Task added successfully!', 'success')
        return redirect('/')
    
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    db.session.delete(task_to_delete)
    commit_session()
    flash('Task deleted successfully!', 'success')
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_content = request.form.get('content', '').strip()
        if not task_content:
            flash('Task content cannot be empty!', 'error')
            return redirect(url_for('update', id=id))
        
        task_to_update.content = task_content
        commit_session()
        flash('Task updated successfully!', 'success')
        return redirect('/')
    
    return render_template('update.html', task=task_to_update)

if __name__ == "__main__":
    app.run(debug=True)