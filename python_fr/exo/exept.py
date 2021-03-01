a=5
b=2

try:
    result = (a/b)
except ZeroDivisionError:
    print("division par 0 impossible")
except:
    print("division impossible")
#else s'execute si le try est bon
else:
    print(result)
#finally s'execute de toute facon
finally:
    print("fin du bloc")