package structural.bridge.specification;

import structural.bridge.implementation.WindowImpl;

public abstract class Window {
	protected WindowImpl impl;
	public abstract void drawWindow();
}
