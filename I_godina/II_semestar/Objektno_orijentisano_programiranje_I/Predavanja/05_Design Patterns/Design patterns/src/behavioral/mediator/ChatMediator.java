package behavioral.mediator;

import java.util.ArrayList;
import java.util.List;

public class ChatMediator implements Mediator {

	List<ChatColleague> chatColleagues;
	
	public ChatMediator() {
		 chatColleagues = new ArrayList<ChatColleague>();
	}
	@Override
	public void sendMessageToColleagues(String message, String senderName) {
		for (ChatColleague cc : chatColleagues)
			if (!cc.name.equals(senderName))
				cc.receiveMessage(message, senderName);
	}

}
