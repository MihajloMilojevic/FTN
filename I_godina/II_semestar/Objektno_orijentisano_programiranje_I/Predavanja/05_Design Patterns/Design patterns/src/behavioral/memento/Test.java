package behavioral.memento;

public class Test {

	public static void main(String[] args) {
		TextArea textEditor = new TextArea();
		
		textEditor.addText("danas");
		textEditor.addText("sam");
		textEditor.addText("naucio");
		textEditor.addText("programski");
		textEditor.addText("jezik");
		textEditor.addText("Java");
		textEditor.showText();
		textEditor.undo();
		textEditor.showText();
		textEditor.undo();		
		textEditor.showText();
		
	}

}
