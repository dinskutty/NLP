from bottle import Bottle,run,template,request
from predict import *

app=Bottle()

@app.route('/')
def get_name():
    return '''
        <form action="/results" method="post">
            Name: <input name="name" type="text" /><br><br>
            <input value="Submit" type="submit" />
        </form>
    '''
@app.route('/results',method='POST')
def index():
    name = request.forms.get('name')
    return 'Results:\n',template('{{ans}}',ans=predict(name, 3))

run(app,host='localhost', port=8080)
