class Bar(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
def main():
    bar = Bar(a=1, b=2)
    print bar.a 
            
if __name__=="__main__":
    main()
