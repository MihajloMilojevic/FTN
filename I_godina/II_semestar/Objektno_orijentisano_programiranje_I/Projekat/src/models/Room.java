package models;

import java.text.ParseException;
import java.util.ArrayList;

import models.enums.RoomStatus;

public class Room extends Model {
	
	/* ******************************  ATTRIBUTES  *************************************** */
	
	private int number;
	private RoomType type;
	private RoomStatus status;
	private ArrayList<RoomAddition> roomAdditions;
	private Maid maid;
	private ArrayList<CleaningLog> cleaningLogs;
	
	/* ******************************  CONSTRUCTORS  *************************************** */	
	
	public Room() {
		super();
		this.number = 0;
		this.type = null;
		this.status = RoomStatus.FREE;
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	
	public Room(String id) {
		super(id);
		this.number = 0;
		this.type = null;
		this.status = RoomStatus.FREE;
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}

	public Room(int number, RoomType type, RoomStatus status, ArrayList<RoomAddition> roomAdditions) {
		super();
		this.number = number;
		this.type = type;
		this.status = status;
		this.roomAdditions = roomAdditions;
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	
	public Room(String id, int number, RoomType type, RoomStatus status, ArrayList<RoomAddition> roomAdditions) {
		super(id);
		this.number = number;
		this.type = type;
		this.status = status;
		this.roomAdditions = roomAdditions;
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}

	public Room(int number, RoomType type, RoomStatus status) {
		super();
		this.number = number;
		this.type = type;
		this.status = status;
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}

	public Room(int number, RoomType type) {
		super();
		this.number = number;
		this.type = type;
		this.status = RoomStatus.FREE;
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	
	public Room(String id, int number, RoomType type) {
		super(id);
		this.number = number;
		this.type = type;
		this.status = RoomStatus.FREE;
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	
	public Room(String id, int number, RoomType type, RoomStatus status) {
		super(id);
		this.number = number;
		this.type = type;
		this.status = status;
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	public Room(int number, RoomType type, String status, ArrayList<RoomAddition> roomAdditions) {
		super();
		this.number = number;
		this.type = type;
		this.status = RoomStatus.valueOf(status);
		this.roomAdditions = roomAdditions;
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	public Room(String id, int number, RoomType type, String status, ArrayList<RoomAddition> roomAdditions) {
		super(id);
		this.number = number;
		this.type = type;
		this.status = RoomStatus.valueOf(status);
		this.roomAdditions = roomAdditions;
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}

	public Room(int number, RoomType type, String status) {
		this.number = number;
		this.type = type;
		this.status = RoomStatus.valueOf(status);
		this.roomAdditions = new ArrayList<RoomAddition>();
		this.maid = null;
		this.cleaningLogs = new ArrayList<CleaningLog>();
	}
	
	/* ******************************  METHODS  *************************************** */

	public void addRoomAddition(RoomAddition roomAddition) {
		this.roomAdditions.add(roomAddition);
	}

	public void removeRoomAddition(RoomAddition roomAddition) {
		this.roomAdditions.remove(roomAddition);
	}
	
	public void addCleaningLog(CleaningLog cleaningLog) {
		this.cleaningLogs.add(cleaningLog);
	}
	
	@Override
	public boolean isValid() {
		if (this.number < 0) return false;
		if (this.type == null || !this.type.isValid()) return false;
		if (this.status == null) return false;
		if (this.roomAdditions == null) return false;
		for (RoomAddition roomAddition : this.roomAdditions) {
			if (!roomAddition.isValid())
				return false;
		}
		return super.isValid();
	}
	
	@Override
	public Object get(String key) throws IllegalArgumentException {
		switch (key) {
			case "number":
				return (Object) this.number;
			case "type":
				return (Object) this.type;
			case "status":
				return (Object) this.status;
			case "roomAdditions":
				return (Object) this.roomAdditions;
			case "maid":
				return (Object) this.maid;
			default:
				return super.get(key);
		}
	}
	@SuppressWarnings("unchecked")
	@Override
	public void set(String key, Object value) {
		switch (key) {
		case "number":
			this.number = (int) value;
			break;
		case "type":
			this.type = (RoomType) value;
			break;
		case "status":
			this.status = (RoomStatus) value;
			break;
		case "roomAdditions":
			this.roomAdditions = (ArrayList<RoomAddition>) value;
			break;
		case "maid":
			this.maid = (Maid) value;
			break;
		default:
			super.set(key, value);
		}
	}
	
	@Override
	public String toString() {
		return String.join(";", new String[] { 
				super.toString(),
				String.valueOf(number), 
				status.toString()
			});
	}
	@Override
	public Object clone() throws CloneNotSupportedException {
		ArrayList<RoomAddition> roomAdditionsClone = new ArrayList<RoomAddition>();
		for (RoomAddition roomAddition : this.roomAdditions) {
			roomAdditionsClone.add((RoomAddition)roomAddition.clone());
		}
		ArrayList<CleaningLog> cleaningLogsClone = new ArrayList<CleaningLog>();
		for (CleaningLog cleaningLog : this.cleaningLogs) {
			if (cleaningLog == null) continue;
			cleaningLogsClone.add((CleaningLog) cleaningLog.clone());
		}
		Room r = new Room(id, number, type != null ? (RoomType)type.clone() : null, status, roomAdditionsClone);
		r.setMaid(maid != null ? (Maid)maid.clone() : null);
		r.setCleaningLogs(cleaningLogsClone);
		if (this.isDeleted()) r.delete();
		return r;
	}
	
	@Override
	public void update(Model newModel) throws IllegalArgumentException {
		super.update(newModel);
		if (!(newModel instanceof Room)) throw new IllegalArgumentException("Not  a Room object");
		Room room = (Room) newModel;
		this.number = room.number;
		this.type = room.type;
		this.status = room.status;
		this.roomAdditions = room.roomAdditions;
		this.maid = room.maid;
		this.cleaningLogs = room.cleaningLogs;
	}
	
    @Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null || obj.getClass() != this.getClass()) {
			return false;
		}
		Room room = (Room) obj;
		return (this.number == room.number && this.type.equals(room.type) && this.status.equals(room.status)
				&& this.roomAdditions.equals(room.roomAdditions));
	}
    @Override
	public Model fromCSV(String csv) throws ParseException {
		super.fromCSV(csv);
		String[] values = csv.split(";");
		if (values.length < 4) throw new ParseException("Invalid RoomType string", 1);
		this.number = Integer.parseInt(values[2]);
		this.status = RoomStatus.valueOf(values[3]);
		return this;
	}
    
    
    /* ******************************  GETTERS AND SETTERS  *************************************** */
    
    
	/**
	 * @return the number
	 */
	public int getNumber() {
		return number;
	}
	
	/**
	 * @return the number
	 */
	public void setNumber(int number) {
		this.number = number;
	}


	/**
	 * @return the type
	 */
	public RoomType getType() {
		return type;
	}

	/**
	 * @param type the type to set
	 */
	public void setType(RoomType type) {
		this.type = type;
	}

	/**
	 * @return the status
	 */
	public RoomStatus getStatus() {
		return status;
	}

	/**
	 * @param status the status to set
	 */
	public void setStatus(RoomStatus status) {
		this.status = status;
	}

	/**
	 * @return the roomAdditions
	 */
	public ArrayList<RoomAddition> getRoomAdditions() {
		return roomAdditions;
	}

	/**
	 * @param roomAdditions the roomAdditions to set
	 */
	public void setRoomAdditions(ArrayList<RoomAddition> roomAdditions) {
		this.roomAdditions = roomAdditions;
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

	/**
	 * @return the cleaningLogs
	 */
	public ArrayList<CleaningLog> getCleaningLogs() {
		return cleaningLogs;
	}

	/**
	 * @param cleaningLogs the cleaningLogs to set
	 */
	public void setCleaningLogs(ArrayList<CleaningLog> cleaningLogs) {
		this.cleaningLogs = cleaningLogs;
	}

}
