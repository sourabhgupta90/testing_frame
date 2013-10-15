import colander

class Parrot(object):
    def __init__(self):
        self._voltage = 230000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

a = Parrot()
print a.voltage




class cat(object):
    def __init__(self,mapping):
        self.mapping = mapping
        
    def _get(self, paths, value):
        print paths, value
        for path in paths:
            if path in value:
                value = value[path]
            else:
                return colander.null
        return value if value else colander.null

    def __call__(self, values):
        modified_value = {}
        for k, v, f in self.mapping:
            result = self._get(k.split('.'), values)
            print "result", result
            modified_value[v] = f(result) if result and\
                                hasattr(f, '__call__') else result
        return modified_value


pt = cat([('id', 'encounter_id', None)])
value = {"id":23} 
print pt(value)
















