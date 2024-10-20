"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    resultado = result[1:-1]
    return resultado

print("Resultado es: ",fn_hack_8())