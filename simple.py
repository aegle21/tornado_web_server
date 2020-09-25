import random
import tornado.web
import tornado.ioloop
import json


class ResourceRequestHandler(tornado.web.RequestHandler):
    def get(self, n):
        try:
            response = json.dumps({'result': random.randint(0, int(n))})
            self.write(response)
        except ValueError:
            self.write('Invalid request param')


def make_app():
    return tornado.web.Application([
        (r"/(\w+)",  ResourceRequestHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
