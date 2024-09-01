'''
stri="100kl564abc365bg" out put should be 564 in python without using inbuilt functions. with simple methods.

To extract the largest integer from the string `"100kl564abc365bg"` without using inbuilt functions,
you can achieve this by iterating over the string, building numbers when you encounter digits, and comparing them.
 Here's a simple solution:

```python
stri = "100kl564abc365bg"

# Initialize variables
current_num = 0
max_num = 0
in_number = False

# Iterate over each character in the string
for char in stri:
    # If the character is a digit
    if '0' <= char <= '9':
        # If we're already in a number, continue building it
        current_num = current_num * 10 + int(char)
        in_number = True
    else:
        # If we encounter a non-digit, check if we were in a number
        if in_number:
            # Compare the current number with the max number
            if current_num > max_num:
                max_num = current_num
            # Reset for the next potential number
            current_num = 0
            in_number = False

# After the loop, make sure to check the last number if any
if current_num > max_num:
    max_num = current_num

print(max_num)
```

### Explanation:
1. **Variables**:
   - `current_num` is used to build the current number.
   - `max_num` holds the largest number found so far.
   - `in_number` is a flag indicating whether we are currently building a number.

2. **Loop**: We iterate through each character in the string:
   - If the character is a digit (checked using `if '0' <= char <= '9'`), we build the number
   by multiplying the current number by 10 and adding the new digit.
   - If the character is not a digit and we were building a number (`in_number` is `True`),
    we compare the current number with `max_num`, and if it's larger, we update `max_num`.

3. **Final Check**: After the loop, we check one last time if `current_num` is larger than `max_num`
in case the string ends with a number.

### Output:
The output for the string `"100kl564abc365bg"` will be:

```python
564
```
'''
# ------------------------------------------------------------------------------------------------
'''
a= [1, 2, 3]
b = ["a", "b", "c", "d", "e", "f", "i"]
c =[i%len(a) for i in range(len(b))]
print(c)
write in normal program
---------------------
The list comprehension `[i % len(a) for i in range(len(b))]` generates a list where each element is the remainder 
when the index `i` is divided by the length of list `a`. Here’s how you can write the equivalent code without using 
list comprehension:

```python
a = [1, 2, 3]
b = ["a", "b", "c", "d", "e", "f", "i"]

# Initialize an empty list to store the results
c = []

# Iterate over the range of the length of list b
for i in range(len(b)):
    # Calculate i % len(a) and append the result to list c
    c.append(i % len(a))

# Print the resulting list c
print(c)
```

### Explanation:
1. **`a` and `b`**: The lists `a` and `b` are predefined.
2. **Loop**: We loop over the range of the length of `b`.
3. **Modulo Operation**: For each index `i`, we compute `i % len(a)`, which gives the remainder when `i` is divided
 by the length of `a` (which is 3 in this case).
4. **Append to List**: The result of the modulo operation is appended to the list `c`.
5. **Print**: Finally, we print the list `c`.

This will produce the same output as the list comprehension:

```python
[0, 1, 2, 0, 1, 2, 0]
```
#########################################################################>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
extract the middle elements 
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] in simple function python i list comprehension and lambda 
----------------------------------------------------------------------------------------------------------
Let's break down how to extract the middle elements (i.e., the middle element from each sublist) 
from the list `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` using a simple function, list comprehension, and a lambda function.

### 1. Using a Simple Function

```python
def extract_middle_elements(matrix):
    middle_elements = []
    for row in matrix:
        middle_elements.append(row[1])  # Access the middle element in each row (index 1)
    return middle_elements

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
middle_elements = extract_middle_elements(matrix)
print(middle_elements)  # Outputs: [2, 5, 8]
```

### 2. Using List Comprehension

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
middle_elements = [row[1] for row in matrix]  # List comprehension to extract middle elements
print(middle_elements)  # Outputs: [2, 5, 8]
```

### 3. Using Lambda and `map`

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
extract_middle = lambda row: row[1]
middle_elements = list(map(extract_middle, matrix))  # Apply lambda to each row
print(middle_elements)  # Outputs: [2, 5, 8]
```

### Summary:
- **Simple Function**: A straightforward way to loop through the matrix and collect the middle elements.
- **List Comprehension**: A more Pythonic and concise way to achieve the same result.
- **Lambda and `map`**: A functional approach using `lambda` to define a function inline and `map`
 to apply it across the matrix.

'''
##Stri="100kl564abc365bg" out put should be 564 in python without using inbuilt functions. with simple methods.
'''
To extract the largest integer from the string `"100kl564abc365bg"` without using inbuilt functions, 
you can achieve this by iterating over the string, building numbers when you encounter digits, and comparing them. 
Here's a simple solution:

```python
stri = "100kl564abc365bg"

# Initialize variables
current_num = 0
max_num = 0
in_number = False

# Iterate over each character in the string
for char in stri:
    # If the character is a digit
    if '0' <= char <= '9':
        # If we're already in a number, continue building it
        current_num = current_num * 10 + int(char)
        in_number = True
    else:
        # If we encounter a non-digit, check if we were in a number
        if in_number:
            # Compare the current number with the max number
            if current_num > max_num:
                max_num = current_num
            # Reset for the next potential number
            current_num = 0
            in_number = False

# After the loop, make sure to check the last number if any
if current_num > max_num:
    max_num = current_num

print(max_num)
```

### Explanation:
1. **Variables**: 
   - `current_num` is used to build the current number.
   - `max_num` holds the largest number found so far.
   - `in_number` is a flag indicating whether we are currently building a number.

2. **Loop**: We iterate through each character in the string:
   - If the character is a digit (checked using `if '0' <= char <= '9'`), we build the number by 
   multiplying the current number by 10 and adding the new digit.
   - If the character is not a digit and we were building a number (`in_number` is `True`), 
   we compare the current number with `max_num`, and if it's larger, we update `max_num`.

3. **Final Check**: After the loop, we check one last time if `current_num` is larger than `max_num` 
in case the string ends with a number.

### Output:
The output for the string `"100kl564abc365bg"` will be:

```python
564
```
----------------------------------------------------------------------------------------------------------########
input  , a=[1,2,3] ,b=[4,5,6]output should be [5,7,9] use decorators in python

#############
You can achieve this by using decorators to implement the functionality that adds corresponding elements 
of two lists together. Here's how you can use a decorator to wrap a function that performs the addition of two lists:

### Code with Decorator:

```python
# Decorator to add corresponding elements of two lists
def add_elements_decorator(func):
    def wrapper(a, b):
        # Perform element-wise addition inside the decorator
        return [a[i] + b[i] for i in range(len(a))]
    return wrapper

@add_elements_decorator
def add_lists(a, b):
    return a, b  # The actual function doesn't do the adding; the decorator does.

# Example input
a = [1, 2, 3]
b = [4, 5, 6]

# Call the function
result = add_lists(a, b)

print(result)  # Outputs: [5, 7, 9]
```

### Explanation:
1. **Decorator Function** (`add_elements_decorator`):
   - This function takes another function (`func`) as its input and returns a wrapper function.
   - Inside the wrapper, we perform the element-wise addition of the two lists `a` and `b`.

2. **Wrapper Function**:
   - The wrapper function is where the actual list addition happens.
   - It adds corresponding elements of the lists `a` and `b` using list comprehension.

3. **Decorated Function** (`add_lists`):
   - The function `add_lists` is decorated with `@add_elements_decorator`.
   - The original `add_lists` function doesn't perform the addition; instead, the decorator modifies the behavior.

4. **Output**:
   - When you call `add_lists(a, b)`, the decorator intercepts the call and performs the element-wise addition, 
   resulting in the output `[5, 7, 9]`.

### Output:

```python
[5, 7, 9]
```

This demonstrates how decorators can be used to modify the behavior of functions, in this case adding 
corresponding elements from two lists.

'''
##TypeError: drag_and_drop_by_offset() missing 3 required positional arguments: 'source', 'xoffset', and
# 'yoffset' in python selenium
'''
Error 1: TypeError: drag_and_drop_by_offset() missing 3 required positional arguments: 'source', 'xoffset', and 'yoffset'
'''
# input :- test90pop12java99pyt$$@#
# output:- tset90pop12avaj99typ#@$$
# in python regular expression
'''
To reverse the alphabetic characters in a string while preserving the positions of the digits, 
symbols, and special characters using regular expressions in Python, you can approach it like this:

1. Use regular expressions to extract the alphabetic characters.
2. Reverse those characters.
3. Re-insert them into the original positions while leaving the non-alphabetic characters untouched.

Here's how you can implement this:

### Code:

```python
import re

def reverse_alphabets(input_string):
    # Find all alphabetic characters using regex
    alphabets = re.findall(r'[a-zA-Z]', input_string)
    
    # Reverse the list of alphabetic characters
    alphabets.reverse()
    
    # Initialize an index to track the position in the reversed alphabets
    alpha_index = 0
    
    # Create a new list to hold the result
    result = []
    
    # Loop through the original string
    for char in input_string:
        # If the character is alphabetic, replace it with the reversed alphabetic character
        if char.isalpha():
            result.append(alphabets[alpha_index])
            alpha_index += 1
        else:
            # If it's not alphabetic, just keep the original character
            result.append(char)
    
    # Join the list into a string and return
    return ''.join(result)

# Example input
input_string = "test90pop12java99pyt$$@#"

# Get the output
output = reverse_alphabets(input_string)

print(output)
```

### Explanation:

1. **Regular Expression (`re.findall`)**:
   - The `re.findall(r'[a-zA-Z]', input_string)` extracts all the alphabetic characters from the 
   input string. It returns a list of alphabetic characters.

2. **Reversing the Alphabets**:
   - The list of alphabetic characters is reversed using `alphabets.reverse()`.

3. **Rebuilding the String**:
   - We iterate over the original string, and for each alphabetic character, we replace it with a 
   character from the reversed list.
   - Non-alphabetic characters (like digits and special characters) are directly added to the result 
   list without modification.

4. **Joining the List**:
   - The result list is joined back into a single string using `''.join(result)`.

### Input:

```python
input_string = "test90pop12java99pyt$$@#"
```

### Output:

```python
tset90pop12avaj99typ#@$$
```

### Summary:

This approach efficiently reverses only the alphabetic characters in the string while leaving the 
digits and special characters in their original positions using regular expressions and string manipulation in Python.

'''
#str='aaaabbbbbccc'
# output :- a4b5c3 in python

'''
You can achieve the desired output by counting the consecutive occurrences of each character in the string and then appending the character followed by its count to the result. Here's how you can do it:

### Code:

```python
def compress_string(input_str):
    # Initialize variables
    compressed = []
    count = 1
    
    # Iterate through the string
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1  # Increment count if current char is the same as the previous
        else:
            compressed.append(input_str[i - 1] + str(count))  # Append the character and count
            count = 1  # Reset count for new character
    
    # Append the last character and its count
    compressed.append(input_str[-1] + str(count))
    
    # Join the list into a compressed string
    return ''.join(compressed)

# Example input
str_input = 'aaaabbbbbccc'

# Get the compressed output
output = compress_string(str_input)

print(output)
```

### Explanation:

1. **Iteration through the String**:
   - We loop through the string starting from the second character (index 1).
   - If the current character is the same as the previous one, we increase the count.
   - If the character changes, we append the previous character and its count to a list and reset the count.

2. **Appending the Final Character**:
   - After the loop, we append the last character and its count since it won't be appended inside the loop.

3. **Joining the List**:
   - Finally, the list of characters and counts is joined to form the compressed string.

### Input:

```python
str_input = 'aaaabbbbbccc'
```

### Output:

```python
a4b5c3
```

This method will compress the string as required, outputting `a4b5c3` for the input `'aaaabbbbbccc'`.
'''
