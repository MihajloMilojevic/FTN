package behavioral.memento;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class TextArea {
	private List <String> lines;
	
	private Stack<Memento> undoBuffer;
	
	public TextArea() {
		lines = new ArrayList<String>();
		undoBuffer = new Stack<Memento>();
	}
	
	public void addText(String text) {
		undoBuffer.push(createMemento());
		lines.add(text);
	}
	
	public Memento createMemento() {
		return new Memento(lines);
	}

	
	public void undo() {
		Memento memento = undoBuffer.pop();
		this.lines = memento.getState();
	}
	
	public void showText() {
		System.out.println("======================================");
		for (String line : lines) 
			System.out.println(line);
		System.out.println("======================================");
		
		for (int i = 0; i < undoBuffer.size(); i++)
			System.out.println(undoBuffer.elementAt(i));
			
	}
}
