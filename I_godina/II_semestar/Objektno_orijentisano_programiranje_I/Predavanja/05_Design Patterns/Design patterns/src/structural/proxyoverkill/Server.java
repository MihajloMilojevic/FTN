package structural.proxyoverkill;

import structural.proxyoverkill.server.ServerProxyReceiver;

/** Kompleksni objekat, na serverskoj strani. Pravi ga programer na osnovu LoginServiceI interfejsa. */
public class Server extends ServerProxyReceiver implements ServerI {

	@Override
	public Auto napraviJedan() throws Exception {
		Auto a = new Auto();
		a.radi = false;
		return a;
	}
	
	@Override
	public Auto upali(Auto a) throws Exception {
		a.radi = true;
		return a;
	}
	
	public static void main(String[] args) {
		new Server();
	}

	@Override
	public String hello(String s) throws Exception {
		return "Hello, " + s;
	}
}
