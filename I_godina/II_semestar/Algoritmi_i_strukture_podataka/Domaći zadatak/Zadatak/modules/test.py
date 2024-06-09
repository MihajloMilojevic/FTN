from domaci_sv_57_2023 import infix_to_postfix, calculate_postfix, calculate_infix
from tokenizer import tokenize

if __name__ == '__main__':
    while ((unos := input(">> ")) != "exit"):
        print("Postfix: ", " ".join([str(x) for x in infix_to_postfix(unos)]))
        print("Rezultat: ", calculate_postfix(infix_to_postfix(unos)))
        print("Resultat infix: ", calculate_infix(unos))
        print("Python eval: ", eval(unos.replace("^", "**")))
    