## DIMAS FEBRIYANTO
## 50422430
## 1IA24
import requests
from flask import Flask, jsonify, redirect, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# Inisialisasi data mahasiswa
students = []

class Student(Resource):
    def get(self, student_id=None):
        if student_id is None:
            return jsonify(students)
        else:
            for student in students:
                if student['id'] == student_id:
                    return jsonify(student)
            return {'message': 'Mahasiswa dengan id {} tidak ditemukan'.format(student_id)}, 404

    def post(self):
        data = request.json
        data['total'] = calculate_total_score(data)
        data['grade'] = calculate_grade(data['total'])
        students.append(data)
        return jsonify(data)

    def put(self, student_id):
        data = request.json
        for student in students:
            if student['id'] == student_id:
                student['name'] = data.get('name', student['name'])
                student['npm'] = data.get('npm', student['npm'])
                student['uas'] = data.get('uas', student['uas'])
                student['uu'] = data.get('uu', student['uu'])
                student['uts'] = data.get('uts', student['uts'])
                student['total'] = calculate_total_score(student)
                student['grade'] = calculate_grade(student['total'])
                return jsonify(student)
        return {'message': 'Mahasiswa dengan id {} tidak ditemukan'.format(student_id)}, 404

    def delete(self, student_id):
        for student in students:
            if student['id'] == student_id:
                students.remove(student)
                return {'message': 'Mahasiswa dengan id {} telah dihapus'.format(student_id)}
        return {'message': 'Mahasiswa dengan id {} tidak ditemukan'.format(student_id)}, 404

def calculate_total_score(student):
    uas = student.get('uas', 0)
    uu = student.get('uu', 0)
    uts = student.get('uts', 0)
    return (uas + uu + uts) / 3

def calculate_grade(rataRata):
    if rataRata >= 80:
        return 'A'
    elif rataRata >= 70:
        return 'B'
    elif rataRata >= 60:
        return 'C'
    elif rataRata >= 50:
        return 'D'
    else:
        return 'E'

# Register resource
api.add_resource(Student, '/students', '/students/<int:student_id>')

# Render template
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Input data mahasiswa
@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        name = request.form['name']
        npm = request.form['npm']
        uas = int(request.form['uas'])
        uu = int(request.form['uu'])
        uts = int(request.form['uts'])
        id = len(students) + 1
        data = {'id': id, 'name': name, 'npm': npm, 'uas': uas, 'uu': uu, 'uts': uts}
        data['total'] = calculate_total_score(data)
        data['grade'] = calculate_grade(data['total'])
        students.append(data)
        return redirect('/')
    return render_template('input.html')

# Edit data mahasiswa
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    student = None
    for s in students:
        if s['id'] == id:
            student = s
            break
    if request.method == 'POST':
        name = request.form['name']
        npm = request.form['npm']
        uas = int(request.form['uas'])
        uu = int(request.form['uu'])
        uts = int(request.form['uts'])
        student['name'] = name
        student['npm'] = npm
        student['uas'] = uas
        student['uu'] = uu
        student['uts'] = uts
        student['total'] = calculate_total_score(student)
        student['grade'] = calculate_grade(student['total'])
        return redirect('/')
    return render_template('edit.html', student=student)

# Hapus data mahasiswa
@app.route('/delete/<int:id>', methods=['POST'])
def delete_data(id):
    for s in students:
        if s['id'] == id:
            students.remove(s)
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
