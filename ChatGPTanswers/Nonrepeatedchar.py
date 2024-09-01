def non_repeating_chars(string):
    # Initialize an empty list to hold the frequency of characters
    frequency = [0] * 256  # Assuming ASCII charset

    # Traverse through the string and increment frequency
    for char in string:
        frequency[ord(char)] += 1

    # Traverse the string again to print non-repeating characters
    for char in string:
        if frequency[ord(char)] == 1:
            print(char, end=" ")

# Example usage
input_string = "programming"
non_repeating_chars(input_string)
