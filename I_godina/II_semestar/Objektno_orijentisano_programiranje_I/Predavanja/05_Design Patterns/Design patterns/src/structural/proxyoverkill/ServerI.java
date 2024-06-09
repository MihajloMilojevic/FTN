package structural.proxyoverkill;

/**
 * Biznis logika nabrojana ovde. Serverski objekat ovo implementira.
 * Ovo je Remote interfejs.
 *
 */
public interface ServerI {
	public Auto napraviJedan() throws Exception;
	
	public Auto upali(Auto a) throws Exception;
	
	public String hello(String s) throws Exception;
}
