'''
Object Introspection:
Introspection is the automatic process of discovering an object's attributes.
Python offers this capability through the built-in dir() function.
When dir() takes an object as an argument, it returns:
"an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it."

The function returns a list of all the method names of a string object that start with the 'is' prefix
(the first three such method names are shown below):
['isalnum', 'isalpha', 'isascii', ...]
'''

def is_object_introspection():
    is_methods = [method for method in dir(str) if method.startswith('is')]
    return is_methods 

if __name__ == '__main__':
    ret_val = is_object_introspection()
    print(ret_val)
