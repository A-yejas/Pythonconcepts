# What is pickling and unpickling?in python
'''
In Python, pickling and unpickling refer to the process of serializing and deserializing objects, respectively.

Pickling: This is the process of converting a Python object into a byte stream.
This is useful when you want to save an object to a file or send it over a network.
The pickle module in Python provides this functionality. The pickled object can be stored in a file or
transmitted and later reconstructed.

Unpickling: This is the reverse process, where a byte stream (from a file or received over a network)
is converted back into a Python object. The pickle module handles this as well.

import pickle

# Example object
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Pickling the object
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Unpickling the object
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
-------------------
In this example:

pickle.dump(data, file) serializes the data dictionary and writes it to a file (data.pkl).
pickle.load(file) reads the byte stream from the file and deserializes it back into a Python dictionary.
Use Cases
Pickling is often used to save complex data structures, like lists or dictionaries, to a file so they can be easily loaded later.
Unpickling is used to restore these objects to their original state, allowing for easy persistence and retrieval of Python objects.
---------------

Features of OrderedDict
Maintains Order: It preserves the order of keys as they are added.
Extra Methods: It provides methods like move_to_end(), which can move an existing key to either end of the dictionary,
and popitem(), which allows you to pop the last item (or the first item if specified).

from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Iterating over the OrderedDict
for key, value in ordered_dict.items():
    print(key, value)


Methods Specific to OrderedDict
1.move_to_end(key, last=True): Moves the specified key to the end (or to the beginning if last=False).
popitem(last=True): Removes and returns a (key, value) pair from the dictionary. If last=True,
it pops the last item; otherwise, it pops the first item. When to Use OrderedDict.
2.Order-Sensitive Applications: When the order of elements matters, such as in caches or algorithms that depend on insertion order.
Backwards Compatibility: If you're working with older versions of Python (prior to 3.7) where dict does not maintain order.
3.Custom Methods: If you need the additional methods provided by OrderedDict.
For most modern applications in Python 3.7 and later, you can rely on the standard dict to maintain insertion order,
but OrderedDict remains a useful tool in specific scenarios.
'''
