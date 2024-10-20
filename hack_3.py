"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    result = result.capitalize()
    return result

print("Resultado es: ",fn_hack_3())