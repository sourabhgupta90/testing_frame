import colander
from colander import Schema
import types 

cstruct = {
         'name':'keith',
         'age':'20',
         'friends':[('1', 'jim'),('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
         'phones':[{'location':[], 'number':'555-1212'},
                   {'location':'work', 'number':'555-8989'},],
          "mobile":{"home":"232323"} 
          }

class Friend(colander.TupleSchema):
    rank = colander.SchemaNode(colander.Int(),
                               validator=colander.Range(0, 9999))
    name = colander.SchemaNode(colander.String())

class Phone(colander.MappingSchema):
    location = colander.SchemaNode(colander.String(),
                                  validator=colander.OneOf(['home', 'work']))
    number = colander.SchemaNode(colander.String())
    
    def deserialize(self, cstruct):
        for i in cstruct: 
            if isinstance(cstruct['location'], list):
                cstruct['location'] = 'home'
        return super(Phone, self).deserialize(cstruct)


class Friends(colander.SequenceSchema):
    friend = Friend()

class Phones(colander.SequenceSchema):
    phone = Phone()

      
class Mobile(colander.MappingSchema):
    home = colander.SchemaNode(colander.String(),missing='')
    
class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    age = colander.SchemaNode(colander.Int(),
                             validator=colander.Range(0, 200))
    friends = Friends()
    phones = Phones()
    mobile = Mobile()
    
    def deserialize(self, cstruct):
        appstruct = super(Person, self).deserialize(cstruct)
        return types.PersonType(appstruct)
 
    
def testColanderSchema():
    schema = Person()
    deserialized = schema.deserialize(cstruct)
    print deserialized
    
def testUpdateColanderSchema():
    schema = Person()
    person_obj = schema.deserialize(cstruct)
    person_obj._base_dict = cstruct
    person_obj.set_path('person.mobile.home',{"value":"4545545"})
    print person_obj._base_dict