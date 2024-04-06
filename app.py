from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

@app.route('/')
def index():
    workouts = Workout.query.all()
    return render_template('index.html', workouts=workouts)

@app.route('/add_workout', methods=['POST'])
def add_workout():
    exercise = request.form['exercise']
    duration = int(request.form['duration'])
    calories_burned = calculate_calories_burned(exercise, duration)
    workout = Workout(exercise=exercise, duration=duration, calories_burned=calories_burned)
    db.session.add(workout)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_workout/<int:workout_id>', methods=['POST'])
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/chart_data')
def chart_data():
    workouts = Workout.query.all()
    labels = [workout.date.strftime('%Y-%m-%d') if workout.date else 'No Date' for workout in workouts]
    data = [workout.duration for workout in workouts]
    return render_template('chart_data.html', labels=labels, data=data)

@app.route('/workout_history')
def workout_history():
    workouts = Workout.query.all() 
    return render_template('workout_history.html', workouts=workouts)

def calculate_calories_burned(exercise, duration):
    if exercise == 'running':
        return duration * 10
    elif exercise == 'cycling':
        return duration * 8
    else:
        return duration * 5

if __name__ == '__main__':
    app.run(debug=True)
