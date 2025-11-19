import math

def mod_transformation(key: int, B: int) -> int:
    return key % B


def square_transformation(key: int, B: int, v: int, p: int) -> int:
    # N se računa po formuli n = logv(B) zaokruženo naviše
    n = math.ceil(math.log(B, v))
    # T se računa po formuli T = |_ p - n/2 _| (|_ x _| označava zaokruživanje x naniže)
    t = math.floor(p - n / 2)
    # Izračunaj cifre kvadrata ključa -moramo izračunati 2p-1 cifara pa koristimo zfill da dopunimo nulama na početku
    digits = list(map(int, list(str(key ** 2).zfill(2 * p -1))))
    #Centralne cifre su one čiji indeksi su u intervalu [t, t+n-1] što je isto [t: t+n) koji koristimo u pythonu za slice
    central_digits = digits[t: t + n]  # The end index (t + n) is not included in the resulting slice.
    # Spoji cifre u jedan string i pretvori ga u broj
    central_value = int("".join(list(map(str, central_digits))))
    # Konačna adresa se računa po formuli |_ T * B / v^n _| a u našem slučaju T = central_value (|_ x _| označava zaokruživanje x naniže)
    return math.floor(B / (v**p) * central_value)

def overlapping_transformation(key: int, B: int, v: int, p: int) -> int:
    # N se računa po formuli n = logv(B) zaokruženo naviše
    n = math.ceil(math.log(B, v))
    # Broj segmenata se računa kao broj pozicija p / n zaokruženo naviše
    number_of_segments = math.ceil(p / n)
    # Da bi pravilno podelili cifre ključa u segmente, prvo ga moramo dopuniti nulama na početku pa koristimo zfill
    skey = str(key).zfill(number_of_segments * n)
    # Računamo sve cifre pojedinačno
    digits = list(map(int, list(skey)))
    # Delimo cifre u segmente dužine n tako da su parni indeksi normalni a neparni indeksi obrnuti (indeksiranje počinje od 0)
    segments = [digits[i:i + n] if i % 2 == 0 else digits[i:i + n][::-1] for i in range(0, len(digits), n)]
    # Računamo vrednosti segmenata tako što ih pretvaramo u string i onda u int
    segment_values = [int("".join(map(str, segment))) for segment in segments]
    # Računamo pseudoslučajan broj T kao sumu vrednosti segmenata ali po modulu v^n
    T = sum(segment_values) % (v**n)
    return  math.floor(B / (v**n) * T )

if __name__ == "__main__":

    assert mod_transformation(37, 150) == 37
    assert square_transformation(37, 150, 10, 3) == 20
    assert overlapping_transformation(123456789, 175, 10, 9) == 99