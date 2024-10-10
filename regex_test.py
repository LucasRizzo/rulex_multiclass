import re

# pattern = r'(\d+)?\s*([<>]=?)?\s*("[\w\s-]+"|\w+)\s*([<>]=?)?\s*(\d+)?'
# pattern = r'(\d+)?\s*([<>]=?)?\s*((?:"[\w\s-]+")|(?:\'[\w\s-]+\'|\w+(?:-?\w+)*))\s*([<>]=?)?\s*(\d+)?'
pattern = r'(-?\d+(?:\.\d+)?|\w+)\s*([<>]=?)\s*(-?\d+(?:\.\d+)?|\w+)(?:\s*([<>]=?)\s*(-?\d+(?:\.\d+)?))?'

# Your input string
input_string = "0.457 <= Bilirubin"

# Match the pattern
match = re.match(pattern, input_string)

if match:

    groups = match.groups()
    
    # Using any() to check if any group is None
    # Expression does do have 5 elements. Can be value (<, <=) word, or word (<, <=) value
    if any(group is None for group in groups):

        try: # value (<, <=) word
            number1 = float(groups[0])
            op1 = groups[1]
            word = groups[2]
            op2 = None
            number2 = None
        except ValueError:
            
            try: # word (<, <=) value
                word = groups[0]
                op1 = groups[1]
                number1 = float(groups[2])
                op2 = None
                number2 = None
            except ValueError:
                raise("Expression not identified")
                exit()


    else: # value (<, <=) word (<, <=) value
        number1 = float(match.group(1)) if match.group(1) else None
        op1 = match.group(2) if match.group(2) else None
        word = match.group(3)
        op2 = match.group(4) if match.group(4) else None
        number2 = float(match.group(5)) if match.group(5) else None

    print(input_string)
    print("First number:", number1)
    print("Operator 1:", op1)
    print("Word:", word)
    print("Operator 2:", op2)
    print("Second number:", number2)
else:
    print("No match")
