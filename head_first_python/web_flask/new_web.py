from flask import Flask

from head_first_python.web_flask.search import search

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask,屌的一批'

@app.route('/kaka')#/后面是指定路径，随意写
def do_search()->str:
    return str(search('看下情况sdasdfsdaf','sdfsdafsa'))


app.run()
