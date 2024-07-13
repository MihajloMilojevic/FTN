package vezbe_01_csv.zadaci;
import com.opencsv.bean.CsvBindByPosition;

public class Tacka {
	@CsvBindByPosition(position = 0, required = true)
	private double x;
	@CsvBindByPosition(position = 1, required = true)
	private double y;
	@CsvBindByPosition(position = 2, required = true)
	private double z;
	@CsvBindByPosition(position = 3, required = false)
	private double dist;
	
	public Tacka() {
		
	}
	
	public Tacka(double x, double y, double z) {
		super();
		this.x = x;
		this.y = y;
		this.z = z;
	}


	public double getX() {
		return x;
	}


	public void setX(double x) {
		this.x = x;
	}


	public double getY() {
		return y;
	}


	public void setY(double y) {
		this.y = y;
	}


	public double getZ() {
		return z;
	}


	public void setZ(double z) {
		this.z = z;
	}


	public double getDist() {
		return dist;
	}


	public void setDist(double dist) {
		this.dist = dist;
	}


	public Tacka(double x, double y, double z, double dist) {
		super();
		this.x = x;
		this.y = y;
		this.z = z;
		this.dist = dist;
	}
	
	
	public void calculateDistance() {
		this.dist = Math.sqrt(x*x + y*y +z*z);
	}
	
	
	


}
