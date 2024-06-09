package behavioral.mediator;

public class Test {

	public static void main(String[] args) {
		ChatMediator chatMediator = new ChatMediator();
		ChatColleague pera = new ChatColleague("pera", chatMediator);
		ChatColleague mika = new ChatColleague("mika", chatMediator);
		ChatColleague djura = new ChatColleague("djura", chatMediator);
		
		pera.sendMessage("ovo je poruka od pere");
		mika.sendMessage("ovo je poruka od mike");
		djura.sendMessage("ovo je poruka od djure");
	}

}
