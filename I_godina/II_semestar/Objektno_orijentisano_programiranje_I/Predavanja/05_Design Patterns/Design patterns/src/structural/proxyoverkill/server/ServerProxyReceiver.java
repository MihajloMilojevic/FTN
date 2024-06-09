package structural.proxyoverkill.server;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Method;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Serverski deo Proxy mehanizma. Prima komande po protokolu:
 * <ol>
 * <li>ime metode kao String</li>
 * <li>broj argumenata kao int</li>
 * <li>[klase argumenata kao String]</li> 
 * <li>[argumenti kao objekti]</li>
 * </ol>
 * 
 * Vraæa rezultat izvršenja kao objekat.
 *
 */
public class ServerProxyReceiver {

	public static final int LOGIN = 0;

	public ServerProxyReceiver() {
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
	
	/**
	 * Izvršava proizvoljnu metodu zadatu sa klijetske strane Proxy mehanizma.
	 * @param socket socket preko kojeg ide komunikacija sa klijentom
	 * @throws Exception ako nešto ne valja
	 */
	public void executeCommand(Socket socket) throws Exception {
		// ako je na klijentu prvo napravljen ObjectOutputStream, onda ovde
		// ide prvo ObjectInputStream
		ObjectInputStream  in = new ObjectInputStream(
				socket.getInputStream());
		ObjectOutputStream out = new ObjectOutputStream(
				socket.getOutputStream());
		System.out.println("SERVER CEKA KOMANDU");
		String commandId = (String)in.readObject();
		System.err.println("SERVER PRIMIO KOMANDU: " + commandId);
		int argsLen = (Integer)in.readObject();
		System.err.println("Broj argumenata: " + argsLen);
		Class<?>[] clazzez = new Class[argsLen];
		for (int i = 0; i < argsLen; i++) {
			clazzez[i] = Class.forName((String)in.readObject());
		}
		Object[] args = new Object[argsLen];
		for (int i = 0; i < argsLen; i++) {
			args[i] = in.readObject();
			System.err.println(args[i] + ", tipa: " + clazzez[i] +  (i < (argsLen-1)?", ":""));
		}
		
		Method mm = this.getClass().getDeclaredMethod(commandId, clazzez);
		out.writeObject(mm.invoke(this, args));
		out.flush();
		
		in.close();
		out.close();
		socket.close();
	}
}
