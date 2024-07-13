package vezbe_02_json.zadaci;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonAutoDetect(fieldVisibility = Visibility.ANY)
@JsonIgnoreProperties(ignoreUnknown = true)
public class Tweet {
	private String text;
	private String id_str;
	private int feel;
	
	public String getText() {
		return text;
	}
	public void setText(String text) {
		this.text = text;
	}
	public String getId_str() {
		return id_str;
	}
	public void setId_str(String id_str) {
		this.id_str = id_str;
	}
	public int getFeel() {
		return feel;
	}
	public void setFeel(int feel) {
		this.feel = feel;
	}
	@Override
	public String toString() {
		return "Tweet [text=" + text + ", id_str=" + id_str + ", feel=" + feel + "]";
	}
	
}
