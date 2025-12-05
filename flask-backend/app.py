from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'lxf020302',  # Replace with your MySQL password
    'database': 'interview_task'  # Replace with your database name
}

# Establish database connection
try:
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor(dictionary=True)
    print("Connected to the database successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask Backend!"})

# Fetch all events
@app.route('/events', methods=['GET'])
def get_events():
    try:
        cursor.execute("SELECT * FROM events;")
        events = cursor.fetchall()
        return jsonify(events)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# Add a new event
@app.route('/add-event', methods=['POST'])
def add_event():
    data = request.json
    name = data.get('name')
    date = data.get('date')
    description = data.get('description')

    try:
        cursor.execute(
            "INSERT INTO events (name, date, description) VALUES (%s, %s, %s)",
            (name, date, description)
        )
        db.commit()
        return jsonify({"message": "Event added successfully!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# Delete an event
@app.route('/delete-event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
        db.commit()
        return jsonify({"message": "Event deleted successfully!"})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)