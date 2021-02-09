import sys
sys.path.append("..")

from values.symbols import symbolsArith, symbolsMult

# Evalua si existe operacion de multiplicacion o division
def is_mult(operation):
    isMultInOp = False
    for character in operation:
        for symbol in symbolsMult:
            if character == symbol:
                isMultInOp = True
    
    return isMultInOp


# Evalua si existe operacion de suma o resta
def is_arith(operation):
    isArithInOp = False
    for character in operation:
        for symbol in symbolsArith:
            if character == symbol:
                isArithInOp = True
    
    return isArithInOp


# Hace la primera multiplicacion o division que encuentre de izquierda a derecha
def eval_mult(operation):
    i_symbol = 0

    i = 0
    for character in operation:
        for symbol in symbolsMult:
            if i_symbol == 0 and character == symbol:
                i_symbol = i
        i += 1
    
    if i_symbol != 0:
        first_number = float(operation[i_symbol - 1])
        second_number = float(operation[i_symbol + 1])

        result = 0
        if operation[i_symbol] == "*":
            result = first_number * second_number
        else:
            result = first_number / second_number
        
        operation_copy = operation.copy()

        del operation_copy[i_symbol + 1]
        del operation_copy[i_symbol]
        operation_copy[i_symbol - 1] = str(result)

        return operation_copy
    
    return operation


# Hace la primera suma o resta que encuentre de izquierda a derecha
def eval_arith(operation):
    i_symbol = 0

    i = 0
    for character in operation:
        for symbol in symbolsArith:
            if i_symbol == 0 and character == symbol:
                i_symbol = i
        i += 1
    
    if i_symbol != 0:
        first_number = float(operation[i_symbol - 1])
        second_number = float(operation[i_symbol + 1])

        result = 0
        if operation[i_symbol] == "+":
            result = first_number + second_number
        else:
            result = first_number - second_number
        
        operation_copy = operation.copy()

        del operation_copy[i_symbol + 1]
        del operation_copy[i_symbol]
        operation_copy[i_symbol - 1] = str(result)

        return operation_copy
    
    return operation
        

# Realiza todas las evaluaciones y devuelve el resultado de la operacion
def evaluate(operation):
    check_mult = True
    check_arith = True

    while check_mult:
        if is_mult(operation):
            operation = eval_mult(operation)
        else:
            check_mult = False
    
    while check_arith:
        if is_arith(operation):
            operation = eval_arith(operation)
        else:
            check_arith = False
    
    return operation