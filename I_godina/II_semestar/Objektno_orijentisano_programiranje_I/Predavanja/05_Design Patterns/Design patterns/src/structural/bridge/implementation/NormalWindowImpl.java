package structural.bridge.implementation;

public class NormalWindowImpl extends WindowImpl {

	@Override
	public void drawSurface() {
		System.out.println("drawRect() - Normal window implementation");
	}

	@Override
	public void drawTitleBar() {
		System.out.println("drawTitleBar() - Normal window implementation");
	}

}
