package structural.bridge.implementation;

public class FancyWindowImpl extends WindowImpl {

	@Override
	public void drawSurface() {
		System.out.println("drawRect() - Fancy window implementation");
	}

	@Override
	public void drawTitleBar() {
		System.out.println("drawTitleBar() - Fancy window implementation");
	}

}
