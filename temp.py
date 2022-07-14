fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
c = list(map(lambda f: (f-32)/1.8, fahrenheit.values()))
celsius=dict(zip(fahrenheit.keys(),c))
print(celsius)