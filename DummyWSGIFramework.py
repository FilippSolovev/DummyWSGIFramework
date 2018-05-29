import re


def render(string):
    return [string.encode(encoding='utf-8')]


class ReinventedWheel:

    def __init__(self):
        self.urls = []

    @staticmethod
    def not_found(environ, start_response):
        """Should be overridden"""
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return render('Not found')

    def route(self, url):
        def decorator(handler):
            def wrapped(*args, **kwargs):
                proper_handler = handler(*args, **kwargs)
                return proper_handler
            self.urls.append((url, handler))
            return wrapped
        return decorator

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '').lstrip('/')
        for regex, callback in self.urls:
            match = re.search(regex, path)
            if match is not None:
                return callback(environ, start_response)
        return self.not_found(environ, start_response)
