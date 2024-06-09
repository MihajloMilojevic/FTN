package structural.composite;

import java.util.List;

public abstract class FileSystemItem {
	protected String name;

	public String getName() {
		return name;
	}

	public abstract boolean isFile();

	public abstract void add(FileSystemItem item);

	public abstract void remove(FileSystemItem item);

	public abstract List<FileSystemItem> getList();

	public String toString() {
		if (isFile())
			return (getName());
		else
			return ("<" + getName() + ">");
	}
}
