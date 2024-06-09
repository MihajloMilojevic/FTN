package structural.proxy;

import structural.proxy.server.ServerProxyReceiver;

/** Kompleksni objekat, na serverskoj strani. Pravi ga programer na osnovu LoginService interfejsa. */
public class Server extends ServerProxyReceiver implements ServerI {

	@Override
	public boolean login(String username, String password)  throws Exception {
		System.out.println("REMOTE LOGIN, USERNAME: " + username + ", PASSWORD: " + password);
		if (username.equals("pera") && password.equals("pera"))
			return true;
		else
			return false;
	}
	
	public static void main(String[] args) {
		new Server();
	}

}
