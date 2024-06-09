package structural.proxy.server;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

import structural.proxy.ServerI;

public class ServerProxyReceiver {

	public ServerProxyReceiver() {
		// sa serverske strane
		ServerSocket ss;
		try {
			ss = new ServerSocket(9000);
			while (true) {
				System.out.println("SERVER CEKA KLIJENTA");
				Socket s = ss.accept();
				executeCommand(s);
				s.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static final int LOGIN = 0;

	public void executeCommand(Socket socket) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()), true);
		System.out.println("SERVER CEKA KOMANDU");
		String commandId = in.readLine();
		System.out.println("SERVER PRIMIO KOMANDU: " + commandId);

		switch (Integer.parseInt(commandId)) {
		case LOGIN:
			out.println(((ServerI) this).login(in.readLine(), in.readLine()));
		default:
			out.println("null");
		}
		in.close();
		out.close();
	}
}
