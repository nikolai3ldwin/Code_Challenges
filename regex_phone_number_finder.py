'''
Used the open() function to open the file in read mode ('r'). This will read the contents of the file into the variable text.
Then, compiled a regular expression pattern phone_pattern using re.compile();
This pattern matches phone numbers in the format xxx-xxx-xxxx, where 'x' represents a digit.
Next, using re.findall() to find all occurrences of phone numbers that match the phone_pattern in the text.
Finally, returning phone_list, which contains all the found phone numbers.
'''
def stub():
    # Read the text of the 'lorem_ipsum_phone_numbers.txt' file located in the working directory 
    with open('lorem_ipsum_phone_numbers.txt', 'r') as file:
        text = file.read()

    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    phone_list = re.findall(phone_pattern, text)
    return phone_list

if __name__ == '__main__':
    ret_val = stub()
    print(ret_val)
