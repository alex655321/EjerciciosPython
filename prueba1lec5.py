if __name__ == '__main__':
    a = "notar"
    b = a.replace("v", "n")
    print(b)

    a = "oso pardo"
    b = a.strip("o")
    print(b)

    "ANIMALES".upper()

    a = "Barcelona 92"
    print(a[1])

    s = "Acaso hubo buhos aca"
    t = s[2:9] + s[0:1]
    print(t)

    s = input("Ingresa una palabra: ")
    resultado = ""
    i = 0
    while i < len(s):
        resultado = resultado + s[len(s) - i - 1]
        i = i + 1
    print(resultado)

    s = "hola que tal"
    print (len (s))

