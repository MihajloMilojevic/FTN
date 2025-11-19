package rs.ac.uns.ftn.siit.op.yaml.example02;

public class Product {
	private String sku;
	private Integer quantity;
	private String description;
	private Float price;

	public Product() {
		super();
	}

	public Product(String sku, Integer quantity, String description, Float price) {
		super();
		this.sku = sku;
		this.quantity = quantity;
		this.description = description;
		this.price = price;
	}

	public String getSku() {
		return sku;
	}

	public void setSku(String sku) {
		this.sku = sku;
	}

	public Integer getQuantity() {
		return quantity;
	}

	public void setQuantity(Integer quantity) {
		this.quantity = quantity;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public Float getPrice() {
		return price;
	}

	public void setPrice(Float price) {
		this.price = price;
	}

	@Override
	public String toString() {
		return "Product [sku=" + sku + ", quantity=" + quantity + ", description=" + description + ", price=" + price
				+ "]";
	}

}
