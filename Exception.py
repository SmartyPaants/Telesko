a = 10
b = 0
try:
    print('Resource Open')
    print(a / b)

except Exception:
    print('Cannot Divide by Zero')

finally:
    print('Resource Closed')