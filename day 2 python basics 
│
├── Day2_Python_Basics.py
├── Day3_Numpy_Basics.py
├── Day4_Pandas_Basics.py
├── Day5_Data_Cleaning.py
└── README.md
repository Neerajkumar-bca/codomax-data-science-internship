# 1. Variable and Data Types
name = "Amit"
age = 20
cgpa = 8.5
is_student = True
print("Name:", name, type(name))
print("Age:", age, type(age))

# 2. Operators
a, b = 10, 3
print("Add:", a+b, "Div:", a/b, "Power:", a**b)

# 3. Loop
for i in range(1, 6):
    print("Number:", i)

# 4. Function
def add_numbers(x, y):
    return x + y
print("Sum:", add_numbers(5, 7))

# 5. List + If Else
marks = [45, 67, 89]
for m in marks:
    if m > 60:
        print(m, "Pass")
    else:
        print(m, "Fail")