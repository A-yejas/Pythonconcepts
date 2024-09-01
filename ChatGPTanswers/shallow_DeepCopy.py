'''
In Python, **shallow copy** and **deep copy** are two different ways to copy objects.
They differ in how they handle copying the objects and the objects they contain (such as nested lists or objects).

### Shallow Copy

A **shallow copy** of an object is a new object that is a copy of the original object,
but it only copies the references to the objects found in the original. This means that if the original
object contains other objects (like lists, dictionaries, etc.), the shallow copy will reference the same objects,
not create new copies of them.

#### Example of Shallow Copy:

```python
import copy

# Original list
original_list = [1, 2, [3, 4]]

# Shallow copy
shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copied_list[2][0] = 99

print("Original list:", original_list)       # Outputs: [1, 2, [99, 4]]
print("Shallow copied list:", shallow_copied_list)  # Outputs: [1, 2, [99, 4]]
```

**Explanation**:
- `shallow_copied_list` is a shallow copy of `original_list`.
- When the nested list `[3, 4]` is modified in `shallow_copied_list`,
the change is also reflected in `original_list` because both lists share the same reference to the nested list.

### Deep Copy

A **deep copy** of an object is a new object that is a copy of the original object, along with copies
of all objects that are referenced by the original object. This means that deep copying creates entirely independent
objects, even for nested structures.

#### Example of Deep Copy:

```python
import copy

# Original list
original_list = [1, 2, [3, 4]]

# Deep copy
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copied_list[2][0] = 99

print("Original list:", original_list)       # Outputs: [1, 2, [3, 4]]
print("Deep copied list:", deep_copied_list)  # Outputs: [1, 2, [99, 4]]
```

**Explanation**:
- `deep_copied_list` is a deep copy of `original_list`.
- When the nested list `[3, 4]` is modified in `deep_copied_list`, the change does not affect `original_list` because deep copying creates a completely independent copy of the nested list.

### Key Differences

1. **Shared References**:
   - **Shallow Copy**: Copies the reference pointers, so nested objects are shared between the original and the copy.
   - **Deep Copy**: Creates new copies of all nested objects, so no shared references.

2. **Performance**:
   - **Shallow Copy**: Faster, as it only copies the top-level structure.
   - **Deep Copy**: Slower, as it recursively copies all objects.

3. **When to Use**:
   - **Shallow Copy**: When you need a copy of the object and you don't mind sharing the nested objects between the original and the copy.
   - **Deep Copy**: When you need a completely independent copy of the object, including all nested objects.

### Practical Use Cases
- **Shallow Copy**: Useful when working with large data structures where creating a deep copy would be unnecessary and resource-intensive, and when you are certain that nested objects do not need to be modified.
- **Deep Copy**: Essential when you need to ensure that changes in the copied object do not affect the original object, especially when working with nested or complex data structures.


'''
