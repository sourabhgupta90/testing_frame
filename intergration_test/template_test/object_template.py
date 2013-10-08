from django.template import Template, Context

class Person(object):
	def __init__(self, first_name, last_name):
     		self.first_name, self.last_name = first_name, last_name
#t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
#c = Context({'person': Person('John', 'Smith')})
#t.render(c)

