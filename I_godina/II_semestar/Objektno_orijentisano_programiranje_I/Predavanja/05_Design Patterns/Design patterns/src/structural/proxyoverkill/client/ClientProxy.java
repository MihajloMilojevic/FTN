package structural.proxyoverkill.client;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.net.Socket;

/** Klijentski deo Proxy mehanizma.
 *  Koristi pogodnost java.lang.reflect.Proxy klase, koja može da 
 *  implementira proizvoljan interfejs, pa i Remote interfejs, zadat imenom.
 */
public class ClientProxy {
	private String addr;
	public ClientProxy(String addr) {
		this.addr = addr;
	}
	public Object lookup(String interfaceName) throws IllegalArgumentException, ClassNotFoundException {
		InvocationHandler handler = new InvocationHandler() {
			public Object invoke(Object proxy, Method mm, Object[] args) throws Throwable {
				Socket socket = new Socket(addr, 9000);
				// ako je na serveru prvo napravljen ObjectInputStream, onda ovde
				// ide prvo ObjectOutputStream
				ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
				ObjectInputStream in = new ObjectInputStream(socket.getInputStream());
				// pošaljemo ime metode koju æemo izvršiti na serveru
				out.writeObject(mm.getName());
				if (args != null) {
					// pošaljemo broj argumenata metode kao Integer
					out.writeObject(args.length);
					// pošaljemo tipove argumenata u obliku stringa
					for (Object o : args) {
						out.writeObject(o.getClass().getName());
					}
					// pošaljemo same argumente kao objekte
					for (Object o : args) {
						out.writeObject(o);
					}
				} else {
					// ako nema argumenata, pošaljemo nula za broj argumenata metode
					out.writeObject(0);
				}
				out.flush();
				// saèekamo odgovor u kojem se nalazi rezultat rada
				Object res = in.readObject();
				in.close();
				out.close();
				socket.close();

				return res;
			}
		};

		Object proxy = Proxy.newProxyInstance(ClientProxy.this.getClass().getClassLoader(),
				new Class[] { Class.forName(interfaceName) }, handler);
		return proxy;
	}

}
