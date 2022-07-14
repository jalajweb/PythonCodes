T = int(input())
for i in range(T):
    a,b = input().split()
    try:
        result = int(a)/int(b)
    except Exception as e:
        print('Error code: ', e)
    else:
        print(result)
