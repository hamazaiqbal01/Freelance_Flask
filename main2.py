from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
    return render_template('result.html', 
                         status="Pass" if score >= 50 else "Fail",
                         score=score)

@app.route('/submit', methods=['POST'])
def submit():
    subjects = ['science', 'maths', 'c', 'data_science']
    average = sum(float(request.form.get(subj, 0)) for subj in subjects) / 4
    return redirect(url_for('result', score=average))

if __name__ == '__main__':
    app.run(debug=True)