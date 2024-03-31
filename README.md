# Code Challenges

This repository contains several Python code challenges and their solutions.

## Table of Contents

- [regex_phone_number_finder.py](#regex_phone_number_finderpy)
- [mean_std_calc.py](#mean_std_calcpy)
- [dict_key_assertions.py](#dict_key_assertionspy)
- [Squares_Generator.py](#squares_generatorpy)

## regex_phone_number_finder.py

This script reads the contents of a file named 'lorem_ipsum_phone_numbers.txt' located in the working directory and finds all occurrences of phone numbers in the format `xxx-xxx-xxxx` using regular expressions. The found phone numbers are returned as a list.

## mean_std_calc.py

This script generates a list of random numbers with a mean of 10 and a standard deviation of 1 using the `random.gauss()` function. It then calculates the mean and standard deviation of the generated list using the mathematical formulas for mean and standard deviation. The calculated mean and standard deviation are returned as a tuple.

## dict_key_assertions.py

This script demonstrates the behavior of immutable objects (in this case, strings) and their memory addresses when passed to a function. It uses the `id()` function to get the memory addresses of the objects before and after passing them to a function. The script asserts that the memory address of the immutable object (string) changes after reassigning a value to it within the function, while the memory address of the mutable object (number) remains the same.

## Squares_Generator.py

This script defines a Python generator function `squares()` that generates a continuous sequence of squares of integers starting from 0. The `squares_caller()` function takes an integer `n` as input and prints the first `n` squares generated by the `squares()` generator.

To run any of these scripts, simply execute the corresponding Python file in your terminal or command prompt.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

### License
Distributed under the MIT License. See LICENSE for more information.

### Contact
Nikolai Baldwin - https://www.linkedin.com/in/nikolai-a-baldwin/

Project Link: https://github.com/nikolai3ldwin/Code_Challenges
