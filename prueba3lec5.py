def mezclador (string_a, string_b):
    string_a_long= len(string_a)
    string_b_long = len(string_b)
    return string_a[0:2] + string_b[string_b_long-2:string_b_long]


if __name__ == '__main__':
    print(mezclador("perro","malcriado"))