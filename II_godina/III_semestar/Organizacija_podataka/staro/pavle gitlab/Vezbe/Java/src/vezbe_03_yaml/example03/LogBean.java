package vezbe_03_yaml.example03;

import java.util.Map;

public class LogBean {
	public String User;
	public String Warning;
	public String Date;
	public String Time;
	public String Fatal;
	public Map<String, String> Stack;
	@Override
	public String toString() {
		return "LogBean [User=" + User + ", Warning=" + Warning + ", Date=" + Date + ", Time=" + Time + ", Fatal="
				+ Fatal + ", Stack=" + Stack + "]";
	}
	
	
}
