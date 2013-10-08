from django.template import Template, Context

class Person(object):
    def first_name(self):
        raise Test

class Test(AssertionError):
    silent_variable_failure = True
    
t = Template('Hello, {{ person.first_name }}.')
c = Context({'person': Person})
print t.render(c)