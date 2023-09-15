'''
Create two dictionaries.
Compare them with each other and display output as “Dictionaries have same content which is” xyz
Otherwise display, “Not similar”
'''
# first dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
# second dictionary
dict2 = {'a': 1, 'b': 2, 'c': 3}
# Compare the dictionaries
if dict1 == dict2:
    print("Dictionaries have the same content which is", dict1)
else:
    print("Not similar")