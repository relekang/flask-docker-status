import subprocess

from flask import Flask, render_template
from flask.ext.cache import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.debug = True


@app.route("/")
@cache.cached(timeout=30)
def index():
    process = subprocess.Popen(
        'docker ps',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True
    )
    (stdout, stderr) = process.communicate()
    out = stdout.decode('utf-8').strip() if stdout else ''

    return render_template('index.html', ps_output=out)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
