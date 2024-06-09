package structural.composite;

import java.util.List;

public class FileItem extends FileSystemItem {

	public FileItem(String name) {
		this.name = name;
	}

	@Override
	public boolean isFile() {
		return true;
	}
	
	@Override
	public void add(FileSystemItem item) {
	}

	@Override
	public void remove(FileSystemItem item) {
	}

	@Override
	public List<FileSystemItem> getList() {
		return null;
	}
}
