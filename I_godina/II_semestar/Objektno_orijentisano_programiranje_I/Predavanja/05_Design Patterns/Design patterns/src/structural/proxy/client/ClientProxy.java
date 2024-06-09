package structural.proxy.client;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

import structural.proxy.ServerI;
import structural.proxy.server.ServerProxyReceiver;

/** Masinski generisana klasa na osnovu LoginService interfejsa. */
public class ClientProxy implements ServerI {
	
	private String addr;

	public ClientProxy(String addr) {
		this.addr = addr;
	}
	
	@Override
	public boolean login(String username, String password) throws Exception {
		Socket socket = new Socket(addr, 9000);
		BufferedReader in = new BufferedReader(new InputStreamReader(
				socket.getInputStream()));
		PrintWriter out = new PrintWriter(new OutputStreamWriter(
				socket.getOutputStream()), true);

		System.out.println("LOCAL LOGIN, USERNAME: " + username
				+ ", PASSWORD: " + password);
		
		String command = "" + ServerProxyReceiver.LOGIN;
		out.println(command);
		System.out.println("POSLAO KOMANDU: " + command);
		out.println(username);
		System.out.println("POSLAO USERNAME: " + username);
		out.println(password);
		System.out.println("POSLAO PASSWORD: " + password + ", CEKAM ODGOVOR");

		String res = in.readLine();
		System.out.println("DOBIO ODGOVOR: " + res);

		in.close();
		out.close();
		socket.close();
		return Boolean.parseBoolean(res);
	}

}
