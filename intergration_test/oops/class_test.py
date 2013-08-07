class A():
    __private_variable = 3
    def __init__(self):
        print 'constructor'        
        
class B():
    def __init__(self):
        print 'constructor'

class NumberClass():
    def __init__(self, page_counter, *args, **kwargs):
        self.page_counter = page_counter

def numbered_class(page_counter):
    def f(*args, **kwargs):
        NumberClass(page_counter, *args, **kwargs)
    return f

a = A()
