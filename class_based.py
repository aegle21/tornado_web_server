import json
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


define("port", default=8000, help="run on the given port", type=str)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainRequestHandler),
            (r"/(\w+)", ResourceRequestHandler),
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)


class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Welcome to home page!')


class ResourceRequestHandler(tornado.web.RequestHandler):
    def get(self, n):
        try:
            response = json.dumps({'result': random.randint(0, int(n))})
            self.write(response)
        except ValueError:
            self.write('Invalid request param')


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()