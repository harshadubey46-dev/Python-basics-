# 📅 Day 4 - Data Structures II (Sets, Comprehensions, Strings)

## 🎯 Learning Objectives

By the end of Day 4, you will:
- ✨ Understand sets and set operations
- ✨ Master list/dict comprehensions
- ✨ Learn string manipulation
- ✨ Understand string methods and formatting

---

## 📚 Topics Covered

### 1. **Sets (Unique, Unordered)**
```python
# Create set
numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Add: O(1) average
numbers.add(5)

# Remove: O(1) average
numbers.remove(1)

# Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a | set_b      # {1,2,3,4,5}
intersection = set_a & set_b  # {3}
difference = set_a - set_b    # {1,2}
```

**Time Complexity:** Add O(1), Remove O(1)

### 2. **List Comprehensions**
```python
# Simple
squares = [x**2 for x in range(5)]  # [0,1,4,9,16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

**Time Complexity:** O(n)

### 3. **Dictionary Comprehensions**
```python
# Create dictionary
squares_dict = {x: x**2 for x in range(5)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

**Time Complexity:** O(n)

### 4. **String Operations**
```python
# Create string
text = "Hello, World!"

# Access: O(1)
print(text[0])  # 'H'

# Slice: O(k) where k is slice length
print(text[0:5])  # 'Hello'

# Methods: O(n)
print(text.lower())
print(text.upper())
print(text.replace("World", "Python"))
print(text.split(","))
```

### 5. **String Formatting**
```python
name = "Harsha"
age = 20

# f-string
print(f"Hello {name}, age {age}")

# format()
print("Hello {}, age {}".format(name, age))

# % operator
print("Hello %s, age %d" % (name, age))
```

---

## 🔑 Key Concepts

| Method | Complexity | Use Case |
|--------|-----------|----------|
| Set add | O(1) | Remove duplicates |
| Set remove | O(1) | Delete element |
| List comprehension | O(n) | Create filtered list |
| String split | O(n) | Parse text |
| String replace | O(n) | Text substitution |

---

## 💻 Practice Problems

1. **Duplicate Remover**
   - Use set to remove duplicates from list

2. **Even Squares**
   - Create list of squares of even numbers (1-10)

3. **String Reversal**
   - Reverse a string using slicing

4. **Word Frequency**
   - Count word frequency in sentence

5. **Email Validator**
   - Check if email contains @ and .

---

## 🌟 Resources

- [Python Docs - Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Real Python - List Comprehensions](https://realpython.com/list-comprehensions-and-generator-expressions/)

---

## 💡 Tips & Tricks

✨ Use sets for fast lookups (O(1))  
✨ List comprehensions are faster than loops  
✨ Strings are immutable in Python  
✨ Use f-strings for modern Python code  

---

## 📝 Daily Checklist

- [ ] Understand set operations
- [ ] Master list comprehensions
- [ ] Learn dictionary comprehensions
- [ ] Practice string manipulation
- [ ] Complete 5 practice problems

**Next → Day 5: OOP Concepts (Classes, Objects, Inheritance)**
