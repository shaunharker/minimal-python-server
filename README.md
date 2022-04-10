# minimal-python-server

Here's a tutorial on how to call python functions from html javascript.

We'll use the Web Server Gateway Interface (WSGI).

### `server.py`

```python
from wsgiref.simple_server import make_server

def hello_world_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    message = "Hello World"
    return [bytes(message, "utf8")]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")

httpd.serve_forever()
```

### `index.html`

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1 id="message"></h1>
        <script>
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'http://127.0.0.1:8000/', true);
            xhr.onload = function () {
                document.getElementById("message").innerHTML = this.responseText;
            };
            xhr.send();
        </script>
    </body>
</html>
```

### Run the server

```bash
python server.py
```

### Run the client

```bash
open index.html
```
