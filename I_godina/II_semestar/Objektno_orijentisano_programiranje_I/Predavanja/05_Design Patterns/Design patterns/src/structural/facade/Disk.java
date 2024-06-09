package structural.facade;

class Disk {
	public void zavrti() {
		System.out.println("HD: zavrtio disk");
	}

	public byte[] vratiBootSektor() {
		System.out.println("HD: boot sektor pronadjen i dobavljen");
		return new byte[512];
	}
}
