package behavioral.mediator;

public interface Colleague {
	public void sendMessage(String message);
	public void receiveMessage(String message, String senderName);
}
