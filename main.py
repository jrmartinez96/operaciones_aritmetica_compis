import sys
from values.digits import digits
from methods.tokenization import tokenization
from methods.evaluate import evaluate
import re

operation = ""
good_input = False

while not good_input:
    operation = input("Enter the arithmetic operation: ")
    operation = operation.replace(" ", "")
    match = re.fullmatch("(([0-9])+[\/\+\-\*])+([0-9])", operation)
    if match != None:
        good_input = True
    else:
        if operation == "exit":
            sys.exit()
        else:
            print("Not a well written operation")

tokens = tokenization(operation)
ev = evaluate(tokens)
print(ev[0])