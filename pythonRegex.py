# create regex if the string starts with "The" and ends with "Spain":
# Path: regmatch.py
# add multiline comment
# ^ asserts the start of the string.
# The matches the literal characters "The".
# .* matches any character (except a newline) zero or more times.
# Spain matches the literal characters "Spain".
# $ asserts the end of the string.
import re
def new_func2():
    pattern = re.compile(r"^The.*Spain$")
    string = "The capital of Spain"
    if pattern.match(string):
        print("Match!")
    else:
        print("No match!")

new_func2()