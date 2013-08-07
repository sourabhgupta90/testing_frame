import re

def check_validation(field_value = None,field_meta = None):
    clear_validation_test = True
    clear_range_test = True
    
    if 'validation' in field_meta:  
        
        if isinstance(field_value[0],dict): 
           for value in field_value:
               for validation_field in  field_meta['validation']:
                   for key,re_exp in validation_field.iteritems():
                       if key in value and re.match( validation_field[key],str(value[key])) == None:  
                           clear_validation_test = False
        elif  re.match( field_meta['validation'],str(field_value)) == None :
            clear_validation_test = False
    
    if 'range' in field_meta :
        range = field_meta['range']
        if 'max' in range and float(field_value) > float ( range['max'] ) :
            clear_validation_test = False
        if 'min' in range and float(field_value) < float ( range['min'] ) :
            clear_validation_test = False    
        
    return clear_range_test and clear_validation_test

def main_program():
    field_value = [{"BP Systolic":"23"},{"BP Diastolic":"452"}]
    field_meta = { "validation":[{"BP Systolic":"^[0-9]{0,3}$"},{"BP Diastolic":"^[0-9]{0,3}$"}]}
    print check_validation(field_value,field_meta)
    
#response = self.save_form(self.facility, self.patient['id'], self.task, {self._qid('24'):{ [{'BP Systolic':'12'}] }})
#self.assertIn(self._qid('24'), response['updated'],'Error: value is not equal to the whole numbers ')    
    
if __name__ == '__main__':
    main_program()    
