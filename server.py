from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def back_home(page_name):
    return render_template(page_name)

def write_to_txt_file(data):
    with open('database.txt', mode='a') as file:
        name = data['name']
        email = data['email']
        message = data['message']
        file.write(f'\n{name} {email} {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_txt_file(data)
        return redirect('/thank.html')
    else:
        return 'error while requesting data'