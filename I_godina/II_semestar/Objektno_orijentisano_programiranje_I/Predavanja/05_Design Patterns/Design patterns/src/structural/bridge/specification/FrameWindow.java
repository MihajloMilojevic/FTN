package structural.bridge.specification;

import structural.bridge.implementation.WindowImpl;

public class FrameWindow extends Window {
	
	public FrameWindow(WindowImpl impl) {
		this.impl = impl;
	}
	
	@Override
	public void drawWindow() {
		System.out.println("Frame Window with title bar");
		impl.drawSurface();
		impl.drawTitleBar();
	}

}
