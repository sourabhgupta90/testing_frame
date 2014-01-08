class _BaseType(object):
    def __init__(self, base_dict):
        self.base_dict = base_dict
        for key,value in self.base_dict.items():
            setattr(self,key,value)
        self._dirty = False
    
    def set_dirty(self, value=True):
        self._dirty = value

    def is_dirty(self):
        return self._dirty

    def get_path(self, dot_path):
        '''Gets a Nested Path, It uses schema's get_value method to access the
           attributes defined through schema, and has a custom logic to access
           derived attributes.
           '''
        print "on get path",dot_path
        paths = dot_path.split('.')[1:]
        if hasattr(self, paths[-1]):
            return getattr(self, paths[-1])
        else:
            obj = self._base_dict
            for path in paths[:-1]:
                if isinstance(obj, dict):
                    if path in obj:
                        obj = obj[path]
                    else:
                        return None
                else:
                    raise Exception('Object must be Dict. Was %s at %s' %
                                   (obj.__class__, path))
            return obj.get(paths[-1])

    def set_path(self, dot_path, value):
        '''Sets a value to the attribute specified through Nested Path,
           It uses schema's set_value method to set the attributes defined
           through schema, and has a custom logic to set derived attributes.
           '''
        paths = dot_path.split('.')[1:]
        print paths[-1], hasattr(self, paths[-1])
        if hasattr(self, paths[-1]):
            print "has-attr"
            setattr(self, paths[-1], value)
            self.set_dirty(True)
        else:
            obj = self._base_dict
            for path in paths[:-1]:
                if isinstance(obj, dict):
                    if path in obj:
                        obj = obj[path]
                    else:
                        return
                else:
                    raise Exception('Object must be Dict. Was %s at %s' %
                                   (obj.__class__, path))

            obj[paths[-1]] = value
            print self._base_dict
            self.set_dirty(True)


class PersonType(_BaseType):
    def __init__(self, value):
        super(PersonType,self).__init__(value)
        
    @property
    def home(self):
        print "on home"
        return self.home
    
    @home.setter
    def home(self, value):
        print "on setter"
        self.home = value