package vezbe_03_yaml.example03;

import java.util.List;

public class Invoice {
	public Integer invoice; // invoice
	public String date; // date
	public Person billTo;// bill-to
	public Person shipTo;// ship-to
	public List<Product> product;
	public Float tax;
	public Float total;
	public String comments;

	@Override
	public String toString() {
		return "Invoice [invoice=" + invoice + ", date=" + date + ", billTo=" + billTo + ", shipTo=" + shipTo
				+ ", product=" + product + ", tax=" + tax + ", total=" + total + ", comments=" + comments + "]";
	}

}
