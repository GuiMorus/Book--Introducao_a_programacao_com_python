# Defina uma função recursiva que calcule o maior divisor comum(M.D.C) entre dois números
# a e b, em que a > b
#
# mdc(a, b) = |a                        b = 0
#             |mdc(b, a - b[a / b])     a > b
# em que a - b [a / b] pode ser escrito em Python como? a % b.

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


num1 = 32
num2 = 24
print(f"O MDC entre {num1} e {num2} = {mdc(num1, num2)}")
