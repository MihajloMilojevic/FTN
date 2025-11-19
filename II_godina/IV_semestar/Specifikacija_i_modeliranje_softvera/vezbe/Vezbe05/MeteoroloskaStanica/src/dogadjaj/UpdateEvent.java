package dogadjaj;

import java.util.EventObject;


/**
 * Događaj koji se aktivira kada dođe do promene na modelu. Po potrebi, može da sadrži atribute i metode koji opisuju promenu. 
 */
public class UpdateEvent extends EventObject {

	public UpdateEvent(Object object) {		
		super(object);		
	}

}
