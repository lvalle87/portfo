from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def back_home(page_name):
    return render_template(page_name)

def write_to_csv_file(data):
    with open('database.csv', newline='', mode='a') as file:
        fieldnames = ['name','email','message']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv_file(data)
        return redirect('/thank.html')
    else:
        return 'error while requesting data'
