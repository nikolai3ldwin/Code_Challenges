'''
Python's built-in id() function returns a unique id (a number) for an object passed as the parameter.
This id is the object's memory address on the Python virtual machine's heap.
For immutable objects, object id changes after re-assigning a value of the variable;
if you pass the immutable object to a function,
the changed object will stay changed only inside the function;
not reflecting the change in the initial variable's value when the function returns.

Note:
This is different for mutable objects -- dictionaries and lists -- whose elements can be modified within the local scope of a function.
'''

def funky_fun(my_dict, my_number):
    my_dict['some key'] = 'another value'
    my_number = 9999.12
 
def stub():
    my_dict = {'some key' : 'some value'}
    my_number = 1234.99
    
    id_dict_key = id(my_dict['some key']) 
    id_num = id(my_number)
    
    funky_fun(my_dict, my_number)
    

    assert id_dict_key != id(my_dict['some key'])
    assert id_num == id(my_number)
    

if __name__ == '__main__':
    stub()
    print ('Passed ...')
