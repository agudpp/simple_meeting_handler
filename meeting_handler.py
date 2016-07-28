from flask import Flask
from flask import render_template



app = Flask(__name__)

app.config.update(DEBUG = True)

################################################################################
# configs

MEETING_POINTS = [
    {
        "title": "friendly talk", 
        "duration_secs": 10,
        "description": "hablamos de cualquier cosa aca"
    },
    {
        "title": "update agu", 
        "duration_secs": 5,
        "description": "agu update"
    },
    {
        "title": "update raul", 
        "duration_secs": 5,
        "description": "raul update"
    },
    {
        "title": "update mingo", 
        "duration_secs": 5,
        "description": "mingo update"
    }
]

################################################################################
# configure all
def genTimeStructure():
    currTime = 0
    for x in MEETING_POINTS:
        x['base_time'] = currTime
        currTime = x['duration_secs'] + currTime
    



################################################################################
# server functions

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/p/<name1>")
def first_argument(name1=None):
    return render_template('test.html' , name=name1, elementList=MEETING_POINTS)
    #return "This is the argument %s " % argument

if __name__ == "__main__":
    genTimeStructure()
    app.run()