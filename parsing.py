"""
parsing.py
A function that returns a tuple of items.
"""
import sys

def stats(collection):
    "Return the minimum, maximum, and concatenates the strings in the collection."
    return (min(collection,key=len), max(collection,key=len), ' '.join(collection)) #outer parens unnecessary

listOfStrings = ["this","is","a","bunch","of","words"]
shortest, longest, sentence = stats(listOfStrings)

print(f"whole sentence = {sentence}")
print(f"shortest word = {shortest}")
print(f"longest word = {longest}")
sys.exit(0)
