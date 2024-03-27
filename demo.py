def hi(name="yasoob"):
    print("Now you are inside the hi() function")
    
    def greet():
        return "Now you are in the greet() function"
    
    def welcome():
        return "now you are in thte welcome() function"
    
    
    print(greet())
    print(welcome())
    print("now you are back in the hi() function")
    
    
hi()