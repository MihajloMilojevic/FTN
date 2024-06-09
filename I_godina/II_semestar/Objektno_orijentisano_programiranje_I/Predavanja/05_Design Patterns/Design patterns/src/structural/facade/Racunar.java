package structural.facade;

public class Racunar {
	final int BOOT_ADRESA = 1024;
	Procesor procesor = new Procesor();
	Memorija memorija = new Memorija();
	Disk     disk     = new Disk();
	
	public void start() {
		disk.zavrti();
		memorija.ucitajBootSektor(disk.vratiBootSektor());
		procesor.skociNa(BOOT_ADRESA, memorija);
	}
}
