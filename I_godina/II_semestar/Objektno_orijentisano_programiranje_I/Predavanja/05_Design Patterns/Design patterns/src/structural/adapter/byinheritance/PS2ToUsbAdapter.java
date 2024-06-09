package structural.adapter.byinheritance;

public class PS2ToUsbAdapter extends PS2Tastatura implements USBTastatura {

	@Override
	public int vratiTaster() {
		return super.vratiTaster();
	}

}
