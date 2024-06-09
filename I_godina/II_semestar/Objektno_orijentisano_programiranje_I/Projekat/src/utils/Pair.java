package utils;

public class Pair<K, V> {

	private K first;
	private V second;
	
	public Pair(K first, V second) {
		this.first = first;
        this.second = second;
	}
	
	@Override
	public String toString() {
		return "(" + first + ", " + second + ")";
	}

	/**
	 * @return first element of the pair
	 */
	public K getFirst() {
		return first;
	}

	/**
	 * @param first - first element of pair to set
	 */
	public void setFirst(K first) {
		this.first = first;
	}

	/**
	 * @return the second element of the pair
	 */
	public V getSecond() {
		return second;
	}

	/**
	 * @param second - second element of pair to set
	 */
	public void setSecond(V second) {
		this.second = second;
	}
	
}
