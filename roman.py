def int_to_roman(num):
    # Define the mapping of numbers to Roman numerals
    SymbolandValue = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
        90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
        5: "V", 4: "IV", 1: "I"
    }
    
#     # Initialize an empty string to store the Roman numeral
#     roman = ""
    
#     # Iterate over the dictionary in descending order of values
#     for value in sorted(SymbolandValue.keys(), reverse=True):
#         # Determine how many times the Roman numeral can fit into the number
#         while num >= value:
#             # Append the corresponding Roman numeral to the result
#             roman += SymbolandValue[value]
#             # Subtract the value from the number
#             num -= value
    
#     return roman

# # Example usage
# num = 5
# print(f"The Roman numeral for {num} is {int_to_roman(num)}.")
