def getAttributes(expression):
    expression = expression.split("(")[1:] # Remove the first '(' after the predicate
    expression = "(".join(expression) 
    expression = expression.split(")")[:-1] # Remove the last ')' after the last attribute
    expression = ")".join(expression)
    attributes = expression.split(',')
    return attributes

def getPredicate(expression):
    return expression.split("(")[0]

def isConstant(char):
    return char.isupper() and len(char) == 1

def isVariable(char):
    return char.islower() and len(char) == 1

def substitute(exp, old, new):
    attributes = getAttributes(exp)
    predicate = getPredicate(exp)
    for index, val in enumerate(attributes):
        if val == old:
            attributes[index] = new
    return predicate + "(" + ",".join(attributes) + ")"

def apply(exp, substitutions):
    for substitution in substitutions:
        new, old = substitution  
        exp = substitute(exp, old, new)
    return exp

def checkOccurs(var, exp):
    if exp.find(var) == -1:
        return False
    return True

def getFirstAttribute(expression):
    attributes = getAttributes(expression)
    return attributes[0]

def getRemaining(expression):
    predicate = getPredicate(expression)
    attributes = getAttributes(expression)
    newExpression = predicate + "(" + ",".join(attributes[1:]) + ")"
    return newExpression

def unify(exp1, exp2):
    if exp1 == exp2:
        return []
    elif isConstant(exp1) and isConstant(exp2):
        if exp1 != exp2:
            print(f"{exp1} and {exp2} are constants. Cannot be unified")
            return []
    elif isConstant(exp1):
        return [(exp1, exp2)]
    elif isConstant(exp2):
        return [(exp2, exp1)]
    elif isVariable(exp1):
        return [(exp2, exp1)] if not checkOccurs(exp1, exp2) else []
    elif isVariable(exp2):
        return [(exp1, exp2)] if not checkOccurs(exp2, exp1) else []
    elif getPredicate(exp1) != getPredicate(exp2):
        print(f"Predicates {getPredicate(exp1)} and {getPredicate(exp2)} do not match. Cannot be unified")
        return []
    elif len(getAttributes(exp1)) != len(getAttributes(exp2)):
        print(f"Length of attributes {len(getAttributes(exp1))} and {len(getAttributes(exp2))} do not match. Cannot be unified")
        return []

    # Unify first attributes
    firstAttr1 = getFirstAttribute(exp1)
    firstAttr2 = getFirstAttribute(exp2)
    initialSubstitution = unify(firstAttr1, firstAttr2)
    if not initialSubstitution:
        return []
    if len(getAttributes(exp1)) == 1:
        return initialSubstitution

    remainingAttr1 = getRemaining(exp1)
    remainingAttr2 = getRemaining(exp2)
    if initialSubstitution != []:
        # Check if there's "nested" unification. eg. [x, y] and [y, z] in the other attributes
        remainingAttr1 = apply(remainingAttr1, initialSubstitution)
        remainingAttr2 = apply(remainingAttr2, initialSubstitution)
    # Recursively unify other attributes
    remainingSubstitution = unify(remainingAttr1, remainingAttr2)
    if not remainingSubstitution:
        return []

    return initialSubstitution + remainingSubstitution

exp1 = input("Enter first expression:\n")
exp2 = input("Enter second expression:\n")

substitutions = unify(exp1, exp2)

print("Substitutions:")
print([' / '.join(substitution) for substitution in substitutions])
