package structural.composite;

import java.util.ArrayList;
import java.util.List;

public class DirectoryItem extends FileSystemItem {

	List<FileSystemItem> firstLevelChildren = new ArrayList<FileSystemItem>(); 
	
	public DirectoryItem(String name) {
		this.name = name;
	}

	@Override
	public boolean isFile() {
		return false;
	}
	
	@Override
	public void add(FileSystemItem item) {
		firstLevelChildren.add(item);
	}

	@Override
	public void remove(FileSystemItem item) {
		firstLevelChildren.remove(item);
	}

	@Override
	public List<FileSystemItem> getList() {
		return firstLevelChildren;
	}
	
}
