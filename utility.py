########################################
# This is a example module that should #
# define a function and a class for    #
# other scripts to use                 #
########################################

#--- define a function for summation ---#
def add_numbers(number1, number2): #refer to the naming conventioin file in our course repo
    summation = number1 + number2
    return summation


#--- define a class which has one attribute and one method ---#
class Person(): #refer to the naming convention file in out course repo
    
    #python built-in dunder methods for defining class
    #dunder init is an example of dunder methods and it is used for defining attributes
    def __init__(self, name): 
        self.name = name #only one attribute for this class

    #define a method 
    def greet(self):
        print(f"Hi, my name is {self.name}")
    

        
