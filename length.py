def count_letters(input_string):
    letter_count = 0

    for char in input_string:
        if char.isalpha():
            letter_count += 1

    return letter_count

# Example Usage
input_string = "Hello World! How are you?"
result = count_letters(input_string)

print(f"The number of letters in the string is: {result}")

