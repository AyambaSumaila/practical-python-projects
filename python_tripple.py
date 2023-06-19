def is_pyth_tripp(a, b, c):
    num_ab=a**2+b**2
    num_c=c**2
    if num_ab==num_c:
        print(f"The combination of {a}, {b}, {c} support pyth law")
    else:
        print(f"The combination of {a}, {b}, {c} does not support pyth law")

is_pyth_tripp(4, 3, 5)
is_pyth_tripp(5, 4, 3)
