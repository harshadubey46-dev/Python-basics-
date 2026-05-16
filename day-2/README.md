# 📅 Day 2 - Control Flow & Functions

## 🎯 Learning Objectives

By the end of Day 2, you will:
- ✨ Master conditional statements (if, elif, else)
- ✨ Understand loops (for, while, break, continue)
- ✨ Create and call functions
- ✨ Learn function parameters and return values

---

## 📚 Topics Covered

### 1. **Conditional Statements**
```python
# If-elif-else
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

**Time Complexity:** O(1)

### 2. **Loops**

**For Loop:**
```python
for i in range(5):           # Time: O(n)
    print(i)
```

**While Loop:**
```python
count = 0
while count < 5:             # Time: O(n)
    print(count)
    count += 1
```

**Break & Continue:**
```python
for i in range(10):
    if i == 5:
        break                # Exit loop
    if i == 2:
        continue             # Skip iteration
    print(i)
```

### 3. **Functions**
```python
def greet(name, age=18):     # Default parameter
    """Greet a person"""
    return f"Hello {name}, age {age}"

result = greet("Harsha", 20)
print(result)
```

**Time Complexity:** O(1) to O(n) depending on function body

### 4. **Function Scope**
```python
x = 10  # Global

def func():
    x = 5  # Local
    print(x)  # Prints 5

func()
print(x)  # Prints 10
```

---

## 🔑 Key Concepts

| Concept | Example | Purpose |
|---------|---------|---------|
| if-elif-else | `if x > 0: ... elif x < 0: ... else: ...` | Conditional execution |
| for loop | `for i in range(10):` | Iterate n times |
| while loop | `while x > 0:` | Iterate until condition false |
| Function | `def add(a, b): return a+b` | Reusable code block |
| Return | `return value` | Send value back |

---

## 💻 Practice Problems

1. **Number Checker**
   - Take input, check if positive, negative, or zero

2. **Factorial Calculator**
   - Create function to calculate factorial: 5! = 120

3. **Pattern Printing**
   - Print triangle/pyramid pattern using loops

4. **Prime Number Checker**
   - Create function to check if number is prime

5. **Sum of N Numbers**
   - Create function to sum first N natural numbers

---

## 🌟 Resources

- [Python Docs - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Functions](https://realpython.com/defining-your-own-python-function/)

---

## 💡 Tips & Tricks

✨ Use `range()` for efficient loops  
✨ Functions make code reusable and readable  
✨ Use meaningful function names  
✨ Add docstrings to functions  

---

## 📝 Daily Checklist

- [ ] Master if-elif-else statements
- [ ] Understand for and while loops
- [ ] Create and use functions
- [ ] Learn function parameters
- [ ] Complete 5 practice problems

**Next → Day 3: Data Structures I (Lists, Tuples, Dictionaries)**
