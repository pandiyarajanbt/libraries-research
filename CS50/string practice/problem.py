"""
Question 1: Reverse a String
Write a function reverse_string(s) that reverses the input string without using built-in reverse methods.
Starter: def reverse_string(s):
Test: reverse_string("hello") → "olleh"

"""

def reverse_string(string):
    print(string[::-1])
response = reverse_string('hello')
# print(response)


"""
Question 2: Count Vowels
Create count_vowels(s) to count vowels (a, e, i, o, u) in a string, case-insensitive.
Starter: def count_vowels(s):
Test: count_vowels("aeroplane") → 5
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

response = count_vowels("aeroplane")
# print(response)
    

"""
Question 3: Palindrome Check
Build is_palindrome(s) that returns True if the string is a palindrome, ignoring spaces and case.
Starter: def is_palindrome(s):
Test: is_palindrome("A man a plan a canal Panama") → True
"""

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False
response = is_palindrome("madam1")
# print(response)


"""
Question 4: Capitalize Words
Write capitalize_words(s) to capitalize the first letter of each word.
Starter: def capitalize_words(s):
Test: capitalize_words("hello world python") → "Hello World Python"
"""

def capitalize_words(s):
    words = s.title()
    return words
response = capitalize_words("hello world python")
# print(response)


"""
Question 5: Find Substring
Implement find_substring(main, sub) returning the starting index of sub in main or -1 if not found.
Starter: def find_substring(main, sub):
Test: find_substring("hello world", "world") → 6
"""

def find_substring(main, sub):
    main_words = main.find('w')
    return main_words

response = find_substring("hello world", "world")
# print(response)


"""
Question 6: Remove Duplicates
Create remove_duplicates(s) to return a string with consecutive duplicate characters removed.
Starter: def remove_duplicates(s):
Test: remove_duplicates("mississippi") → "misp"
"""


def remove_duplicates(s):
    unique_str = list(dict.fromkeys(s))
    result = "".join(unique_str)
    return result
response = remove_duplicates("mississippi")
# print(response)


"""
Question 7: String to Integer
Write str_to_int(s) to convert a numeric string to an integer without int(). Handle positive only.
Starter: def str_to_int(s):
Test: str_to_int("123") → 123
"""

def str_to_int(s):
    result = 0
    signin = 1
    
    if s and s[0] in ( '+', '-'):
        if s[0] == '-':
            sign = -1
        s = s[s:]
    
    for char in s:
        digit_value = ord(char) - ord('0')
        result = result * 10 + digit_value
    return result * signin
    
response = str_to_int("123")
# print(type(response))


"""
Question 8: Anagram Check
Build are_anagrams(s1, s2) returning True if strings are anagrams, case-insensitive.
Starter: def are_anagrams(s1, s2):
Test: are_anagrams("listen", "silent") → True
"""
 
def are_anagrams(s1, s2):
    s1_processed = sorted(s1.replace("", "").lower())
    s2_processed = sorted(s2.replace("", "").lower())
    print(s1_processed)
    print(s2_processed)
    return s1_processed == s2_processed

response = are_anagrams("listen", "silent")
# print(response)
    

"""
Question 9: Longest Word
Find longest_word(s) returning the longest word in a string (split by spaces).
Starter: def longest_word(s):
Test: longest_word("Python is powerful") → "powerful"
"""

def longest_word(s):
    words = s.split(" ")
    results = max(words)
    # print(results)

response = longest_word("Python is powerful")
# print(response)


"""
Question 10: Format Phone Number
Write format_phone(num) to format a string of digits like "1234567890" into "(123) 456-7890".
Starter: def format_phone(num):
Test: format_phone("1234567890") → "(123) 456-7890"
"""

def format_phone(num):
    first_three_words = num[0:3]
    mid_number = num[3:6]
    last_number = num[6:]
    return f"({first_three_words}) {mid_number}-{last_number}"

response = format_phone("9500525108")
# print(response)