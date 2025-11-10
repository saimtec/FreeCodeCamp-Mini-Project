from mean_var_std import calculate

try:
    data = [0,1,2,3,4,5,6,7,8]
    result = calculate(data)
    print(result)
except ValueError as e:
    print(e)
