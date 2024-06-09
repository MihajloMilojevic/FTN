package behavioral.obsever;

public interface Observable {
	public void register(Observer observer);
	public void unregister(Observer observer);
}
