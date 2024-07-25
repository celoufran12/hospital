from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models after db is initialized to avoid circular import
from models import *

@app.route('/')
def index():
    patients = Patient.query.order_by(Patient.wait_time.asc()).all()
    return render_template('index.html', patients=patients)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if 'update_id' in request.form:
            # Updating patient condition
            patient_id = request.form['update_id']
            patient = Patient.query.get(patient_id)
            patient.severity = request.form['severity']
            patient.wait_time = request.form['wait_time']
            db.session.commit()
        elif 'delete_id' in request.form:
            # Deleting patient
            patient_id = request.form['delete_id']
            patient = Patient.query.get(patient_id)
            db.session.delete(patient)
            db.session.commit()
        else:
            # Adding a new patient
            name = request.form['name']
            severity = request.form['severity']
            wait_time = request.form['wait_time']
            new_patient = Patient(name=name, severity=severity, wait_time=wait_time)
            db.session.add(new_patient)
            db.session.commit()
        return redirect(url_for('admin'))
    patients = Patient.query.all()
    return render_template('admin.html', patients=patients)

@app.route('/init_db')
def init_db():
    db.create_all()
    return "Database initialized."

if __name__ == '__main__':
    app.run(debug=True)
