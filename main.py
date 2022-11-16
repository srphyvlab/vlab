from flask import Flask, request, url_for, redirect, render_template
import numpy as  np
import pandas as pd
import json
import plotly
import plotly.express as px
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home/index.html')

@app.route('/objectives')
def obj():
    return render_template('home/objective.html')

@app.route('/experiments/SHM/objectives')
def obj1():
    return render_template('exp1/objective.html')
    
@app.route('/experiments/Young/objectives')
def obj2():
    return render_template('exp2/objective.html')

@app.route('/experiments/quantum/objectives')
def obj3():
    return render_template('exp3/objective.html')

@app.route('/experiments')
def exp():
    return render_template('home/experiments.html')

@app.route('/experiments/SHM')
def exp1():
    return render_template('exp1/index.html')

@app.route('/experiments/Young')
def exp2():
    return render_template('exp2/index.html')

@app.route('/experiments/exp3')
def exp3():
    return render_template('exp3/index.html')

@app.route('/feedback')
def feed():
    return render_template('home/feedback.html')

@app.route('/target_audience')
def target():
    return render_template('home/target_audience.html')

@app.route('/course_alignment')
def course():
    return render_template('home/course_alignment.html')

@app.route('/experiments/SHM/theory')
def theory1():
    return render_template('exp1/theory.html')

@app.route('/experiments/Young/theory')
def theory2():
    return render_template('exp2/theory.html')

@app.route('/experiments/quantum/theory')
def theory3():
    return render_template('exp3/theory.html')

@app.route('/experiments/SHM/pretest')
def pre1():
    return render_template('exp1/pretest.html')

@app.route('/experiments/Young/pretest')
def pre2():
    return render_template('exp2/pretest.html')

@app.route('/experiments/quantum/pretest')
def pre3():
    return render_template('exp3/theory.html')

@app.route('/experiments/SHM/procedure')
def pro1():
    return render_template('exp1/procedure.html')
    
@app.route('/experiments/Young/procedure')
def pro2():
    return render_template('exp2/procedure.html')

@app.route('/experiments/quantum/procedure')
def pro3():
    return render_template('exp3/procedure.html')


    
@app.route('/experiments/SHM/simulation', methods=["POST", "GET"])
def sim1():
    return render_template('exp1/Driven Damped Harmonic Motion.html')

@app.route('/experiments/Young/simulation', methods=["POST", "GET"])
def sim2():
    return render_template("exp2/Driven Damped Harmonic Motion.html")

@app.route('/experiments/quantum/simulation', methods=["POST", "GET"])
def sim3():
    return render_template("exp2/Driven Damped Harmonic Motion.html")

@app.route('/experiments/SHM/posttest')
def post1():
    return render_template('exp1/posttest.html')

@app.route('/experiments/Young/posttest')
def post2():
    return render_template('exp2/posttest.html')

@app.route('/experiments/quantum/posttest')
def post3():
    return render_template('exp3/posttest.html')

@app.route('/experiments/SHM/references')
def ref():
    return render_template('exp1/references.html')
@app.route('/experiments/Young/references')
def ref2():
    return render_template('exp2/references.html')
@app.route('/experiment/quantum/references')
def ref3():
    return render_template('exp3/references.html')
if __name__ == '__main__':
    app.run(debug=True)
