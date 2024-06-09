package structural.bridge.specification;

import structural.bridge.implementation.WindowImpl;

public class SplashWindow extends Window {

	public SplashWindow(WindowImpl impl) {
		this.impl = impl;
	}
	
	@Override
	public void drawWindow() {
		System.out.println("Splash Window - no title bar");
		impl.drawSurface();
	}

}
