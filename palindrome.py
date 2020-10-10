def palindrome(p):
    p = p.upper().strip()
    p = p.replace(" ", "")
    p1 = p[::-1]
    p = p.upper()
    p1 = p1.upper()
    if p == p1:
        return 'É um palidrome'
    else:
        return 'Não é um palindrome'


palavra = str(input('Informe uma palavra: '))
print(palindrome(palavra))

