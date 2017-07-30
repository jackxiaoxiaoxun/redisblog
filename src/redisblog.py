import rblog.util
import web
import rblog.router



app = web.application(rblog.router.urls, globals())

if __name__ == '__main__':
    app.run()
