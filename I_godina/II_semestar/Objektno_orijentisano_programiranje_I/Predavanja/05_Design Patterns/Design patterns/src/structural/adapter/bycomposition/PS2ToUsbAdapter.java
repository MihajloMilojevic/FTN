package structural.adapter.bycomposition;

public class PS2ToUsbAdapter implements USBTastatura {
	PS2Tastatura tastatura;

	public PS2ToUsbAdapter(PS2Tastatura tastatura) {
		this.tastatura = tastatura;
	}
	
	@Override
	public int vratiTaster() {
		return tastatura.vratiTaster();
	}

}
