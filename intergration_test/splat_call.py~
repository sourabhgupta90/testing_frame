def foo(**kwargs):
    print kwargs
        
def testFunc( **kwargs ):
    options = {
            'option1' : 'default_value1',
            'option2' : 'default_value2',
            'option3' : 'default_value3', }

    options.update(kwargs)
    print options

def main():
    kwargs = {'a':1, 'b':2, 'c':3}
    
    a = foo(**kwargs)
    
    testFunc( option1='new_value1', option3='new_value3' )
    # {'option2': 'default_value2', 'option3': 'new_value3', 'option1': 'new_value1'}

    testFunc( option2='new_value2' )        
        
     
    
if __name__=="__main__":
    main()
