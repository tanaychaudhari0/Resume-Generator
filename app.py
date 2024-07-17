from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    user_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'address': request.form['address'],
        'objective': request.form['objective'],
        'education': request.form['education'],
        'experience': request.form['experience'],
        'skills': request.form['skills']
    }
    return render_template('resume.html', user_data=user_data)


if __name__ == '__main__':
    app.run(debug=True)

