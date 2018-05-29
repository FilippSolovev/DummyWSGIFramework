# The Dummy WSGI Framework

WSGI stands for the Python Web Server Gateway Interface, which is a standard interface between web servers and Python web applications or frameworks. It was specified in 2003 in the [PEP 333](https://www.python.org/dev/peps/pep-0333/ "PEP 333") and later in 2010 in the [PEP 3333](https://www.python.org/dev/peps/pep-3333/ "PEP 3333"). In short words according to the standard, a WSGI application has the following:
* it is by itself a callable object (either a function or a class with a __ call __ method)
* it acquires two arguments: a WSGI environment and a function that starts the response
* an application has to start a response using the function provided and return an iterable where each yielded item means writing and flushing

Here is an example of a WSGI-compatible framework, that has been derived from [The first WSGI application](http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html#the-first-wsgi-application "The first WSGI application") by putting it inside a class named 'ReinventedWheel.' The intention of creating this 'framework' was by no means practical but somewhat educational.

# How to use

The first thing you should to do to use this framework is obviously to import a 'ReinventedWheel' class and a render function to your module. After this, you can inherit from that class in order to override a not_found method to make it more custom. Then create an instance of a framework class and decorate your handler functions with route method of the class. It looks pretty much the same as a flask application.

~~~~
from DummyWSGIFramework import ReinventedWheel, render


application = ReinventedWheel()


@application.route(r'^$')
def index_handler(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return render('Index')
~~~~

For more examples see the enclosed application.py file.

# Installation and running

Clone the project and install the requirements:

~~~~
$ git clone https://github.com/FilippSolovev/DummyWSGIFramework.git
$ pip install -r requirements.txt
~~~~

As documentation for the uWSGI suggests run an HTTP server/router passing requests to your WSGI application:

~~~~
uwsgi --http :9090 --wsgi-file application.py
~~~~

Or you can use the wsgiref WSGI standalone server bundled with python 2.5 and higher by adding to your application file the following lines of code:

~~~~
if __name__ == '__main__':

    from wsgiref.simple_server import make_server
    server = make_server('localhost', 9090, application)
    server.serve_forever()
~~~~

# Built With
* [Python 3](https://docs.python.org/3/ "Python 3")
* [The uWSGI Project](http://uwsgi-docs.readthedocs.io/en/latest/index.html "uWSGI")

# Authors
[FilippSolovev](https://github.com/FilippSolovev "FilippSolovev")

# License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/FilippSolovev/DummyWSGIFramework/blob/master/LICENSE) file for details
