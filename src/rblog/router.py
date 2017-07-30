#encoding=utf8

urls = (
    '([a-z0-9\/]*)', 'rblog.router.dispatcher'
    )

class dispatcher:
    def __init__(self):
        pass
    def GET(self, path):
        return self.__request(path,'get')

    def POST(self, path):
        return self.__request(path,'post')

    def __request(self, path='', method="get"):
        try:
            if path.count('/') < 2:
                path = "index/index"
            modelName, controllerName = path.strip()[1:].split('/', 1)
            controllerName = method + controllerName
            if not controllerName:
                controllerName = 'getindex'
            if not modelName or not controllerName:
                return 'model/controller missing'
            moduleList = __import__('view.' + modelName, {}, {}, [modelName])
            modelObj = getattr(moduleList, modelName)()
            if hasattr(modelObj, controllerName):
                result = getattr(modelObj, controllerName)()
            else:
                result = 'no controller'
            return result
        except Exception ,e:
            return e.message
            #raise Exception,e.message
