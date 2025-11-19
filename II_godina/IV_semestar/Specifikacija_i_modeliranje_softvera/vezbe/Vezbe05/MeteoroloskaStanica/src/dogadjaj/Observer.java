package dogadjaj;


/**
 * Observer interfejs treba da implementiraju svi koji zele da se registruju za pracenje promena podataka u okviru modela
 * 
 */
public interface Observer {
	public void updatePerformed(UpdateEvent e);
}