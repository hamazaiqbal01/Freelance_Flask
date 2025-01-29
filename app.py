#  this is th basic understanding 
from flask import Flask
# WSGI= Web server gateway Application 
app = Flask (__name__)


@app.route('/') # Decoratort = When i go to this url below msg will be displayed 
def welcome():
    return "Welcome to Hamza Website. Hello. Hello, hello "

@app.route('/members') 
def members():
    return "Hi can you hear me "

if __name__ == '__main__': # It ensue code under it runs
    app.run(debug=True) # only when script is executed not imported 
            # as a module 


######################################################################


######################################################################



######################################################################



######################################################################



######################################################################


######################################################################

# this code shows how multiple urls work

from flask import Flask
app= Flask(__name__) # creating object of the Flask 

@app.route('/') # decorators 
def welcome():
    return 'Welome Hamza '


@app.route('/success/<int:score>')
def success(score):
    return " This perosn has passed and marks is  " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return " This perosn has failed and marks is  " + str(score)

# Result Checker 
@app.route('/result/<int:score>')
def results(score):
    result= ""
    if score < 50: 
        result = "fail"
    else: 
        result = 'Pass'
    return result 

if __name__ == '__main__':
    app.run(debug=True)


######################################################################




######################################################################




######################################################################




######################################################################




######################################################################

##  Now i want to show different webpage for fail and sucess student

from flask import Flask, redirect, url_for
app= Flask(__name__) # creating object of the Flask 

@app.route('/') # decorators 
def welcome():
    return 'Welome Hamza '


@app.route('/success/<int:score>')
def success(score):
    return " This perosn has passed and marks is  " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return " This perosn has failed and marks is  " + str(score)

# Result Checker 
@app.route('/result/<int:score>')
def results(score):
    result= ""
    if score < 50: 
        result = "fail"
    else: 
        result = 'success'
    return redirect(url_for(result,score=score))

if __name__ == '__main__':
    app.run(debug=True)