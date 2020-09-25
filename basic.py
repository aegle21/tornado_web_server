import random
import tornado.web
import tornado.ioloop
import json


class ResourceRequestHandler(tornado.web.RequestHandler):
    def get(self, n):
        response = json.dumps({'result': random.randint(0, int(n))})
        self.write(response)


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/([0-9]+)", ResourceRequestHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()