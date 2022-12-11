var = 1

def foo():
    global var
    var = 0
    return var

print(foo())
print(var)