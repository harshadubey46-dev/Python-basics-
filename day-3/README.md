# 📅 Day 3 - Data Structures I (Lists, Tuples, Dicts)

## 🎯 Learning Objectives

By the end of Day 3, you will:
- ✨ Master Python Lists and operations
- ✨ Understand Tuples (immutable sequences)
- ✨ Work with Dictionaries (key-value pairs)
- ✨ Learn data structure selection

---

## 📚 Topics Covered

### 1. **Lists**
```python
# Create and access
numbers = [1, 2, 3, 4, 5]
print(numbers[0])        # Output: 1
print(numbers[-1])       # Output: 5 (last element)

# Add/Remove
numbers.append(6)        # O(1)
numbers.insert(0, 0)     # O(n)
numbers.remove(3)        # O(n)
popped = numbers.pop()   # O(1)
```

**Time Complexity:**
| Operation | Best | Avg | Worst |
|-----------|------|-----|-------|
| Access | O(1) | O(1) | O(1) |
| Search | O(1) | O(n) | O(n) |
| Insert | O(1) | O(n) | O(n) |
| Delete | O(1) | O(n) | O(n) |

### 2. **Tuples** (Immutable)
```python
coordinates = (10, 20)
print(coordinates[0])    # O(1) access
# coordinates[0] = 5     # ERROR! Tuples are immutable

# Unpacking
x, y = coordinates
print(x, y)              # 10 20
```

**Time Complexity:** O(1) for access, O(n) for search

### 3. **Dictionaries**
```python
student = {
    "name": "Harsha",
    "age": 20,
    "gpa": 3.8
}

# Access
print(student["name"])   # O(1) average
print(student.get("city", "N/A"))  # Safe access

# Add/Update
student["city"] = "India"    # O(1)
student.update({"age": 21})  # O(n)

# Delete
del student["city"]          # O(1)
student.pop("age")           # O(1)
```

**Time Complexity:** O(1) average for most operations

### 4. **List Comprehensions**
```python
# Traditional
squares = []
for x in range(5):
    squares.append(x**2)

# Comprehension (Pythonic!)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 🔑 Key Concepts

| DS | Mutable | Ordered | Indexed | Use Case |
|----|---------|---------|---------|----------|
| List | ✅ | ✅ | ✅ | General storage |
| Tuple | ❌ | ✅ | ✅ | Fixed collections |
| Dict | ✅ | ❌ | ❌ | Key-value pairs |

---

## 💻 Practice Problems

1. **List Operations**
   - Create list, add/remove elements, find sum and average

2. **Tuple Unpacking**
   - Multiple assignment and tuple swapping

3. **Dictionary Manipulation**
   - Create student dict, update grades, find top scores

4. **List Comprehension**
   - Generate squares, filter evens, flatten nested lists

5. **Word Frequency Counter**
   - Count word occurrences in a string (use dict)

---

## 🌟 Resources

- [Python Docs - Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)

---

## 💡 Tips & Tricks

✨ Use lists for ordered, changeable data  
✨ Use tuples for immutable sequences  
✨ Use dicts for fast lookups with keys  
✨ List comprehensions are faster and cleaner!  

---

## 📝 Daily Checklist

- [ ] Master list operations
- [ ] Understand tuple immutability
- [ ] Learn dictionary operations
- [ ] Write list comprehensions
- [ ] Complete 5 practice problems

**Next → Day 4: Data Structures II (Sets, Comprehensions, Strings)**
