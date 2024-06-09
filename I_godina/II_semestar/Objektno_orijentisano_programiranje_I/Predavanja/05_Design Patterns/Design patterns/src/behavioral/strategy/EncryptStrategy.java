package behavioral.strategy;

public interface EncryptStrategy {
	public char[] encrypt(String text, String key);
	public String decrypt(char[] text, String key);
}
