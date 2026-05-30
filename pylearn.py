#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════╗
║         PYTHON MASTER ACADEMY  v1.0                  ║
║         Run:  python3 main.py                        ║
║         Then open: http://localhost:8080             ║
╚═══════════════════════════════════════════════════════╝
"""

import http.server
import socketserver
import webbrowser
import threading
import os
import sys

PORT = 8080

# ─────────────────────────────────────────────────────────────────────────────
#  ALL CONTENT DATA
# ─────────────────────────────────────────────────────────────────────────────

MODULES = [
    {
        "id": 1, "icon": "🐍", "color": "#3b82f6", "color2": "#1d4ed8",
        "title": "Python Fundamentals",
        "subtitle": "শুরু করো এখান থেকে",
        "desc": "Python এর একদম প্রথম ধাপ — variables থেকে শুরু করে basic syntax পর্যন্ত।",
        "xp": 500,
        "topics": [
            {"name": "Introduction to Python", "namebn": "Python পরিচিতি",
             "content": "Python হলো একটি high-level, interpreted programming language যা 1991 সালে Guido van Rossum তৈরি করেন। এটি সহজ syntax এবং বিশাল library এর জন্য বিখ্যাত।\n\nPython ব্যবহার হয়:\n• Web Development (Django, Flask)\n• Data Science (NumPy, Pandas)\n• AI/ML (TensorFlow, PyTorch)\n• Automation & Scripting\n• Cybersecurity\n• Robotics & IoT",
             "example": "# তোমার প্রথম Python program!\nprint('Hello, World!')\nprint('Python Master Academy তে স্বাগতম!')\n\n# Python version চেক করো\nimport sys\nprint(f'Python version: {sys.version}')",
             "tip": "Python install করতে python.org থেকে latest version download করো।"},

            {"name": "Variables & Data Types", "namebn": "ভেরিয়েবল ও ডেটা টাইপ",
             "content": "Variable হলো data store করার জায়গা। Python এ automatically type নির্ধারণ হয়।\n\nমূল Data Types:\n• int — পূর্ণ সংখ্যা (1, 42, -10)\n• float — দশমিক সংখ্যা (3.14, -0.5)\n• str — text (\"Hello\", 'Python')\n• bool — True / False\n• list — ordered collection [1, 2, 3]\n• dict — key-value pairs {'name': 'Alice'}",
             "example": "# Variables তৈরি করো\nname = 'Rahim'          # str\nage = 20                # int\ngpa = 3.85              # float\nis_student = True       # bool\n\n# Type চেক করো\nprint(type(name))       # <class 'str'>\nprint(type(age))        # <class 'int'>\n\n# F-string দিয়ে print করো\nprint(f'{name} এর বয়স {age} বছর')",
             "tip": "Variable নাম lowercase এ লেখো, space এর বদলে underscore ব্যবহার করো।"},

            {"name": "Input & Output", "namebn": "ইনপুট ও আউটপুট",
             "content": "input() দিয়ে user থেকে data নেওয়া যায়। print() দিয়ে output দেখানো যায়।\n\nগুরুত্বপূর্ণ বিষয়:\n• input() সবসময় string return করে\n• int() বা float() দিয়ে convert করতে হয়\n• print() তে sep ও end parameter আছে",
             "example": "# User থেকে input নাও\nname = input('তোমার নাম কী? ')\nage = int(input('তোমার বয়স কত? '))\n\n# Output দেখাও\nprint(f'হ্যালো {name}!')\nprint(f'তুমি {age} বছর বয়সী।')\n\n# আগামী বছর বয়স\nnext_year = age + 1\nprint(f'আগামী বছর তুমি {next_year} বছরের হবে!')",
             "tip": "int(input()) একসাথে লিখলে সরাসরি integer পাবে।"},

            {"name": "Operators", "namebn": "অপারেটর",
             "content": "Operators দিয়ে calculations করা যায়।\n\nArithmetic: + - * / // % **\nComparison: == != > < >= <=\nLogical: and, or, not\nAssignment: = += -= *= /=",
             "example": "a, b = 15, 4\n\n# Arithmetic\nprint(a + b)    # 19\nprint(a - b)    # 11\nprint(a * b)    # 60\nprint(a / b)    # 3.75\nprint(a // b)   # 3  (integer division)\nprint(a % b)    # 3  (remainder)\nprint(a ** b)   # 50625 (power)\n\n# Comparison\nprint(a > b)    # True\nprint(a == b)   # False\n\n# Logical\nprint(a > 10 and b < 10)  # True",
             "tip": "// দিয়ে integer division হয় — ভাগের পূর্ণ অংশ পাওয়া যায়।"},

            {"name": "Comments & Syntax", "namebn": "কমেন্ট ও সিনট্যাক্স",
             "content": "Comment হলো code এর ভেতরে explanation যা program run করে না।\n\n# দিয়ে single line comment\n''' ''' বা \"\"\" \"\"\" দিয়ে multi-line comment\n\nPython এ indentation (4 space বা tab) অত্যন্ত গুরুত্বপূর্ণ!",
             "example": "# এটা একটা single line comment\n\n'''\nএটা একটা\nmulti-line comment\n'''\n\ndef greet(name):\n    # এখানে 4 space indentation আছে\n    print(f'হ্যালো, {name}!')\n    print('Python শেখা মজার!')\n\ngreet('বাংলাদেশ')",
             "tip": "Consistent indentation ব্যবহার করো — সবসময় 4 space।"},
        ],
        "project": {
            "name": "Simple Calculator",
            "namebn": "সাধারণ ক্যালকুলেটর",
            "desc": "দুটি সংখ্যা নিয়ে চারটি arithmetic operation (যোগ, বিয়োগ, গুণ, ভাগ) করার program।",
            "code": "# Simple Calculator Project\nprint('=== সাধারণ ক্যালকুলেটর ===')\n\nnum1 = float(input('প্রথম সংখ্যা দাও: '))\nnum2 = float(input('দ্বিতীয় সংখ্যা দাও: '))\n\nprint('\\nফলাফল:')\nprint(f'  যোগ:    {num1} + {num2} = {num1 + num2}')\nprint(f'  বিয়োগ:  {num1} - {num2} = {num1 - num2}')\nprint(f'  গুণ:    {num1} × {num2} = {num1 * num2}')\nif num2 != 0:\n    print(f'  ভাগ:    {num1} ÷ {num2} = {num1 / num2:.2f}')\nelse:\n    print('  ভাগ:    শূন্য দিয়ে ভাগ করা যায় না!')",
            "skills": ["Variables", "Input/Output", "Operators", "Conditions"]
        }
    },
    {
        "id": 2, "icon": "🔀", "color": "#8b5cf6", "color2": "#6d28d9",
        "title": "Conditional Statements",
        "subtitle": "সিদ্ধান্ত নেওয়া শেখো",
        "desc": "if, elif, else দিয়ে program কে সিদ্ধান্ত নিতে শেখাও।",
        "xp": 600,
        "topics": [
            {"name": "if Statement", "namebn": "if স্টেটমেন্ট",
             "content": "if statement দিয়ে condition check করা হয়। Condition True হলে block execute হয়।\n\nSyntax:\nif condition:\n    # code এখানে\n\nIndentation অবশ্যই দিতে হবে!",
             "example": "age = 18\n\nif age >= 18:\n    print('তুমি প্রাপ্তবয়স্ক।')\n    print('ভোট দিতে পারবে।')\n\n# Number check\nnumber = 42\nif number > 0:\n    print(f'{number} একটি positive number')\nif number % 2 == 0:\n    print(f'{number} একটি জোড় সংখ্যা')",
             "tip": "Condition এর পরে colon (:) দিতে ভুলো না।"},

            {"name": "if-else Statement", "namebn": "if-else স্টেটমেন্ট",
             "content": "else block তখন execute হয় যখন if condition False হয়।\n\nএকটি if এর সাথে একটিই else থাকতে পারে।",
             "example": "temperature = 35\n\nif temperature > 30:\n    print('গরম আবহাওয়া! পানি বেশি পান করো।')\nelse:\n    print('আবহাওয়া ঠিক আছে।')\n\n# Login check\npassword = input('Password দাও: ')\nif password == 'python123':\n    print('✅ Login সফল!')\nelse:\n    print('❌ ভুল password!')",
             "tip": "else কখনো condition নেয় না — সবসময় শেষে আসে।"},

            {"name": "elif Statement", "namebn": "elif স্টেটমেন্ট",
             "content": "elif (else if) দিয়ে একাধিক condition check করা যায়। প্রথম True condition টি execute হয়, বাকিগুলো skip হয়।",
             "example": "score = 75\n\nif score >= 90:\n    grade = 'A+'\nelif score >= 80:\n    grade = 'A'\nelif score >= 70:\n    grade = 'B'\nelif score >= 60:\n    grade = 'C'\nelse:\n    grade = 'F'\n\nprint(f'স্কোর: {score}')\nprint(f'গ্রেড: {grade}')",
             "tip": "elif যত দরকার তত লেখা যায়।"},

            {"name": "Nested Conditions", "namebn": "নেস্টেড কন্ডিশন",
             "content": "if এর ভেতরে আরেকটি if লেখা যায় — এটাই nested condition।\n\nতবে বেশি nested করলে code পড়া কঠিন হয়ে যায়।",
             "example": "age = 20\nhas_id = True\n\nif age >= 18:\n    print('বয়স ঠিক আছে।')\n    if has_id:\n        print('✅ প্রবেশাধিকার দেওয়া হলো!')\n    else:\n        print('❌ ID card নেই!')\nelse:\n    print('❌ বয়স কম, প্রবেশ নিষেধ।')",
             "tip": "Nested এর বদলে and/or ব্যবহার করলে code সহজ হয়।"},
        ],
        "project": {
            "name": "Student Grade Calculator",
            "namebn": "শিক্ষার্থী গ্রেড ক্যালকুলেটর",
            "desc": "পাঁচটি বিষয়ের নম্বর নিয়ে গড় বের করো এবং গ্রেড নির্ধারণ করো।",
            "code": "# Student Grade Calculator\nprint('=== শিক্ষার্থী গ্রেড ক্যালকুলেটর ===')\n\nsubjects = ['বাংলা', 'English', 'গণিত', 'বিজ্ঞান', 'ICT']\nscores = []\n\nfor subject in subjects:\n    score = float(input(f'{subject} নম্বর দাও: '))\n    scores.append(score)\n\naverage = sum(scores) / len(scores)\n\nif average >= 80:\n    grade, point = 'A+', 5.0\nelif average >= 70:\n    grade, point = 'A', 4.0\nelif average >= 60:\n    grade, point = 'A-', 3.5\nelif average >= 50:\n    grade, point = 'B', 3.0\nelif average >= 40:\n    grade, point = 'C', 2.0\nelse:\n    grade, point = 'F', 0.0\n\nprint(f'\\n=== ফলাফল ===')\nprint(f'গড় নম্বর: {average:.1f}')\nprint(f'গ্রেড: {grade}')\nprint(f'GPA: {point}')\nprint('অভিনন্দন!' if grade != 'F' else 'আরো পড়াশোনা করো!')",
            "skills": ["Input/Output", "Lists", "Loops", "Conditions", "F-strings"]
        }
    },
    {
        "id": 3, "icon": "🔁", "color": "#06b6d4", "color2": "#0e7490",
        "title": "Loops",
        "subtitle": "পুনরাবৃত্তি শেখো",
        "desc": "for ও while loop দিয়ে একই কাজ বারবার করো।",
        "xp": 700,
        "topics": [
            {"name": "for Loop", "namebn": "for লুপ",
             "content": "for loop দিয়ে একটি sequence (list, string, range) এর প্রতিটি item এ iterate করা যায়।\n\nSyntax:\nfor item in sequence:\n    # code",
             "example": "# 1 থেকে 5 print করো\nfor i in range(1, 6):\n    print(f'সংখ্যা: {i}')\n\n# List এ iterate\nfruits = ['আম', 'কলা', 'লিচু', 'জাম']\nfor fruit in fruits:\n    print(f'ফল: {fruit}')\n\n# String এ iterate\nfor char in 'Python':\n    print(char, end=' ')",
             "tip": "range(start, stop, step) দিয়ে custom sequence তৈরি করো।"},

            {"name": "while Loop", "namebn": "while লুপ",
             "content": "while loop তখন চলে যতক্ষণ condition True থাকে।\n\nSyntax:\nwhile condition:\n    # code\n\nসাবধান: Infinite loop এড়াতে condition কে False করার ব্যবস্থা রাখো!",
             "example": "# Countdown\ncount = 5\nwhile count > 0:\n    print(f'{count}...')\n    count -= 1\nprint('🚀 উৎক্ষেপণ!')\n\n# User input validate করো\nwhile True:\n    age = int(input('বয়স দাও (1-120): '))\n    if 1 <= age <= 120:\n        break\n    print('ভুল বয়স! আবার চেষ্টা করো।')\nprint(f'তোমার বয়স: {age}')",
             "tip": "while True দিয়ে infinite loop করে break দিয়ে বের হওয়া একটি common pattern।"},

            {"name": "break & continue", "namebn": "break ও continue",
             "content": "break — loop সম্পূর্ণ বন্ধ করে দেয়\ncontinue — current iteration skip করে পরেরটায় যায়",
             "example": "# break example\nfor i in range(1, 11):\n    if i == 6:\n        print('6 পাওয়া গেছে! Loop বন্ধ।')\n        break\n    print(i)\n\n# continue example — জোড় সংখ্যা skip\nprint('\\nবিজোড় সংখ্যা:')\nfor i in range(1, 11):\n    if i % 2 == 0:\n        continue\n    print(i, end=' ')",
             "tip": "break ও continue nested loop এ শুধু innermost loop কে affect করে।"},

            {"name": "Nested Loops", "namebn": "নেস্টেড লুপ",
             "content": "Loop এর ভেতরে আরেকটি loop — এটাই nested loop। Multiplication table, pattern print ইত্যাদিতে ব্যবহার হয়।",
             "example": "# Multiplication table\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(f'{i}×{j}={i*j}', end='  ')\n    print()  # নতুন লাইন\n\n# Star pattern\nfor i in range(1, 6):\n    print('★' * i)",
             "tip": "Outer loop এক বার ঘুরলে inner loop সম্পূর্ণ ঘুরে যায়।"},
        ],
        "project": {
            "name": "Number Guessing Game",
            "namebn": "সংখ্যা অনুমানের খেলা",
            "desc": "Computer একটি random সংখ্যা ঠিক করবে, user গেস করবে। Hint দিয়ে সাহায্য করবে।",
            "code": "# Number Guessing Game\nimport random\n\nprint('=== সংখ্যা অনুমানের খেলা ===')\nprint('আমি 1 থেকে 100 এর মধ্যে একটি সংখ্যা ভাবছি...')\n\nsecret = random.randint(1, 100)\nattempts = 0\nmax_attempts = 7\n\nwhile attempts < max_attempts:\n    remaining = max_attempts - attempts\n    guess = int(input(f'\\nঅনুমান করো ({remaining} সুযোগ বাকি): '))\n    attempts += 1\n    \n    if guess == secret:\n        print(f'🎉 সঠিক! {attempts} চেষ্টায় পেয়েছো!')\n        stars = '⭐' * (8 - attempts)\n        print(f'তোমার রেটিং: {stars}')\n        break\n    elif guess < secret:\n        print('⬆️  বড় সংখ্যা অনুমান করো!')\n    else:\n        print('⬇️  ছোট সংখ্যা অনুমান করো!')\nelse:\n    print(f'\\n😔 হেরে গেছো! সংখ্যাটি ছিল: {secret}')",
            "skills": ["Loops", "Conditions", "Random module", "break"]
        }
    },
    {
        "id": 4, "icon": "⚙️", "color": "#10b981", "color2": "#047857",
        "title": "Functions",
        "subtitle": "কোড পুনর্ব্যবহার করো",
        "desc": "Function দিয়ে code কে reusable block এ ভাগ করো।",
        "xp": 800,
        "topics": [
            {"name": "Functions", "namebn": "ফাংশন",
             "content": "Function হলো একটি named block of code যা বারবার call করা যায়। def keyword দিয়ে তৈরি করা হয়।\n\nSyntax:\ndef function_name():\n    # code\n\nfunction_name()  # call করো",
             "example": "def greet():\n    print('হ্যালো!')\n    print('Python Master Academy তে স্বাগতম!')\n\n# Function call করো\ngreet()\ngreet()  # আবার call করো\n\n# DRY principle: Don't Repeat Yourself",
             "tip": "Function একবার লিখো, যতবার দরকার call করো।"},

            {"name": "Parameters & Arguments", "namebn": "প্যারামিটার",
             "content": "Parameter হলো function এর input। Function call করার সময় argument দেওয়া হয়।\n\nDefault parameter: parameter = default_value",
             "example": "def greet(name, lang='বাংলা'):\n    if lang == 'বাংলা':\n        print(f'হ্যালো, {name}!')\n    else:\n        print(f'Hello, {name}!')\n\ngreet('রহিম')\ngreet('Alice', 'English')\n\n# Multiple parameters\ndef add(a, b, c=0):\n    return a + b + c\n\nprint(add(1, 2))      # 3\nprint(add(1, 2, 3))   # 6",
             "tip": "Default parameter দিলে সেই argument না দিলেও চলে।"},

            {"name": "Return Values", "namebn": "রিটার্ন ভ্যালু",
             "content": "return statement দিয়ে function থেকে value ফেরত দেওয়া যায়। Multiple value return করা যায় tuple হিসেবে।",
             "example": "def square(n):\n    return n * n\n\ndef min_max(numbers):\n    return min(numbers), max(numbers)  # tuple\n\nresult = square(5)\nprint(f'5² = {result}')  # 25\n\nnums = [3, 1, 7, 2, 9]\nsmallest, largest = min_max(nums)\nprint(f'সর্বনিম্ন: {smallest}, সর্বোচ্চ: {largest}')",
             "tip": "return ছাড়া function None return করে।"},

            {"name": "Lambda Functions", "namebn": "ল্যাম্বডা ফাংশন",
             "content": "Lambda হলো single-line anonymous function। Simple operations এ ব্যবহার হয়।\n\nSyntax: lambda arguments: expression",
             "example": "# Regular vs Lambda\ndef double(x):\n    return x * 2\n\ndouble_l = lambda x: x * 2\n\nprint(double(5))    # 10\nprint(double_l(5))  # 10\n\n# Sorting এ lambda\nstudents = [('Rahim', 85), ('Karim', 72), ('Nadia', 91)]\nstudents.sort(key=lambda s: s[1], reverse=True)\n\nfor name, score in students:\n    print(f'{name}: {score}')",
             "tip": "Lambda এ একটাই expression থাকে, complex logic এর জন্য regular function ব্যবহার করো।"},

            {"name": "Recursion", "namebn": "রিকার্সন",
             "content": "Recursion মানে function নিজেকে নিজে call করা। Base case (থামার শর্ত) অবশ্যই থাকতে হবে।",
             "example": "# Factorial\ndef factorial(n):\n    if n <= 1:       # base case\n        return 1\n    return n * factorial(n - 1)  # recursive case\n\nprint(factorial(5))  # 120\nprint(factorial(10)) # 3628800\n\n# Fibonacci\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nfor i in range(8):\n    print(fib(i), end=' ')",
             "tip": "Base case না থাকলে infinite recursion হবে — RecursionError!"},
        ],
        "project": {
            "name": "Scientific Calculator",
            "namebn": "বৈজ্ঞানিক ক্যালকুলেটর",
            "desc": "Functions ব্যবহার করে একটি scientific calculator তৈরি করো যা power, square root, factorial calculate করতে পারে।",
            "code": "# Scientific Calculator\nimport math\n\ndef add(a, b): return a + b\ndef subtract(a, b): return a - b\ndef multiply(a, b): return a * b\ndef divide(a, b): return a / b if b != 0 else 'Error: শূন্য দিয়ে ভাগ!'\ndef power(base, exp): return base ** exp\ndef sqrt(n): return math.sqrt(n) if n >= 0 else 'Error: ঋণাত্মক!'\ndef factorial(n): return math.factorial(int(n)) if n >= 0 else 'Error!'\n\noperations = {\n    '1': ('যোগ (+)', add),\n    '2': ('বিয়োগ (-)', subtract),\n    '3': ('গুণ (×)', multiply),\n    '4': ('ভাগ (÷)', divide),\n    '5': ('ঘাত (^)', power),\n    '6': ('বর্গমূল (√)', sqrt),\n    '7': ('ফ্যাক্টোরিয়াল (!)', factorial),\n}\n\nprint('=== বৈজ্ঞানিক ক্যালকুলেটর ===')\nfor key, (name, _) in operations.items():\n    print(f'  {key}. {name}')\n\nchoice = input('\\nঅপারেশন বেছে নাও: ')\nif choice in operations:\n    name, func = operations[choice]\n    if choice in ['6', '7']:\n        n = float(input('সংখ্যা দাও: '))\n        print(f'ফলাফল: {func(n)}')\n    else:\n        a = float(input('প্রথম সংখ্যা: '))\n        b = float(input('দ্বিতীয় সংখ্যা: '))\n        print(f'ফলাফল: {func(a, b)}')",
            "skills": ["Functions", "Dictionary", "Math module", "Lambda"]
        }
    },
    {
        "id": 5, "icon": "📦", "color": "#f59e0b", "color2": "#d97706",
        "title": "Data Structures",
        "subtitle": "ডেটা সাজিয়ে রাখো",
        "desc": "List, Tuple, Set, Dictionary — Python এর শক্তিশালী data structures।",
        "xp": 900,
        "topics": [
            {"name": "Lists", "namebn": "লিস্ট",
             "content": "List হলো ordered, mutable collection। [] দিয়ে তৈরি করা হয়। যেকোনো type এর data রাখা যায়।\n\nমূল methods: append(), remove(), pop(), sort(), len()",
             "example": "students = ['Rahim', 'Karim', 'Nadia']\n\n# Add\nstudents.append('Sara')\nprint(students)\n\n# Access\nprint(students[0])   # Rahim\nprint(students[-1])  # Sara (শেষেরটা)\n\n# Slice\nprint(students[1:3])  # ['Karim', 'Nadia']\n\n# Remove & sort\nstudents.remove('Karim')\nstudents.sort()\nprint(students)",
             "tip": "Negative index দিয়ে শেষ থেকে access করা যায়।"},

            {"name": "Tuples", "namebn": "টাপল",
             "content": "Tuple হলো ordered, immutable collection। () দিয়ে তৈরি। একবার তৈরি হলে change করা যায় না।\n\nকখন ব্যবহার করবে: Data যখন change হওয়া উচিত নয় — coordinates, RGB color, date etc.",
             "example": "# Tuple তৈরি\ncoords = (23.8103, 90.4125)  # Dhaka\nrgb = (255, 128, 0)\n\nprint(f'Latitude: {coords[0]}')\nprint(f'Longitude: {coords[1]}')\n\n# Unpacking\nx, y = coords\nprint(f'x={x}, y={y}')\n\n# Tuple of tuples\nstudents = (\n    ('Rahim', 85),\n    ('Nadia', 92),\n)\nfor name, score in students:\n    print(f'{name}: {score}')",
             "tip": "Tuple list এর চেয়ে দ্রুত এবং memory কম লাগে।"},

            {"name": "Sets", "namebn": "সেট",
             "content": "Set হলো unordered, unique collection। {} দিয়ে তৈরি। Duplicate automatically remove হয়।\n\nSet operations: union (|), intersection (&), difference (-)",
             "example": "# Duplicate remove\nnumbers = {1, 2, 3, 2, 1, 4}\nprint(numbers)  # {1, 2, 3, 4}\n\n# Set operations\na = {1, 2, 3, 4}\nb = {3, 4, 5, 6}\n\nprint(a | b)  # Union: {1,2,3,4,5,6}\nprint(a & b)  # Intersection: {3,4}\nprint(a - b)  # Difference: {1,2}\n\n# Membership test (দ্রুত!)\nprint(3 in a)   # True\nprint(10 in a)  # False",
             "tip": "Set এ membership test list এর চেয়ে অনেক দ্রুত।"},

            {"name": "Dictionaries", "namebn": "ডিকশনারি",
             "content": "Dictionary হলো key-value pairs। {} দিয়ে তৈরি। Key unique হতে হবে।\n\nমূল methods: keys(), values(), items(), get()",
             "example": "student = {\n    'name': 'Rahim',\n    'age': 20,\n    'gpa': 3.85,\n    'subjects': ['Math', 'CS', 'Physics']\n}\n\n# Access\nprint(student['name'])\nprint(student.get('age', 0))  # safe access\n\n# Add/Update\nstudent['email'] = 'rahim@gmail.com'\nstudent['gpa'] = 3.90\n\n# Iterate\nfor key, value in student.items():\n    print(f'{key}: {value}')",
             "tip": "get() ব্যবহার করো — key না থাকলে KeyError হবে না।"},
        ],
        "project": {
            "name": "Student Management System",
            "namebn": "শিক্ষার্থী ব্যবস্থাপনা সিস্টেম",
            "desc": "Dictionary ও List ব্যবহার করে একটি student management system তৈরি করো।",
            "code": "# Student Management System\nstudents = {}\n\ndef add_student(roll, name, gpa):\n    students[roll] = {'name': name, 'gpa': gpa}\n    print(f'✅ {name} যোগ করা হয়েছে!')\n\ndef show_all():\n    if not students:\n        print('কোনো শিক্ষার্থী নেই।')\n        return\n    print('\\n=== শিক্ষার্থী তালিকা ===')\n    for roll, info in students.items():\n        print(f'Roll: {roll} | Name: {info[\"name\"]} | GPA: {info[\"gpa\"]}')\n\ndef find_student(roll):\n    if roll in students:\n        s = students[roll]\n        print(f'নাম: {s[\"name\"]}, GPA: {s[\"gpa\"]}')\n    else:\n        print('শিক্ষার্থী পাওয়া যায়নি!')\n\ndef top_students():\n    sorted_s = sorted(students.items(), key=lambda x: x[1]['gpa'], reverse=True)\n    print('\\n🏆 শীর্ষ শিক্ষার্থী:')\n    for roll, info in sorted_s[:3]:\n        print(f'{info[\"name\"]}: {info[\"gpa\"]}')\n\n# Demo\nadd_student(101, 'Rahim Ahmed', 3.85)\nadd_student(102, 'Nadia Islam', 3.92)\nadd_student(103, 'Karim Khan', 3.70)\n\nshow_all()\ntop_students()",
            "skills": ["Dictionary", "Lists", "Functions", "Sorting", "Lambda"]
        }
    },
    {
        "id": 6, "icon": "🔤", "color": "#ef4444", "color2": "#b91c1c",
        "title": "Strings & Regex",
        "subtitle": "টেক্সট নিয়ে কাজ করো",
        "desc": "String manipulation এবং Regular Expression দিয়ে text processing করো।",
        "xp": 700,
        "topics": [
            {"name": "String Methods", "namebn": "স্ট্রিং মেথড",
             "content": "Python এ string এর অনেক built-in method আছে।\n\nসবচেয়ে বেশি ব্যবহৃত:\nupper(), lower(), strip(), split(), join(), replace(), find(), count(), startswith(), endswith()",
             "example": "text = '  Python Master Academy  '\n\nprint(text.strip())          # spaces remove\nprint(text.upper())\nprint(text.lower())\nprint(text.strip().replace('Python', 'বাংলা'))\n\n# Split & Join\nwords = 'আম,কলা,লিচু'.split(',')\nprint(words)           # ['আম', 'কলা', 'লিচু']\nprint(' | '.join(words)) # আম | কলা | লিচু\n\n# Check\nemail = 'user@example.com'\nprint(email.endswith('.com'))  # True\nprint('@' in email)            # True",
             "tip": "strip() দিয়ে সবসময় user input পরিষ্কার করো।"},

            {"name": "String Formatting", "namebn": "স্ট্রিং ফরম্যাটিং",
             "content": "তিনটি পদ্ধতি:\n1. % formatting (পুরনো)\n2. .format() method\n3. f-string (সবচেয়ে আধুনিক ও সহজ — Python 3.6+)",
             "example": "name = 'Rahim'\nscore = 87.5\n\n# f-string (recommended)\nprint(f'নাম: {name}, স্কোর: {score:.1f}')\n\n# Formatting\nprint(f'{score:10.2f}')   # right-aligned, 2 decimals\nprint(f'{name:>10}')      # right-align text\nprint(f'{name:<10}')      # left-align text\nprint(f'{name:^10}')      # center\n\n# Multiline f-string\nreport = f'''\n=== রিপোর্ট ===\nনাম:   {name}\nস্কোর: {score}\n'''\nprint(report)",
             "tip": "f-string এ {value:.2f} দিয়ে decimal places control করো।"},

            {"name": "Regular Expressions", "namebn": "রেগুলার এক্সপ্রেশন",
             "content": "Regex দিয়ে text এ pattern search করা যায়। Python এ re module ব্যবহার করতে হয়।\n\nমূল patterns:\n. — যেকোনো character\n* — 0 বা তার বেশি\n+ — 1 বা তার বেশি\n? — 0 বা 1\n\\d — digit\n\\w — word character\n\\s — whitespace",
             "example": "import re\n\ntext = 'আমার email: rahim@gmail.com আর phone: 01712345678'\n\n# Email খোঁজো\nemail = re.search(r'[\\w.]+@[\\w.]+', text)\nif email:\n    print(f'Email: {email.group()}')\n\n# Phone number খোঁজো\nphone = re.search(r'01[3-9]\\d{8}', text)\nif phone:\n    print(f'Phone: {phone.group()}')\n\n# সব digits খোঁজো\ndigits = re.findall(r'\\d+', text)\nprint(f'Digits: {digits}')",
             "tip": "r'' (raw string) ব্যবহার করো regex pattern এ।"},
        ],
        "project": {
            "name": "Password Strength Checker",
            "namebn": "পাসওয়ার্ড শক্তি পরীক্ষক",
            "desc": "Regex দিয়ে password এর strength check করো এবং suggestions দাও।",
            "code": "# Password Strength Checker\nimport re\n\ndef check_password(password):\n    score = 0\n    feedback = []\n    \n    if len(password) >= 8:\n        score += 1\n    else:\n        feedback.append('❌ কমপক্ষে ৮ character হতে হবে')\n    \n    if re.search(r'[A-Z]', password):\n        score += 1\n    else:\n        feedback.append('❌ বড় হাতের অক্ষর (A-Z) দাও')\n    \n    if re.search(r'[a-z]', password):\n        score += 1\n    else:\n        feedback.append('❌ ছোট হাতের অক্ষর (a-z) দাও')\n    \n    if re.search(r'\\d', password):\n        score += 1\n    else:\n        feedback.append('❌ সংখ্যা (0-9) দাও')\n    \n    if re.search(r'[!@#$%^&*]', password):\n        score += 1\n    else:\n        feedback.append('❌ Special character (!@#$%) দাও')\n    \n    strengths = ['খুব দুর্বল', 'দুর্বল', 'মাঝারি', 'শক্তিশালী', 'খুব শক্তিশালী']\n    strength = strengths[min(score, 4)]\n    bar = '█' * score + '░' * (5 - score)\n    \n    print(f'\\nশক্তি: [{bar}] {strength}')\n    if feedback:\n        print('উন্নতির পরামর্শ:')\n        for f in feedback:\n            print(f'  {f}')\n    else:\n        print('✅ চমৎকার password!')\n    return score\n\npassword = input('Password দাও: ')\ncheck_password(password)",
            "skills": ["Regex", "String methods", "Functions", "Lists"]
        }
    },
    {
        "id": 7, "icon": "📁", "color": "#ec4899", "color2": "#be185d",
        "title": "File Handling",
        "subtitle": "ফাইলে ডেটা সংরক্ষণ করো",
        "desc": "Text, CSV, JSON file read ও write করো।",
        "xp": 800,
        "topics": [
            {"name": "Reading & Writing Files", "namebn": "ফাইল পড়া ও লেখা",
             "content": "Python এ open() দিয়ে file খোলা হয়।\n\nModes:\n'r' — read (default)\n'w' — write (পুরনো data মুছে)\n'a' — append (যোগ করে)\n'r+' — read & write\n\nwith statement ব্যবহার করো — automatically close হয়।",
             "example": "# File লেখো\nwith open('diary.txt', 'w', encoding='utf-8') as f:\n    f.write('আজকের দিনটি চমৎকার ছিল।\\n')\n    f.write('Python শিখলাম।\\n')\n\n# File পড়ো\nwith open('diary.txt', 'r', encoding='utf-8') as f:\n    content = f.read()\n    print(content)\n\n# Line by line পড়ো\nwith open('diary.txt', 'r', encoding='utf-8') as f:\n    for line in f:\n        print(line.strip())\n\n# Append করো\nwith open('diary.txt', 'a', encoding='utf-8') as f:\n    f.write('আরো শিখতে হবে।\\n')",
             "tip": "সবসময় with statement ব্যবহার করো — এটা automatically file close করে।"},

            {"name": "CSV Files", "namebn": "CSV ফাইল",
             "content": "CSV (Comma Separated Values) — tabular data store করার সবচেয়ে সহজ format।\n\nPython এ csv module built-in আছে।",
             "example": "import csv\n\n# CSV লেখো\nstudents = [\n    ['নাম', 'রোল', 'GPA'],\n    ['রহিম', 101, 3.85],\n    ['নাদিয়া', 102, 3.92],\n]\n\nwith open('students.csv', 'w', newline='', encoding='utf-8') as f:\n    writer = csv.writer(f)\n    writer.writerows(students)\n\n# CSV পড়ো\nwith open('students.csv', 'r', encoding='utf-8') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        print(f\"{row['নাম']}: {row['GPA']}\")",
             "tip": "DictReader ব্যবহার করলে header দিয়ে column access করা যায়।"},

            {"name": "JSON Files", "namebn": "JSON ফাইল",
             "content": "JSON (JavaScript Object Notation) — web API ও configuration এ সবচেয়ে বেশি ব্যবহৃত format।\n\njson.dump() — write\njson.load() — read\njson.dumps() — to string\njson.loads() — from string",
             "example": "import json\n\ndata = {\n    'academy': 'Python Master Academy',\n    'modules': 20,\n    'languages': ['English', 'বাংলা'],\n    'free': True\n}\n\n# JSON লেখো\nwith open('config.json', 'w', encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n\n# JSON পড়ো\nwith open('config.json', 'r', encoding='utf-8') as f:\n    loaded = json.load(f)\n    print(loaded['academy'])\n    print(loaded['languages'])",
             "tip": "ensure_ascii=False দিলে বাংলা সঠিকভাবে save হয়।"},
        ],
        "project": {
            "name": "Personal Notes Manager",
            "namebn": "ব্যক্তিগত নোটস ম্যানেজার",
            "desc": "JSON file এ notes save, read, delete করার একটি command-line application।",
            "code": "# Personal Notes Manager\nimport json\nimport os\nfrom datetime import datetime\n\nNOTES_FILE = 'notes.json'\n\ndef load_notes():\n    if os.path.exists(NOTES_FILE):\n        with open(NOTES_FILE, 'r', encoding='utf-8') as f:\n            return json.load(f)\n    return []\n\ndef save_notes(notes):\n    with open(NOTES_FILE, 'w', encoding='utf-8') as f:\n        json.dump(notes, f, ensure_ascii=False, indent=2)\n\ndef add_note(title, content):\n    notes = load_notes()\n    notes.append({\n        'id': len(notes) + 1,\n        'title': title,\n        'content': content,\n        'date': datetime.now().strftime('%Y-%m-%d %H:%M')\n    })\n    save_notes(notes)\n    print('✅ নোট সংরক্ষণ করা হয়েছে!')\n\ndef show_notes():\n    notes = load_notes()\n    if not notes:\n        print('কোনো নোট নেই।')\n        return\n    for note in notes:\n        print(f\"\\n[{note['id']}] {note['title']}\")\n        print(f\"    {note['content']}\")\n        print(f\"    📅 {note['date']}\")\n\n# Demo\nadd_note('Python শেখা', 'আজ loops শিখলাম!')\nadd_note('প্রজেক্ট আইডিয়া', 'একটি quiz app বানাবো।')\nshow_notes()",
            "skills": ["JSON", "File handling", "Functions", "datetime module"]
        }
    },
    {
        "id": 8, "icon": "🏗️", "color": "#6366f1", "color2": "#4338ca",
        "title": "Object Oriented Programming",
        "subtitle": "বাস্তব জগতের মতো code লেখো",
        "desc": "Class, Object, Inheritance দিয়ে professional code লেখো।",
        "xp": 1200,
        "topics": [
            {"name": "Classes & Objects", "namebn": "ক্লাস ও অবজেক্ট",
             "content": "Class হলো blueprint, Object হলো সেই blueprint থেকে তৈরি instance।\n\n__init__ হলো constructor — object তৈরির সময় automatically call হয়।\nself হলো object নিজে।",
             "example": "class Student:\n    def __init__(self, name, roll, gpa):\n        self.name = name\n        self.roll = roll\n        self.gpa = gpa\n    \n    def introduce(self):\n        print(f'আমি {self.name}, রোল: {self.roll}')\n    \n    def is_pass(self):\n        return self.gpa >= 2.0\n\n# Object তৈরি\ns1 = Student('রহিম', 101, 3.85)\ns2 = Student('নাদিয়া', 102, 3.92)\n\ns1.introduce()\nprint(f'পাস: {s1.is_pass()}')",
             "tip": "self সবসময় method এর প্রথম parameter হয়।"},

            {"name": "Inheritance", "namebn": "ইনহেরিটেন্স",
             "content": "Inheritance দিয়ে একটি class অন্য class এর properties পায়।\n\nParent class (Base) → Child class (Derived)\nsuper() দিয়ে parent এর method call করা যায়।",
             "example": "class Animal:\n    def __init__(self, name):\n        self.name = name\n    \n    def speak(self):\n        return '...'\n    \n    def info(self):\n        print(f'{self.name} বলে: {self.speak()}')\n\nclass Dog(Animal):\n    def speak(self):\n        return 'ঘেউ ঘেউ!'\n\nclass Cat(Animal):\n    def speak(self):\n        return 'মিয়াও!'\n\ndog = Dog('টমি')\ncat = Cat('মিনি')\n\ndog.info()\ncat.info()",
             "tip": "super().__init__() দিয়ে parent এর constructor call করো।"},

            {"name": "Encapsulation", "namebn": "এনক্যাপসুলেশন",
             "content": "Encapsulation মানে data hide করা। Private attribute: _name (convention) বা __name (name mangling)।\n\nGetter/Setter দিয়ে controlled access দেওয়া হয়।",
             "example": "class BankAccount:\n    def __init__(self, owner, balance):\n        self.owner = owner\n        self.__balance = balance  # private\n    \n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n            print(f'✅ {amount}৳ জমা হয়েছে')\n    \n    def withdraw(self, amount):\n        if amount <= self.__balance:\n            self.__balance -= amount\n            print(f'✅ {amount}৳ তোলা হয়েছে')\n        else:\n            print('❌ পর্যাপ্ত টাকা নেই')\n    \n    def get_balance(self):\n        return self.__balance\n\nacc = BankAccount('রহিম', 5000)\nacc.deposit(2000)\nacc.withdraw(1000)\nprint(f'ব্যালেন্স: {acc.get_balance()}৳')",
             "tip": "__ দিয়ে শুরু attribute সরাসরি access করা যায় না।"},
        ],
        "project": {
            "name": "Library Management System",
            "namebn": "লাইব্রেরি ব্যবস্থাপনা সিস্টেম",
            "desc": "OOP দিয়ে একটি library system তৈরি করো — book add, issue, return করা যাবে।",
            "code": "# Library Management System\nclass Book:\n    def __init__(self, title, author, isbn):\n        self.title = title\n        self.author = author\n        self.isbn = isbn\n        self.is_available = True\n    \n    def __str__(self):\n        status = '✅ পাওয়া যাচ্ছে' if self.is_available else '❌ ইস্যু করা'\n        return f'{self.title} — {self.author} [{status}]'\n\nclass Library:\n    def __init__(self, name):\n        self.name = name\n        self.books = []\n    \n    def add_book(self, book):\n        self.books.append(book)\n        print(f'📚 \"{book.title}\" যোগ করা হয়েছে!')\n    \n    def issue_book(self, isbn, member):\n        for book in self.books:\n            if book.isbn == isbn:\n                if book.is_available:\n                    book.is_available = False\n                    print(f'✅ \"{book.title}\" {member} কে দেওয়া হয়েছে।')\n                else:\n                    print('❌ বইটি এখন পাওয়া যাচ্ছে না।')\n                return\n        print('❌ বই পাওয়া যায়নি।')\n    \n    def show_books(self):\n        print(f'\\n=== {self.name} ==='),\n        for book in self.books:\n            print(f'  {book}')\n\nlib = Library('ঢাকা পাবলিক লাইব্রেরি')\nlib.add_book(Book('Python Programming', 'John Doe', 'PY001'))\nlib.add_book(Book('Data Science', 'Jane Smith', 'DS002'))\nlib.show_books()\nlib.issue_book('PY001', 'রহিম')\nlib.show_books()",
            "skills": ["Classes", "Objects", "Methods", "__str__", "Lists"]
        }
    },
    {
        "id": 9, "icon": "🗄️", "color": "#14b8a6", "color2": "#0f766e",
        "title": "Database Programming",
        "subtitle": "ডেটা স্থায়ীভাবে সংরক্ষণ করো",
        "desc": "SQLite দিয়ে database তৈরি করো এবং CRUD operations করো।",
        "xp": 1100,
        "topics": [
            {"name": "SQLite Basics", "namebn": "SQLite মূল বিষয়",
             "content": "SQLite হলো Python এর built-in database। কোনো installation দরকার নেই।\n\nমূল commands:\nCREATE TABLE — table তৈরি\nINSERT INTO — data যোগ\nSELECT — data পড়া\nUPDATE — data পরিবর্তন\nDELETE — data মুছা",
             "example": "import sqlite3\n\n# Database connect করো\nconn = sqlite3.connect('school.db')\ncursor = conn.cursor()\n\n# Table তৈরি করো\ncursor.execute('''\n    CREATE TABLE IF NOT EXISTS students (\n        id INTEGER PRIMARY KEY,\n        name TEXT NOT NULL,\n        grade REAL\n    )\n''')\n\n# Data যোগ করো\ncursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)',\n               ('রহিম', 3.85))\n\nconn.commit()\nconn.close()\nprint('✅ Database তৈরি হয়েছে!')",
             "tip": "? placeholder ব্যবহার করো — SQL injection থেকে safe থাকবে।"},

            {"name": "CRUD Operations", "namebn": "CRUD অপারেশন",
             "content": "CRUD = Create, Read, Update, Delete\n\nএই চারটি operation দিয়েই database এর সব কাজ হয়।",
             "example": "import sqlite3\n\nconn = sqlite3.connect(':memory:')  # RAM এ temp DB\ncur = conn.cursor()\n\ncur.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')\n\n# Create\ncur.execute('INSERT INTO books (title, author) VALUES (?, ?)', ('Python 101', 'রহিম'))\n\n# Read\ncur.execute('SELECT * FROM books')\nrows = cur.fetchall()\nprint('সব বই:', rows)\n\n# Update\ncur.execute('UPDATE books SET author = ? WHERE id = ?', ('করিম', 1))\n\n# Delete\n# cur.execute('DELETE FROM books WHERE id = ?', (1,))\n\nconn.commit()\nconn.close()",
             "tip": "fetchall() সব row, fetchone() শুধু প্রথম row return করে।"},
        ],
        "project": {
            "name": "Inventory Management System",
            "namebn": "ইনভেন্টরি ব্যবস্থাপনা সিস্টেম",
            "desc": "SQLite দিয়ে product inventory system — add, search, update stock করা যাবে।",
            "code": "# Inventory Management System\nimport sqlite3\n\ndef init_db():\n    conn = sqlite3.connect('inventory.db')\n    conn.execute('''\n        CREATE TABLE IF NOT EXISTS products (\n            id INTEGER PRIMARY KEY,\n            name TEXT NOT NULL,\n            price REAL,\n            stock INTEGER DEFAULT 0\n        )\n    ''')\n    conn.commit()\n    return conn\n\ndef add_product(conn, name, price, stock):\n    conn.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)',\n                 (name, price, stock))\n    conn.commit()\n    print(f'✅ {name} যোগ করা হয়েছে!')\n\ndef show_inventory(conn):\n    rows = conn.execute('SELECT * FROM products ORDER BY name').fetchall()\n    print('\\n=== ইনভেন্টরি ===')\n    print(f'{'ID':<5} {'পণ্য':<20} {'দাম':<10} {'স্টক'}')\n    print('-' * 45)\n    for row in rows:\n        print(f'{row[0]:<5} {row[1]:<20} {row[2]:<10.2f} {row[3]}')\n\ndef low_stock_alert(conn):\n    rows = conn.execute('SELECT name, stock FROM products WHERE stock < 10').fetchall()\n    if rows:\n        print('\\n⚠️  কম স্টক সতর্কতা:')\n        for name, stock in rows:\n            print(f'  {name}: {stock} টি বাকি')\n\nconn = init_db()\nadd_product(conn, 'Python বই', 350.00, 25)\nadd_product(conn, 'USB Cable', 120.00, 8)\nadd_product(conn, 'Mouse', 450.00, 5)\nshow_inventory(conn)\nlow_stock_alert(conn)\nconn.close()",
            "skills": ["SQLite", "CRUD", "Functions", "String formatting"]
        }
    },
    {
        "id": 10, "icon": "⚡", "color": "#f97316", "color2": "#c2410c",
        "title": "Advanced Python",
        "subtitle": "Professional Python লেখো",
        "desc": "Decorators, Generators, Threading — Python এর advanced features।",
        "xp": 1400,
        "topics": [
            {"name": "Decorators", "namebn": "ডেকোরেটর",
             "content": "Decorator হলো একটি function যা অন্য function কে modify করে। @ syntax দিয়ে apply করা হয়।\n\nReal-world use: logging, timing, authentication, caching",
             "example": "import time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f'⏱️ {func.__name__} চলতে লাগলো {end-start:.4f} সেকেন্ড')\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    time.sleep(0.1)\n    return 'সম্পন্ন!'\n\n@timer\ndef calculate_sum(n):\n    return sum(range(n))\n\nprint(slow_function())\nprint(calculate_sum(1000000))",
             "tip": "functools.wraps ব্যবহার করো original function এর metadata রাখতে।"},

            {"name": "Generators", "namebn": "জেনারেটর",
             "content": "Generator হলো lazy iterator — সব data একবারে memory তে রাখে না। yield keyword ব্যবহার করে।\n\nবড় data process করতে memory efficient।",
             "example": "# Regular function\ndef squares_list(n):\n    return [x**2 for x in range(n)]  # সব memory তে\n\n# Generator\ndef squares_gen(n):\n    for x in range(n):\n        yield x**2  # একটা একটা করে\n\n# Use করো\nfor sq in squares_gen(5):\n    print(sq, end=' ')\n\n# Infinite generator\ndef countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor num in countdown(5):\n    print(num, end=' ')",
             "tip": "Generator expression: (x**2 for x in range(n)) — list comprehension এর মতো কিন্তু lazy।"},

            {"name": "Multithreading", "namebn": "মাল্টিথ্রেডিং",
             "content": "Threading দিয়ে একই সময়ে multiple task চালানো যায়।\n\nI/O bound tasks এ (file, network) threading ভালো।\nCPU bound tasks এ multiprocessing ভালো।",
             "example": "import threading\nimport time\n\ndef download(site, delay):\n    print(f'⬇️ {site} download শুরু...')\n    time.sleep(delay)  # simulate download\n    print(f'✅ {site} সম্পন্ন!')\n\n# Without threading: sequential\n# download('site1.com', 2)\n# download('site2.com', 3)  # মোট ৫ সেকেন্ড\n\n# With threading: concurrent\nstart = time.time()\nt1 = threading.Thread(target=download, args=('site1.com', 2))\nt2 = threading.Thread(target=download, args=('site2.com', 3))\n\nt1.start(); t2.start()\nt1.join(); t2.join()\n\nprint(f'মোট সময়: {time.time()-start:.1f}s')",
             "tip": "join() দিলে main thread সব thread শেষ হওয়া পর্যন্ত অপেক্ষা করে।"},
        ],
        "project": {
            "name": "Task Automation Tool",
            "namebn": "টাস্ক অটোমেশন টুল",
            "desc": "Decorator ও Threading দিয়ে একটি task scheduler তৈরি করো।",
            "code": "# Task Automation Tool\nimport threading\nimport time\nfrom functools import wraps\n\ndef retry(max_attempts=3, delay=1):\n    def decorator(func):\n        @wraps(func)\n        def wrapper(*args, **kwargs):\n            for attempt in range(max_attempts):\n                try:\n                    return func(*args, **kwargs)\n                except Exception as e:\n                    print(f'❌ Attempt {attempt+1} failed: {e}')\n                    if attempt < max_attempts - 1:\n                        time.sleep(delay)\n            print('সব attempt ব্যর্থ!')\n        return wrapper\n    return decorator\n\ndef log_task(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f'🚀 শুরু: {func.__name__}')\n        result = func(*args, **kwargs)\n        print(f'✅ শেষ: {func.__name__}')\n        return result\n    return wrapper\n\n@log_task\n@retry(max_attempts=3)\ndef backup_files():\n    time.sleep(0.5)\n    print('  📁 Files backup সম্পন্ন!')\n\n@log_task\ndef send_report():\n    time.sleep(0.3)\n    print('  📧 Report পাঠানো হয়েছে!')\n\n# Parallel execution\nt1 = threading.Thread(target=backup_files)\nt2 = threading.Thread(target=send_report)\n\nt1.start(); t2.start()\nt1.join(); t2.join()\nprint('\\n🎉 সব কাজ সম্পন্ন!')",
            "skills": ["Decorators", "Threading", "functools", "Exception handling"]
        }
    },
]

# Add remaining 10 modules (11-20) as summary cards
ADVANCED_MODULES = [
    {"id":11,"icon":"🌐","color":"#3b82f6","title":"Web Development","desc":"Flask ও FastAPI দিয়ে web application ও REST API তৈরি করো।","project":"Personal Portfolio Website","xp":1500},
    {"id":12,"icon":"🤖","color":"#8b5cf6","title":"Automation","desc":"Selenium দিয়ে browser automate করো। Scripts দিয়ে repetitive tasks বন্ধ করো।","project":"Auto Form Filler","xp":1200},
    {"id":13,"icon":"🔐","color":"#ef4444","title":"Cybersecurity","desc":"Port scanner, packet analysis, network security tools তৈরি করো।","project":"Network Scanner","xp":1600},
    {"id":14,"icon":"🏠","color":"#10b981","title":"IoT with Python","desc":"Raspberry Pi ও ESP32 দিয়ে smart devices তৈরি করো।","project":"Smart Home Controller","xp":1400},
    {"id":15,"icon":"🦾","color":"#06b6d4","title":"Robotics","desc":"ROS ও Python দিয়ে robot control করো।","project":"Robot Controller Dashboard","xp":1600},
    {"id":16,"icon":"📊","color":"#f59e0b","title":"Data Science","desc":"NumPy, Pandas, Matplotlib দিয়ে data analysis করো।","project":"Sales Data Analyzer","xp":1500},
    {"id":17,"icon":"🧠","color":"#6366f1","title":"Machine Learning","desc":"Scikit-Learn দিয়ে ML models তৈরি করো।","project":"Student Performance Predictor","xp":1800},
    {"id":18,"icon":"🤯","color":"#ec4899","title":"Artificial Intelligence","desc":"TensorFlow ও PyTorch দিয়ে neural networks তৈরি করো।","project":"AI Chat Assistant","xp":2000},
    {"id":19,"icon":"👁️","color":"#14b8a6","title":"Computer Vision","desc":"OpenCV ও YOLO দিয়ে image processing করো।","project":"Object Detection System","xp":2000},
    {"id":20,"icon":"🚀","color":"#f97316","title":"Professional Track","desc":"Git, GitHub, Deployment, Freelancing, Interview Preparation।","project":"Capstone Projects (4টি)","xp":3000},
]

CERTIFICATES = [
    {"id":1,"title":"Python Fundamentals Certificate","modules":"Module 1-5","color":"#3b82f6","icon":"🎓"},
    {"id":2,"title":"Python Intermediate Certificate","modules":"Module 6-10","color":"#8b5cf6","icon":"🏅"},
    {"id":3,"title":"Python Advanced Certificate","modules":"Module 11-15","color":"#10b981","icon":"🌟"},
    {"id":4,"title":"Python Professional Certificate","modules":"Module 16-20","color":"#f59e0b","icon":"🏆"},
    {"id":5,"title":"Python Master Certificate","modules":"সম্পূর্ণ কোর্স","color":"#ef4444","icon":"👑"},
]

# ─────────────────────────────────────────────────────────────────────────────
#  HTML GENERATION
# ─────────────────────────────────────────────────────────────────────────────

def build_topic_html(topic, idx):
    example_escaped = topic['example'].replace('`', '&#96;').replace('<', '&lt;').replace('>', '&gt;')
    content_lines = topic['content'].replace('\n', '<br>')
    return f"""
    <div class="topic-card" id="topic-{idx}">
      <div class="topic-header" onclick="toggleTopic({idx})">
        <span class="topic-num">{idx+1:02d}</span>
        <div class="topic-titles">
          <span class="topic-en">{topic['name']}</span>
          <span class="topic-bn">{topic['namebn']}</span>
        </div>
        <span class="topic-arrow" id="arrow-{idx}">▼</span>
      </div>
      <div class="topic-body" id="body-{idx}" style="display:none">
        <div class="topic-content">{content_lines}</div>
        <div class="code-block"><pre>{example_escaped}</pre></div>
        <div class="tip-box">💡 <strong>টিপস:</strong> {topic['tip']}</div>
      </div>
    </div>"""

def build_project_html(project, color):
    code_escaped = project['code'].replace('<', '&lt;').replace('>', '&gt;')
    skills_html = ''.join(f'<span class="skill-tag">{s}</span>' for s in project['skills'])
    return f"""
    <div class="project-card" style="border-color:{color}44;background:linear-gradient(135deg,{color}08,transparent)">
      <div class="project-header" style="background:{color}22;border-color:{color}44">
        <div>
          <div class="project-title">🎯 {project['name']}</div>
          <div class="project-titlebn">{project['namebn']}</div>
        </div>
        <div class="project-badge" style="background:{color}">Capstone Project</div>
      </div>
      <p class="project-desc">{project['desc']}</p>
      <div class="skills-row">{skills_html}</div>
      <div class="project-code"><pre>{code_escaped}</pre></div>
    </div>"""

def build_module_html(mod):
    topics_html = ''.join(build_topic_html(t, i) for i, t in enumerate(mod['topics']))
    project_html = build_project_html(mod['project'], mod['color'])
    return f"""
    <div class="module-page" id="module-{mod['id']}" style="display:none">
      <div class="module-hero" style="background:linear-gradient(135deg,{mod['color']},{mod['color2']})">
        <a class="back-btn" onclick="showPage('courses')">← ফিরে যাও</a>
        <div class="module-hero-icon">{mod['icon']}</div>
        <div class="module-hero-num">Module {mod['id']}</div>
        <h1 class="module-hero-title">{mod['title']}</h1>
        <p class="module-hero-sub">{mod['desc']}</p>
        <div class="module-hero-stats">
          <span>📚 {len(mod['topics'])} Topics</span>
          <span>⚡ +{mod['xp']} XP</span>
          <span>🎯 1 Project</span>
        </div>
      </div>
      <div class="module-content">
        <h2 class="section-title">📖 Lessons</h2>
        <div class="topics-list">{topics_html}</div>
        <h2 class="section-title" style="margin-top:40px">🏗️ Capstone Project</h2>
        {project_html}
      </div>
    </div>"""

def build_course_card(mod):
    return f"""
    <div class="course-card" onclick="showModule({mod['id']})"
         style="--accent:{mod['color']};border-color:{mod['color']}33">
      <div class="card-icon" style="background:{mod['color']}22;border-color:{mod['color']}44">{mod['icon']}</div>
      <div class="card-num" style="color:{mod['color']}">Module {mod['id']}</div>
      <div class="card-title">{mod['title']}</div>
      <div class="card-sub">{mod['subtitle']}</div>
      <div class="card-footer">
        <span class="card-topics">📚 {len(mod['topics'])} lessons</span>
        <span class="card-xp" style="background:{mod['color']}22;color:{mod['color']}">+{mod['xp']} XP</span>
      </div>
    </div>"""

def build_advanced_card(mod):
    return f"""
    <div class="course-card advanced-card" style="--accent:{mod['color']};border-color:{mod['color']}33">
      <div class="card-icon" style="background:{mod['color']}22;border-color:{mod['color']}44">{mod['icon']}</div>
      <div class="card-num" style="color:{mod['color']}">Module {mod['id']}</div>
      <div class="card-title">{mod['title']}</div>
      <div class="card-sub">{mod['desc']}</div>
      <div class="card-footer">
        <span class="card-topics">🎯 {mod['project'][:25]}...</span>
        <span class="card-xp" style="background:{mod['color']}22;color:{mod['color']}">+{mod['xp']} XP</span>
      </div>
      <div class="coming-soon-badge">Coming Soon</div>
    </div>"""

def build_certificate_html(cert):
    return f"""
    <div class="cert-card" style="border-color:{cert['color']}44">
      <div class="cert-seal" style="background:linear-gradient(135deg,{cert['color']},{cert['color']}88)">{cert['icon']}</div>
      <div class="cert-body">
        <div class="cert-title">{cert['title']}</div>
        <div class="cert-modules">{cert['modules']}</div>
        <div class="cert-requirements">সম্পূর্ণ করলে অর্জন করবে</div>
      </div>
      <div class="cert-preview" style="border-color:{cert['color']}44">
        <div style="font-size:32px;margin-bottom:8px">{cert['icon']}</div>
        <div style="font-size:11px;color:#94a3b8;margin-bottom:4px">PYTHON MASTER ACADEMY</div>
        <div style="font-size:14px;font-weight:800;color:#e2e8f0">{cert['title']}</div>
        <div style="font-size:10px;color:#64748b;margin-top:8px">{cert['modules']}</div>
      </div>
    </div>"""

def generate_html():
    all_module_pages = ''.join(build_module_html(m) for m in MODULES)
    course_cards = ''.join(build_course_card(m) for m in MODULES)
    advanced_cards = ''.join(build_advanced_card(m) for m in ADVANCED_MODULES)
    cert_cards = ''.join(build_certificate_html(c) for c in CERTIFICATES)

    return f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Python Master Academy</title>
<style>
:root {{
  --bg: #0a0a14;
  --surface: #12121f;
  --surface2: #1a1a2e;
  --border: #ffffff0f;
  --text: #e2e8f0;
  --sub: #64748b;
  --accent: #6366f1;
}}

* {{ box-sizing:border-box; margin:0; padding:0; }}

body {{
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
}}

/* ── NAV ── */
nav {{
  position: sticky; top: 0; z-index: 100;
  background: rgba(10,10,20,0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 28px; height: 60px;
  display: flex; align-items: center; justify-content: space-between;
}}
.nav-brand {{ display:flex; align-items:center; gap:10px; cursor:pointer; }}
.nav-brand span {{ font-weight:900; font-size:16px;
  background:linear-gradient(135deg,#6366f1,#06b6d4);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}
.nav-links {{ display:flex; gap:4px; }}
.nav-btn {{
  background:transparent; border:none; color:var(--sub);
  padding:7px 14px; border-radius:8px; cursor:pointer;
  font-size:13px; font-weight:600; transition:all 0.2s;
}}
.nav-btn:hover,.nav-btn.active {{ background:#6366f133; color:#a5b4fc; }}

/* ── PAGES ── */
.page {{ display:none; max-width:1100px; margin:0 auto; padding:32px 24px; }}
.page.active {{ display:block; animation:fadeUp 0.35s ease; }}

@keyframes fadeUp {{
  from {{ opacity:0; transform:translateY(16px); }}
  to {{ opacity:1; transform:none; }}
}}

/* ── HOME HERO ── */
.hero {{
  text-align:center; padding:70px 0 50px;
}}
.hero-badge {{
  display:inline-flex; align-items:center; gap:8px;
  background:#6366f115; border:1px solid #6366f133;
  padding:7px 18px; border-radius:40px; margin-bottom:24px;
  font-size:12px; color:#a5b4fc; font-weight:600;
}}
.hero h1 {{
  font-size: clamp(38px,6vw,68px); font-weight:900; line-height:1.1;
  margin-bottom:16px; letter-spacing:-0.02em;
  background:linear-gradient(135deg,#e2e8f0 20%,#6366f1 60%,#06b6d4);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}}
.hero p {{ font-size:17px; color:var(--sub); max-width:520px; margin:0 auto 36px; line-height:1.7; }}
.hero-btns {{ display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin-bottom:56px; }}
.btn-primary {{
  background:linear-gradient(135deg,#6366f1,#8b5cf6);
  border:none; color:#fff; padding:14px 30px;
  border-radius:12px; font-size:15px; font-weight:800;
  cursor:pointer; box-shadow:0 8px 32px #6366f140;
  transition:transform 0.2s,box-shadow 0.2s;
}}
.btn-primary:hover {{ transform:translateY(-2px); box-shadow:0 14px 40px #6366f155; }}
.btn-secondary {{
  background:transparent; border:1px solid var(--border);
  color:var(--text); padding:14px 30px; border-radius:12px;
  font-size:15px; font-weight:600; cursor:pointer;
  transition:all 0.2s;
}}
.btn-secondary:hover {{ border-color:#6366f155; background:#6366f10a; }}

.hero-stats {{ display:flex; gap:48px; justify-content:center; flex-wrap:wrap; }}
.stat {{ text-align:center; }}
.stat-val {{ font-size:28px; font-weight:900; color:#e2e8f0; }}
.stat-lbl {{ font-size:12px; color:var(--sub); margin-top:3px; }}

/* ── FEATURES ── */
.features-grid {{
  display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px;
}}
.feature-card {{
  background:var(--surface); border:1px solid var(--border);
  border-radius:16px; padding:24px;
  transition:all 0.25s;
}}
.feature-card:hover {{ border-color:#6366f144; transform:translateY(-3px); }}
.feature-icon {{ font-size:32px; margin-bottom:12px; }}
.feature-title {{ font-weight:800; font-size:15px; margin-bottom:6px; }}
.feature-desc {{ color:var(--sub); font-size:13px; line-height:1.6; }}

/* ── SECTION HEADERS ── */
.section-header {{ text-align:center; margin-bottom:40px; }}
.section-header h2 {{ font-size:30px; font-weight:900; margin-bottom:8px; }}
.section-header p {{ color:var(--sub); font-size:15px; }}

/* ── COURSE CARDS ── */
.courses-grid {{
  display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:14px;
}}
.course-card {{
  background:var(--surface); border:1px solid var(--border);
  border-radius:16px; padding:20px; cursor:pointer;
  transition:all 0.25s; position:relative; overflow:hidden;
}}
.course-card:hover {{
  border-color:var(--accent); transform:translateY(-4px);
  box-shadow:0 16px 48px color-mix(in srgb, var(--accent) 20%, transparent);
}}
.advanced-card {{ cursor:default; opacity:0.65; }}
.advanced-card:hover {{ transform:none; border-color:var(--border); }}
.card-icon {{
  width:48px; height:48px; border-radius:12px;
  display:flex; align-items:center; justify-content:center;
  font-size:22px; margin-bottom:14px; border:1px solid;
}}
.card-num {{ font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px; }}
.card-title {{ font-weight:800; font-size:15px; margin-bottom:4px; line-height:1.3; }}
.card-sub {{ font-size:12px; color:var(--sub); margin-bottom:14px; }}
.card-footer {{ display:flex; align-items:center; justify-content:space-between; }}
.card-topics {{ font-size:11px; color:var(--sub); }}
.card-xp {{ font-size:11px; font-weight:700; padding:3px 8px; border-radius:20px; }}
.coming-soon-badge {{
  position:absolute; top:12px; right:12px;
  font-size:9px; font-weight:700; padding:3px 8px;
  border-radius:20px; background:#ffffff15; color:#64748b;
  text-transform:uppercase; letter-spacing:0.5px;
}}
.grid-section-title {{
  font-size:18px; font-weight:800; margin:36px 0 16px;
  color:var(--sub); text-transform:uppercase; letter-spacing:1px;
  display:flex; align-items:center; gap:10px;
}}
.grid-section-title::after {{ content:''; flex:1; height:1px; background:var(--border); }}

/* ── MODULE PAGE ── */
.module-page {{ display:none; }}
.module-hero {{
  border-radius:20px; padding:36px 32px; margin-bottom:32px;
  position:relative; overflow:hidden;
}}
.module-hero::before {{
  content:''; position:absolute; top:-50px; right:-50px;
  width:200px; height:200px; border-radius:50%;
  background:rgba(255,255,255,0.05);
}}
.back-btn {{
  display:inline-flex; align-items:center; gap:6px;
  color:rgba(255,255,255,0.8); cursor:pointer;
  font-size:13px; margin-bottom:20px; font-weight:600;
}}
.back-btn:hover {{ color:#fff; }}
.module-hero-icon {{ font-size:52px; margin-bottom:12px; display:block; }}
.module-hero-num {{
  font-size:11px; font-weight:700; text-transform:uppercase;
  letter-spacing:2px; color:rgba(255,255,255,0.7); margin-bottom:6px;
}}
.module-hero-title {{ font-size:32px; font-weight:900; color:#fff; margin-bottom:10px; }}
.module-hero-sub {{ color:rgba(255,255,255,0.8); font-size:15px; line-height:1.6; margin-bottom:20px; }}
.module-hero-stats {{ display:flex; gap:24px; flex-wrap:wrap; }}
.module-hero-stats span {{
  font-size:13px; font-weight:600; color:rgba(255,255,255,0.9);
  background:rgba(255,255,255,0.15); padding:6px 14px; border-radius:20px;
}}

.module-content {{ padding:0; }}
.section-title {{ font-size:20px; font-weight:800; margin-bottom:20px; }}

/* ── TOPICS ── */
.topics-list {{ display:flex; flex-direction:column; gap:10px; }}
.topic-card {{
  background:var(--surface); border:1px solid var(--border); border-radius:12px; overflow:hidden;
}}
.topic-header {{
  display:flex; align-items:center; gap:14px;
  padding:16px 20px; cursor:pointer;
  transition:background 0.2s;
}}
.topic-header:hover {{ background:#ffffff05; }}
.topic-num {{
  width:32px; height:32px; border-radius:8px;
  background:#6366f122; color:#a5b4fc;
  display:flex; align-items:center; justify-content:center;
  font-size:12px; font-weight:800; flex-shrink:0;
}}
.topic-titles {{ flex:1; }}
.topic-en {{ font-weight:700; font-size:14px; display:block; }}
.topic-bn {{ font-size:11px; color:var(--sub); }}
.topic-arrow {{ color:var(--sub); transition:transform 0.2s; font-size:12px; }}
.topic-arrow.open {{ transform:rotate(180deg); }}
.topic-body {{ padding:0 20px 20px; border-top:1px solid var(--border); margin-top:0; }}
.topic-content {{
  font-size:13px; line-height:1.8; color:#94a3b8;
  padding:16px 0; white-space:pre-line;
}}
.code-block {{
  background:#050814; border-radius:10px;
  border:1px solid #ffffff0a; overflow-x:auto;
  margin-bottom:12px;
}}
.code-block pre {{
  padding:16px 18px; font-family:'Courier New',monospace;
  font-size:12px; color:#a3e635; line-height:1.7;
  white-space:pre; overflow-x:auto;
}}
.tip-box {{
  background:#6366f110; border:1px solid #6366f133;
  border-radius:8px; padding:10px 14px;
  font-size:12px; color:#a5b4fc; line-height:1.6;
}}

/* ── PROJECT CARD ── */
.project-card {{
  border:1px solid; border-radius:16px; overflow:hidden;
}}
.project-header {{
  padding:20px 24px; border-bottom:1px solid;
  display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;
}}
.project-title {{ font-weight:900; font-size:18px; }}
.project-titlebn {{ font-size:13px; color:var(--sub); margin-top:2px; }}
.project-badge {{
  font-size:11px; font-weight:700; padding:5px 12px;
  border-radius:20px; color:#fff; white-space:nowrap;
}}
.project-desc {{ padding:16px 24px; font-size:14px; color:var(--sub); line-height:1.6; }}
.skills-row {{ padding:0 24px 14px; display:flex; flex-wrap:wrap; gap:6px; }}
.skill-tag {{
  font-size:11px; padding:4px 10px; border-radius:20px;
  background:#ffffff0a; color:var(--sub); border:1px solid var(--border);
}}
.project-code {{
  background:#050814; border-top:1px solid #ffffff08; overflow:auto; max-height:380px;
}}
.project-code pre {{
  padding:20px 24px; font-family:'Courier New',monospace;
  font-size:12px; color:#e2e8f0; line-height:1.7;
  white-space:pre;
}}

/* ── CERTIFICATES ── */
.certs-grid {{ display:flex; flex-direction:column; gap:16px; }}
.cert-card {{
  background:var(--surface); border:1px solid;
  border-radius:16px; overflow:hidden;
  display:grid; grid-template-columns:60px 1fr auto; align-items:center;
}}
.cert-seal {{
  width:60px; height:100%; min-height:80px;
  display:flex; align-items:center; justify-content:center;
  font-size:24px;
}}
.cert-body {{ padding:16px 20px; }}
.cert-title {{ font-weight:800; font-size:15px; margin-bottom:4px; }}
.cert-modules {{ font-size:12px; color:var(--sub); margin-bottom:4px; }}
.cert-requirements {{ font-size:11px; color:#6366f1; }}
.cert-preview {{
  margin:12px; padding:16px 20px; border-radius:10px;
  border:1px solid; text-align:center; min-width:160px;
  background:var(--surface2);
}}

/* ── SCROLLBAR ── */
::-webkit-scrollbar {{ width:5px; height:5px; }}
::-webkit-scrollbar-track {{ background:transparent; }}
::-webkit-scrollbar-thumb {{ background:#2a2a40; border-radius:3px; }}

/* ── RESPONSIVE ── */
@media(max-width:600px) {{
  nav {{ padding:0 16px; }}
  .nav-btn span {{ display:none; }}
  .hero h1 {{ font-size:34px; }}
  .module-hero {{ padding:24px 20px; }}
  .cert-card {{ grid-template-columns:50px 1fr; }}
  .cert-preview {{ display:none; }}
  .topic-body {{ padding:0 14px 14px; }}
}}
</style>
</head>
<body>

<nav>
  <div class="nav-brand" onclick="showPage('home')">
    <span style="font-size:24px">🐍</span>
    <span>Python Master Academy</span>
  </div>
  <div class="nav-links">
    <button class="nav-btn active" id="nav-home" onclick="showPage('home')">🏠 হোম</button>
    <button class="nav-btn" id="nav-courses" onclick="showPage('courses')">📚 কোর্স</button>
    <button class="nav-btn" id="nav-certs" onclick="showPage('certs')">🏆 সার্টিফিকেট</button>
  </div>
</nav>

<!-- ═══ HOME PAGE ═══ -->
<div class="page active" id="page-home">
  <div class="hero">
    <div class="hero-badge">🚀 শূন্য থেকে Python Professional</div>
    <h1>Python শিখুন।<br>সবকিছু তৈরি করুন।</h1>
    <p>সম্পূর্ণ বিনামূল্যে — Beginner থেকে Professional পর্যন্ত ২০টি Module।</p>
    <div class="hero-btns">
      <button class="btn-primary" onclick="showPage('courses')">📚 শেখা শুরু করো</button>
      <button class="btn-secondary" onclick="showPage('certs')">🏆 সার্টিফিকেট দেখো</button>
    </div>
    <div class="hero-stats">
      <div class="stat"><div class="stat-val">২০</div><div class="stat-lbl">মডিউল</div></div>
      <div class="stat"><div class="stat-val">৬৫+</div><div class="stat-lbl">Lessons</div></div>
      <div class="stat"><div class="stat-val">২০</div><div class="stat-lbl">Projects</div></div>
      <div class="stat"><div class="stat-val">৫</div><div class="stat-lbl">সার্টিফিকেট</div></div>
    </div>
  </div>

  <div class="section-header">
    <h2>কেন Python Master Academy?</h2>
    <p>একটি platform, সব কিছু</p>
  </div>
  <div class="features-grid">
    <div class="feature-card"><div class="feature-icon">🇧🇩</div><div class="feature-title">বাংলায় শেখো</div><div class="feature-desc">সব lesson বাংলায় explain করা। মাতৃভাষায় শেখা সবচেয়ে সহজ।</div></div>
    <div class="feature-card"><div class="feature-icon">📋</div><div class="feature-title">Code Examples</div><div class="feature-desc">প্রতিটি topic এ real code example সহ explanation।</div></div>
    <div class="feature-card"><div class="feature-icon">🏗️</div><div class="feature-title">Real Projects</div><div class="feature-desc">প্রতিটি module শেষে একটি real-world project।</div></div>
    <div class="feature-card"><div class="feature-icon">🏆</div><div class="feature-title">Certificate</div><div class="feature-desc">কোর্স শেষে official certificate অর্জন করো।</div></div>
    <div class="feature-card"><div class="feature-icon">💡</div><div class="feature-title">Tips & Tricks</div><div class="feature-desc">প্রতিটি lesson এ expert tips — common mistakes এড়াও।</div></div>
    <div class="feature-card"><div class="feature-icon">🚀</div><div class="feature-title">Career Ready</div><div class="feature-desc">Cybersecurity, AI, Data Science, Robotics — সব পথ খোলা।</div></div>
  </div>

  <div class="section-header" style="margin-top:56px">
    <h2>শেখার পথ</h2>
    <p>Beginner থেকে Professional পর্যন্ত</p>
  </div>
  <div class="courses-grid">
    {''.join(build_course_card(m) for m in MODULES[:6])}
  </div>
  <div style="text-align:center;margin-top:24px">
    <button class="btn-primary" onclick="showPage('courses')">সব ২০টি Module দেখো →</button>
  </div>
</div>

<!-- ═══ COURSES PAGE ═══ -->
<div class="page" id="page-courses">
  <div class="section-header">
    <h2>📚 সম্পূর্ণ কোর্স</h2>
    <p>২০টি Module — Beginner থেকে Professional</p>
  </div>

  <div class="grid-section-title">Beginner to Intermediate — Module 1–10</div>
  <div class="courses-grid">{course_cards}</div>

  <div class="grid-section-title" style="margin-top:40px">Advanced & Specialized — Module 11–20</div>
  <div class="courses-grid">{advanced_cards}</div>
</div>

<!-- ═══ CERTIFICATES PAGE ═══ -->
<div class="page" id="page-certs">
  <div class="section-header">
    <h2>🏆 সার্টিফিকেট</h2>
    <p>কোর্স সম্পূর্ণ করলে অফিশিয়াল সার্টিফিকেট অর্জন করো</p>
  </div>
  <div class="certs-grid">{cert_cards}</div>

  <div style="margin-top:40px;background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;text-align:center">
    <div style="font-size:48px;margin-bottom:12px">👑</div>
    <h3 style="font-size:20px;font-weight:900;margin-bottom:8px">Python Master Certificate</h3>
    <p style="color:var(--sub);margin-bottom:20px;line-height:1.6">সম্পূর্ণ ২০টি Module শেষ করলে এই বিশেষ সার্টিফিকেট পাবে।<br>এটি দিয়ে Freelancing, Job Application ও Portfolio তে যোগ করো।</p>
    <button class="btn-primary" onclick="showPage('courses')">এখনই শুরু করো 🚀</button>
  </div>
</div>

<!-- ═══ MODULE PAGES ═══ -->
{all_module_pages}

<script>
let currentPage = 'home';
let currentModule = null;

function showPage(page) {{
  // Hide all pages
  document.querySelectorAll('.page, .module-page').forEach(p => {{
    p.style.display = 'none';
    p.classList.remove('active');
  }});

  // Update nav
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));

  if (page === 'home') {{
    const el = document.getElementById('page-home');
    el.style.display = 'block';
    el.classList.add('active');
    document.getElementById('nav-home').classList.add('active');
  }} else if (page === 'courses') {{
    const el = document.getElementById('page-courses');
    el.style.display = 'block';
    el.classList.add('active');
    document.getElementById('nav-courses').classList.add('active');
  }} else if (page === 'certs') {{
    const el = document.getElementById('page-certs');
    el.style.display = 'block';
    el.classList.add('active');
    document.getElementById('nav-certs').classList.add('active');
  }}
  window.scrollTo({{top:0, behavior:'smooth'}});
  currentPage = page;
}}

function showModule(id) {{
  document.querySelectorAll('.page, .module-page').forEach(p => {{
    p.style.display = 'none';
    p.classList.remove('active');
  }});
  const el = document.getElementById('module-' + id);
  if (el) {{
    el.style.display = 'block';
    el.style.animation = 'fadeUp 0.35s ease';
    window.scrollTo({{top:0, behavior:'smooth'}});
  }}
}}

function toggleTopic(idx) {{
  const body = document.getElementById('body-' + idx);
  const arrow = document.getElementById('arrow-' + idx);
  if (body.style.display === 'none') {{
    body.style.display = 'block';
    arrow.classList.add('open');
  }} else {{
    body.style.display = 'none';
    arrow.classList.remove('open');
  }}
}}
</script>
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
#  SERVER
# ─────────────────────────────────────────────────────────────────────────────

class Handler(http.server.BaseHTTPRequestHandler):
    _html = None

    def do_GET(self):
        if Handler._html is None:
            Handler._html = generate_html().encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', len(Handler._html))
        self.end_headers()
        self.wfile.write(Handler._html)

    def log_message(self, fmt, *args):
        pass  # Suppress request logs


def main():
    print("=" * 52)
    print("  🐍  PYTHON MASTER ACADEMY")
    print("=" * 52)
    print(f"  ✅  Server চালু হচ্ছে...")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"  🌐  URL: {url}")
        print(f"  📚  ২০টি Module লোড হয়েছে")
        print(f"  🏆  ৫টি Certificate প্রস্তুত")
        print("=" * 52)
        print("  বন্ধ করতে Ctrl+C চাপো")
        print("=" * 52)

        # Auto-open browser after short delay
        def open_browser():
            import time
            time.sleep(0.8)
            webbrowser.open(url)

        threading.Thread(target=open_browser, daemon=True).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  👋  Python Master Academy বন্ধ হলো। ধন্যবাদ!")
            sys.exit(0)


if __name__ == "__main__":
    main()
