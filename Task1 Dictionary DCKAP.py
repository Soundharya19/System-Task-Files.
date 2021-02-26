var_and_values = input().split(",")

var_and_values = dict((key.strip(), value.strip()) for key, value in (element.split('-') for element in var_and_values))


var = var_and_values.keys()

variables=list()

for key in var:
    variables.append(key)


val = var_and_values.values()

values=list()

for value in val:
    values.append(value)


expression = input()

exp=""

def ex_eval(expression):
    if 'or' in expression:
        expression = expression.split('or')
        operator = 'or'
    else:
        expression = expression.split('and')
        operator = 'and'
    if operator == 'or':
        if expression[0].strip() in variables:
            return expression[0].strip()
        return expression[1].strip()
    elif operator == 'and':
        return expression[0].strip()+" "+operator+" "+expression[1].strip()

def evl(operand1, operator, operand2):
    if operator == 'or':
        if operand1 in values:
            return operand1
        return operand2
    elif operator == 'and':
        return operand1+operand2

def extract(index):
    exp=""
    index= int(index)
    while expression[index] != ')' and index < len(expression):
        exp += expression[index]
        index+=1
    return ex_eval(exp[1:index])

for index in range(len(expression)):
    if expression[index] == ' ':
        continue
    elif expression[index] == '(':
        exp = extract(index) 
        
        expression = expression.replace(expression[expression.find('('):expression.find(')')+1], exp) # replace the expression inside the parenthesis
        break


op="" 
index=1

expression = expression.split(" ")

op += var_and_values.get(expression[0], "")


while index < len(expression):
    op = evl(op, expression[index], var_and_values.get(expression[index+1], "")) 
    index+=2
print(op)
