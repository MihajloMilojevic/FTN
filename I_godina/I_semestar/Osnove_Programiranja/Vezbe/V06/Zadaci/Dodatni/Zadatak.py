from Vrh import Vrh


class Zadatak:
    def __init__(self) -> None:
        self.vrhovi: list[Vrh] = []
        with open("mountains.txt", "r") as fajl:
            for linija in fajl.readlines():
                self.vrhovi.append(Vrh.iz_fajla(linija))

    def podzatak_a(self, drzava: str, lista: list[Vrh] = None) -> list[Vrh]:
        rez: list[Vrh] = []
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            drzave = [d.lower() for d in vrh.drzave]
            if drzava.lower() in drzave:
                rez.append(vrh)
        return rez

    def podzatak_b(self, lista: list[Vrh] = None) -> list[Vrh]:
        rez: list[Vrh] = []
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            if len(vrh.drzave) == 2 and 7700 < vrh.visina_metri < 8100:
                rez.append(vrh)
        return rez
    
    def podzatak_c(self, drzava: str, lista: list[Vrh] = None) -> list[Vrh]:
        rez: list[Vrh] = []
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            drzave = [d.lower() for d in vrh.drzave]
            if drzava.lower() in drzave and vrh.visina_metri > 6000:
                rez.append(vrh)
        return rez
    
    def podzatak_d(self, lista: list[Vrh] = None) -> dict[str, int]:
        rez: dict[str, int] = {}
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            if vrh.visina_metri <= 6000:
                continue
            for drzava in vrh.drzave:
                if drzava not in rez:
                    rez[drzava] = 0
                rez[drzava] += 1
        return rez

    def podzatak_e(self, venac: str, lista: list[Vrh] = None) -> list[Vrh]:
        rez: list[Vrh] = []
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            if venac.lower() == vrh.planina.lower():
                rez.append(vrh)
        return rez
    
    def podzatak_f_1(self, lista: list[Vrh] = None) -> list[Vrh]:
        rez: list[Vrh] = []
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            if len(vrh.drzave) > 1:
                rez.append(vrh)
        return rez
    
    def podzatak_f_2(self, lista: list[Vrh] = None) -> list[str]:
        mapa: dict[str, int] = {}
        if lista is None:
            lista = self.vrhovi
        for vrh in lista:
            if vrh.planina not in mapa:
                mapa[vrh.planina] = 0
            mapa[vrh.planina] += 1
        max_venac = [mapa.keys()[0]]
        for key in mapa.keys():
            if mapa[key] > mapa[max_venac[0]]:
                max_venac = [key]
            elif mapa[key] == mapa[max_venac[0]]:
                max_venac.append(key)
        return max_venac