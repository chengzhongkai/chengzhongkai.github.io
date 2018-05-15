# help infomation
This site is maked by flask(python). You can get help from [flask site](http://flask.pocoo.org/).
- [Quickstart](http://flask.pocoo.org/docs/1.0/quickstart/)
- [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO): WebSocket

## startup
```
set FLASK_APP=app.py
flask run
```
> http://localhost:5000/index.html

## python flask browsing through directory with files
```python
@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = '/Users/vivek/Desktop'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)
```
Template:
```html
<ul>
    {% for file in files %}
    <li><a href="{{ file }}">{{ file }}</a></li>
    {% endfor %}
</ul>
```
## [Flaskで静的ファイルの格納ディレクトリとURLを変更する](https://qiita.com/5zm/items/db6acb96594e0ff7c549)

