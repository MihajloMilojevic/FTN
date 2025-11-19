package rs.ac.uns.ftn.siit.op.yaml.example02;

import java.util.List;

public class Invoice {
	private Integer invoice; // invoice
	private String date; // date
	private Person billTo;// bill-to
	private Person shipTo;// ship-to
	private List<Product> product;
	private Float tax;
	private Float total;
	private String comments;

	public Invoice() {
		super();
	}

	public Invoice(Integer invoice, String date, Person billTo, Person shipTo, List<Product> product, Float tax,
			Float total, String comments) {
		super();
		this.invoice = invoice;
		this.date = date;
		this.billTo = billTo;
		this.shipTo = shipTo;
		this.product = product;
		this.tax = tax;
		this.total = total;
		this.comments = comments;
	}

	public Integer getInvoice() {
		return invoice;
	}

	public void setInvoice(Integer invoice) {
		this.invoice = invoice;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}

	public Person getBillTo() {
		return billTo;
	}

	public void setBillTo(Person billTo) {
		this.billTo = billTo;
	}

	public Person getShipTo() {
		return shipTo;
	}

	public void setShipTo(Person shipTo) {
		this.shipTo = shipTo;
	}

	public List<Product> getProduct() {
		return product;
	}

	public void setProduct(List<Product> product) {
		this.product = product;
	}

	public Float getTax() {
		return tax;
	}

	public void setTax(Float tax) {
		this.tax = tax;
	}

	public Float getTotal() {
		return total;
	}

	public void setTotal(Float total) {
		this.total = total;
	}

	public String getComments() {
		return comments;
	}

	public void setComments(String comments) {
		this.comments = comments;
	}

	@Override
	public String toString() {
		return "Invoice [invoice=" + invoice + ", date=" + date + ", billTo=" + billTo + ", shipTo=" + shipTo
				+ ", product=" + product + ", tax=" + tax + ", total=" + total + ", comments=" + comments + "]";
	}

}
