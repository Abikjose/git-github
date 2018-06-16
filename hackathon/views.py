from flask import render_template
from frontend import frontend

@frontend.route('/')
@frontend.route('/index')
def index():
    return render_template('index.html')

@frontend.route('/awsiam/<url>')

def awsiam(url):
    if url =='aws.html':
         return render_template('awsiam/aws.html')
    elif url =='awsjump.html':
         return render_template('awsiam/awsjump.html')
    elif url =='awsopsworks.html':
         return render_template('awsiam/awsopsworks.html')
    else:
        return "<html><body><h1>Sorry, I don't know what you're looking for.</h1></body></html><h1>"

@frontend.route('/orch/orchestrator.html')
def orch():
    return render_template('orch/orchestrator.html')

@frontend.route('/newrelic/newrelic.html')
def newrelic():
    return render_template('newrelic/newrelic.html')

@frontend.route('/rstudio/<url>')
def rstudio(url):
    if url=='rstudio.html':
        return render_template('rstudio/rstudio.html')
    elif url=='mysqljump.html':
        return render_template('rstudio/mysqljump.html')
    else:
         return "<html><body><h1>Sorry, I don't know what you're looking for.</h1></body></html><h1>"
#@frontend.route('/rstudio/mysqljump.html')
#def rstudi():
#    return render_template('rstudio/mysqljump.html')

@frontend.route('/knowledge.html')
def knowledge():
    return render_template('knowledge.html')

@frontend.route('/assets')
def assets():
    return render_template('css/')

#@frontend.route('/success')

