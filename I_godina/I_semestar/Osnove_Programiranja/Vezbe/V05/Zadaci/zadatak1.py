import math

def sqrt_eq(a: float, b: float, c: float) -> tuple[bool, float, float]:
    d = b**2 - 4*a*c
    if(d < 0):
        return True, 0, 0
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    return False, root1, root2

def main():
    print("Program racuna resenja kvadratne jednacine oblika ax^2 + bx + c = 0")
    a = float(input("Unesi a: "))
    b = float(input("Unesi b: "))
    c = float(input("Unesi c: "))

    if a == 0:
        return print("Uneta jednacina nije kvadratna")
    complex_roots, r1, r2 = sqrt_eq(a, b, c)
    if complex_roots:
        return print("Jednacina nema realnih resenja")
    if r1 == r2:
        return print(f"Jednacina ima samo jedna koren i to je {round(r1, 2)}")
    print (f"Koreni jednacine su: x1 = {round(r1, 2)} x2 = {round(r2, 2)}")


if __name__ == "__main__":
    main()