# How to integrate HTML with Flask 
# Jinga 2 = if you have separate data source you can integrate with HTML
#HTTP verb GET and POST 


'''
{%...%} condition for loops 
{{   }} expressions to print ouput 
{#...#} this is for comments 
'''



from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template('result.html', result="success", score=score)

@app.route('/fail/<int:score>')  
def fail(score):
    return render_template('result.html', result="fail", score=score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0 
    if request.method == 'POST':
        science = float(request.form.get('science', 0))
        maths = float(request.form.get('maths', 0))
        c = float(request.form.get('c', 0))
        data_science = float(request.form.get('data_science', 0))
        total_score = (science + maths + c + data_science) / 4 

    res = "success" if total_score >= 50 else "fail"
    return redirect(url_for(res, score=total_score))  

if __name__ == '__main__':
    app.run(debug=True)