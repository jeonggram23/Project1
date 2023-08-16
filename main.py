def add_func(n1, n2):
    return n1+n2

def minus_func(n1, n2):
    return n1 - n2



## 전역 변수부
num1, num2 = 100, 200
result = 0

## 메인 코드부
result = add_func(num1, num2)
print(num1, '+', num2, '=', result)

a = add_func(4,4)
print(a)

result = minus_func(num1, num2)
print(num1, '-', num2, '=', result)
