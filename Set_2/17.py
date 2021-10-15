"""
Program:    
    Sorts the string alphabetically.
    Sorts the string by length.
Author:     
    Katarzyna Miałkowska
"""

def sort_alf(line: str) -> str:
    return ' '.join(sorted(list(line.split())))

def sort_len(line: str) -> str:
    return ' '.join(sorted(list(line.split()), key = len ))

line = "bsas deeaas sx aaa"

print("sort alphabetically: {}".format(sort_alf(line)))
print("sort by length : {}".format(sort_len(line)))

