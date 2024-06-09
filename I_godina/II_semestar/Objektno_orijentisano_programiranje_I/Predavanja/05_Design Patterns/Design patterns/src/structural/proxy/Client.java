package structural.proxy;

import structural.proxy.client.ClientProxy;

public class Client {

	public static void main(String[] args) {
		// sa klijentske strane
		try {
			ServerI proxy = new ClientProxy("localhost");
			System.err.println(proxy.login("pera", "pera"));
			System.err.println(proxy.login("mika", "mika"));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
