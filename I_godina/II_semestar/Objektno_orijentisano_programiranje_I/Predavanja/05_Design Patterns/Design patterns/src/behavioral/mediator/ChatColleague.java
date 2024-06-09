package behavioral.mediator;

public class ChatColleague implements Colleague {

	public String name;
	private ChatMediator mediator;

	public ChatColleague(String name, ChatMediator mediator) {
		this.name = name;
		this.mediator = mediator;
		this.mediator.chatColleagues.add(this);
		
	}
	
	@Override
	public void sendMessage(String message) {
		mediator.sendMessageToColleagues(message, name);

	}

	@Override
	public void receiveMessage(String message, String senderName) {
		System.out.println(name + " je primio poruku od: " + senderName + ", a ona glasi: " + message);
	}

}
