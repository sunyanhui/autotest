
'''
Created on 2009-9-29

@author: selfimpr
'''
class Window(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class WindowDescriptor(object):
    def __init__(self, obj):
        self.data = obj
    '''
    @param self: instance of WindowDescriptor
    @param obj: instance of Main
    @param type: unknow
    '''
    def __get__(self, obj, type = None):
        print 'get method called'
        return 'width: %s, height: %s' % (self.data.width, self.data.height)
    '''
    @param self: instance of WindowDescriptor
    @param obj: instance of Main
    @param value: value is 1024, it is the value after equal mark
    '''
    def __set__(self, obj, value):
        print 'set method called'
        self.data.width = value
        self.data.height = obj.height
    '''
    @param self: instance of WindowDescriptor
    @param obj: instance of Main
    '''
    def __delete__(self, obj):
        print 'delete method called'
        del self.data
        del self

class Main(object):
    def __init__(self, height):
        self.height = height
    '''
    This is a data descriptor
    '''
    window = WindowDescriptor(Window(width = 800, height = 600))


if __name__ == '__main__':
    m = Main(600)
    m.height = 768
    m.window = 1024 #call method name is __set__ in window data descriptor
    print m.window #call method name is __get__ in window data descriptor
    del m.window #call method name is __delete__ in window data descriptor

