package models;

import java.text.ParseException;
import java.time.LocalDate;

import utils.CSVDateParser;

public class CleaningLog extends Model {

	/* **************************** Attributes **************************** */
	
	private LocalDate date;
	private Maid maid;
	
	/* **************************** CONSTRUCTORS **************************** */
	
	public CleaningLog() {
	    super();
	}

	public CleaningLog(String id) {
		super(id);
	}
	public CleaningLog(LocalDate date) {
		super();
		this.date = date;
	}
	public CleaningLog(String id, LocalDate date) {
		super(id);
		this.date = date;
	}
	
	public CleaningLog(LocalDate date, Maid maid) {
		super();
		this.date = date;
		this.maid = maid;
	}
	
	public CleaningLog(String id, LocalDate date, Maid maid) {
		super(id);
		this.date = date;
		this.maid = maid;
	}
	

	/* **************************** METHODS **************************** */

	@Override
	public boolean isValid() {
		if (this.date == null) {
			return false;
		}
		if (this.maid == null) {
			return false;
		}
		return super.isValid();
	}

	@Override
	public Object get(String key) throws IllegalArgumentException {
		switch (key) {
		case "date":
			return this.date;
		case "maid":
			return this.maid;
		default:
			return super.get(key);
		}
	}

	@Override
	public void set(String key, Object value) throws IllegalArgumentException {
		switch (key) {
		case "date":
			this.date = (LocalDate) value;
			break;
		case "maid":
			this.maid = (Maid) value;
			break;
		default:
			super.set(key, value);
		}
	}

	@Override
	public void update(Model newModel) throws IllegalArgumentException {
		super.update(newModel);
		CleaningLog cleaningLog = (CleaningLog) newModel;
		this.date = cleaningLog.getDate();
		this.maid = cleaningLog.getMaid();
	}

	@Override
	public String toString() {
		return String.join(";", super.toString(), CSVDateParser.formatDate(date));
	}

	@Override
	public boolean equals(Object obj) {
		return super.equals(obj) && this.date.equals(((CleaningLog) obj).getDate()) && this.maid.equals(((CleaningLog) obj).getMaid());
	}

	@Override
	public Object clone() throws CloneNotSupportedException {
		CleaningLog cleaningLog = new CleaningLog(this.getId());
		if (this.date != null) {
			cleaningLog.setDate(LocalDate.from(date));
		}
		if (this.maid != null) {
			cleaningLog.setMaid((Maid) maid.clone());
		}
		return cleaningLog;
	}

	@Override
	public Model fromCSV(String csv) throws ParseException {
		super.fromCSV(csv);
		String[] values = csv.split(";");
		if (values.length < 3) throw new ParseException("Invalid Cleaning Log csv string", 1);
		this.date = CSVDateParser.parseString(values[2]);
		return this;
	}
	

	/* **************************** GETTERS & SETTERS **************************** */

	/**
	 * @return the date
	 */
	public LocalDate getDate() {
		return date;
	}

	/**
	 * @param date the date to set
	 */
	public void setDate(LocalDate date) {
		this.date = date;
	}

	/**
	 * @return the maid
	 */
	public Maid getMaid() {
		return maid;
	}

	/**
	 * @param maid the maid to set
	 */
	public void setMaid(Maid maid) {
		this.maid = maid;
	}
	
}
