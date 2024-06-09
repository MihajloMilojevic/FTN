package behavioral.strategy;

public class CaesarStrategy implements EncryptStrategy {

	@Override
	public char[] encrypt(String text, String key) {
		char[] buff = new char[text.length()];
		char keyC = key.charAt(0);
		for (int i = 0; i < text.length(); i++) {
			char c = (char) (text.charAt(i) + keyC);
			buff[i] = c;
		}
		return buff;
	}

	@Override
	public String decrypt(char[] text, String key) {
		char keyC = key.charAt(0);
		for (int i = 0; i < text.length; i++) {
			char c = (char) (text[i] - keyC);
			text[i] = c;
		}
		return new String(text);
	}

}
