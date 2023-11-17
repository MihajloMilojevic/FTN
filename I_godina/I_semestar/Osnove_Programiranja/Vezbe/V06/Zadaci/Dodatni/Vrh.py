
class Vrh:
    def __init__(self, ime: str, visina_metri: int, visina_stope: int, planina: str, drzave: list[str]) -> None:
        self.ime = ime
        self.visina_metri = visina_metri
        self.visina_stope = visina_stope
        self.planina = planina
        self.drzave = drzave
    @staticmethod
    def iz_fajla(linija: str) -> 'Vrh':
        delovi = linija.replace("\n", "").split("|")
        return Vrh(delovi[0], int(delovi[1]), int(delovi[2]), delovi[3], (delovi[4].split("/") if len(delovi) > 4 else []))
    
    def __str__(self) -> str:
        return f"Ime: {self.ime}; Visina(m): {self.visina_metri}; Visina(ft): {self.visina_stope}; Venac: {self.planina}; Drzave: {', '.join(self.drzave)}"
    