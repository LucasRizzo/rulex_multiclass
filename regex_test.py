import re

# pattern = r'(\d+)?\s*([<>]=?)?\s*("[\w\s-]+"|\w+)\s*([<>]=?)?\s*(\d+)?'
# pattern = r'(\d+)?\s*([<>]=?)?\s*((?:"[\w\s-]+")|(?:\'[\w\s-]+\'|\w+(?:-?\w+)*))\s*([<>]=?)?\s*(\d+)?'
pattern = r'(-?\d+)?\s*([<>]=?)?\s*((?:"[\w\s-]+")|(?:\'[\w\s-]+\'|\w+(?:-?\w+)*))\s*([<>]=?)?\s*(-?\d+)?'

# Your input string
input_string = "-10 <= relationship <= -2909"

# Match the pattern
match = re.match(pattern, input_string)

if match:
    number1 = int(match.group(1)) if match.group(1) else None
    op1 = match.group(2) if match.group(2) else None
    word = match.group(3)
    op2 = match.group(4) if match.group(4) else None
    number2 = int(match.group(5)) if match.group(5) else None

    print(input_string)
    print("First number:", number1)
    print("Operator 1:", op1)
    print("Word:", word)
    print("Operator 2:", op2)
    print("Second number:", number2)
else:
    print("No match")
