import rblog.util
import web



### Url mappings

urls = (
    '/', 'view.index.index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
)



### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)



app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
