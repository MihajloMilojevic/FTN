package structural.proxyoverkill;

import structural.proxyoverkill.client.ClientProxy;

public class Client {

	public static void main(String[] args) {
		// sa klijentske strane
		try {
			ServerI proxy = (ServerI)new ClientProxy("localhost").lookup(ServerI.class.getName());
			
			Auto a = proxy.napraviJedan();
			System.out.println(a);
			
			System.out.println(proxy.upali(a));
			
			System.out.println(proxy.hello("pera"));
			
			System.err.println(proxy.getClass());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
