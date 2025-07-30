from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
students = []

@app.route('/')
def home():
    return render_template("fontend.html")

@app.route('/add', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student added successfully"}), 200

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
