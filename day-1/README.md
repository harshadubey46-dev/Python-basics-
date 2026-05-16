# 📅 Day 1 - Python Basics & Fundamentals

## 🎯 Learning Objectives

By the end of Day 1, you will:
- ✨ Understand Python variables and data types
- ✨ Learn input/output operations
- ✨ Explore type conversion and casting
- ✨ Understand Python naming conventions

---

## 📚 Topics Covered

### 1. **Variables & Data Types**
```python
# Integers
age = 25

# Floats
height = 5.9

# Strings
name = "Harsha"

# Booleans
is_student = True

# Multiple assignment
a, b, c = 1, 2, 3
```

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

### 2. **Input/Output Operations**
```python
# Input
name = input("Enter your name: ")

# Output
print("Hello, " + name)
```

### 3. **Type Conversion**
```python
num_str = "25"
num_int = int(num_str)        # String to Integer
num_float = float(num_int)     # Integer to Float
num_str_back = str(num_float)  # Float to String
```

### 4. **Variable Naming Conventions**
- Use `snake_case` for variables: `user_name`, `total_price`
- Use `UPPER_CASE` for constants: `PI = 3.14`
- Avoid Python keywords: `if`, `for`, `class`, etc.

---

## 🔑 Key Concepts

| Concept | Example | Output |
|---------|---------|--------|
| Variable Assignment | `x = 10` | Stores 10 in x |
| Dynamic Typing | `x = 10; x = "ten"` | Type changes |
| Type Check | `type(x)` | Returns <class 'int'> |
| Length | `len("Hello")` | 5 |

---

## 💻 Practice Problems

1. **Simple Input/Output**
   - Take user's name and age, print a greeting with their birth year

2. **Temperature Converter**
   - Convert Celsius to Fahrenheit: F = (C × 9/5) + 32

3. **Circle Area Calculator**
   - Given radius, calculate area: A = π × r²

4. **String Manipulation**
   - Take a string, print it in different cases (upper, lower, title)

5. **Type Conversion Challenge**
   - Take string input of numbers, convert to int/float, perform arithmetic

---

## 🌟 Resources

- [Python Docs - Variables](https://docs.python.org/3/tutorial/introduction.html)
- [Real Python - Data Types](https://realpython.com/python-data-types/)
- [W3Schools - Variables](https://www.w3schools.com/python/python_variables.asp)

---

## 💡 Tips & Tricks

✨ Use `type()` to check variable types  
✨ Use `input()` for user interaction  
✨ Remember: Everything in Python is an object!  
✨ Use meaningful variable names for readability  

---

## 📝 Daily Checklist

- [ ] Understand all 4 basic data types
- [ ] Practice input/output operations
- [ ] Learn type conversion
- [ ] Complete 5 practice problems
- [ ] Review code and add comments

**Next → Day 2: Control Flow & Functions**
