# Copyright (c) UCYT5040
# minlang - A minimal language
code = input() # Cahnge if you want
output = ""
currentValue = ord("0")
vars = {"?":"1"}
outputNext = False
getNext = False
setNext = False
valNext = False
appendNext = False
for i in code:
  if valNext:
    currentValue = ord(i)
    valNext = False
    continue
  if appendNext:
    currentValue += ord(i)
    appendNext = False
    continue
  if getNext:
    currentValue = ord(vars[i])
    getNext = False
    continue
  if outputNext:
    output += chr(i)
    outputNext = False
    continue
  if setNext:
    vars[i] = chr(currentValue)
    setNext = False
    continue
  if i == "e": # Sets the current value to the next character
    valNext = True
  if i == "a": # Adds the next character to the current value
    appendNext = True
  if i == "p": # Print current value
    output += chr(currentValue)
  if i == "g": # Get the value of a variable
    getNext = True
  if i == "v": # Set a variable
    setNext = True
print(output)
