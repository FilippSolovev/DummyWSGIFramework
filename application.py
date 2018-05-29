import datetime
from urllib.parse import parse_qs

from reinventedwheel import ReinventedWheel, render


application = ReinventedWheel()


@application.route(r'^$')
def index_handler(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return render('Index')


@application.route(r'contacts/')
def contacts_handler(environ, start_response):
    contact_details = 'some contact information'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return render(f'Contacts: {contact_details}')


@application.route(r'^time/$')
def current_time_handler(environ, start_response):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return render(f'It is now {now}')


@application.route(r'^time/?$')  # example: localhost:9090/time?plus=2
def hours_ahead_handler(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'plus' in parameters:
        offset = int(parameters['plus'][0])
    else:
        offset = 0
    time_ahead = datetime.datetime.now() + datetime.timedelta(hours=offset)
    time_ahead = time_ahead.strftime('%H:%M:%S')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return render(f'In {offset} hour(s), it will be {time_ahead}')


if __name__ == '__main__':

    from wsgiref.simple_server import make_server
    server = make_server('localhost', 9090, application)
    server.serve_forever()
