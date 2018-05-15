from flask import Flask, render_template, abort, send_file, redirect
from flask_socketio import SocketIO, emit
import os,sys

from urls import urls_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.register_blueprint(urls_blueprint)

socketio = SocketIO(app)

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = './'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)
    print(abs_path,file=sys.stderr)

    # top page
    if abs_path == BASE_DIR and os.path.exists("./index.html"):
        return redirect("./index.html", code=302)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        if abs_path.endswith('.py'):
            #return abort(404)
            return redirect(abs_path.replace(".py", "", -1), code=302)
        else:
            return send_file(abs_path)

    # Show directory contents
    files = []
    for x in os.listdir(abs_path):
        if os.path.isdir(abs_path + x):  #isdirの代わりにisfileを使う
            files.append(x+"/")
        elif not x.endswith('.py'):
            files.append(x)
    return render_template('files.html', files=files)

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message2(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)