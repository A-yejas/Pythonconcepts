# import requests
#
# def Api_data(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
# Api_data('https/ur/queryparams')
#####################

# import pytest
#
# def is_even(number):
#     return number % 2 == 0
#
# @pytest.mark.parametrize("test_input,expected",[(2,True),(3,False),(10,True)])
# def test_is_even(test_input,expected):
#     assert is_even(test_input) == expected
# ------------------------------------------------
# def fibonacci_generator():
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b,a+b
#
# fib = fibonacci_generator()
#
# for i in range(10):
#     print(next(fib))
# -------------------------------------------------------------------------
def are_anagrams(word1,word2):
    word1 = word1.replace(" ","").lower()
    word2 = word2.replace(" ","").lower()

    return sorted(word1) == sorted(word2)

word1 = "listen"
word2 = "silent"

if are_anagrams(word1,word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")
# -------------------------------------------------------------------------------
def are_anagrams(word1,word2):
    word1 = word1.replace(" ","").lower()
    word2 = word2.replace(" ","").lower()

    return sorted(word1) == sorted(word2)

word1 = "Listen"
word2 = "silent"

if are_anagrams(word1,word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")
# ------------------------------------------
# a = 5
# b = 6
# a = b == 6
# print (a)
