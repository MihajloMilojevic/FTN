package pogled;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.text.DecimalFormat;
import java.util.List;

import javax.swing.JPanel;

import dogadjaj.Observer;
import dogadjaj.UpdateEvent;
import model.DnevnaTemperatura;

/**
 *  PanelGrafik mogućava crtanje grafika promene temperature u toku dana 
 */
public class PanelGrafik extends JPanel implements Observer {
	//model
	private DnevnaTemperatura dnevnaTemperatura;	
	
	private float razmakX;
	private float razmakY;	
	
	public PanelGrafik(DnevnaTemperatura dnevnaTemperatura) {					
		this.dnevnaTemperatura = dnevnaTemperatura;				
		//panel se registruje za praćenje dogadjaja o promeni podataka 
		dnevnaTemperatura.addObserver(this);				
	}	

	/**
	 *  updatePerformed - reakcija na dogadjaj o promeni podataka u modelu
	 */
	public void updatePerformed(UpdateEvent e) {
		// poziv metode pretka za ponovno iscrtavanje komponente. Ona poziva metodu paintComponent. 
		// paintComponent se nikad ne poziva direktno!
		repaint();
	}
	
	/**
	 *  paintComponent - metoda koju treba redefinisati kada želimo da promenimo način iscrtavanja komponente 
	 */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);        
        
        Graphics2D g2 = (Graphics2D)g;                                                  
        
        List<Float> temperature = dnevnaTemperatura.getIzmereneVrednosti();
        if (null == temperature) 
        	return;                     
        
        //Pravimo podeok za svakih 10 stepeni:
        float brojPodeoka = (DnevnaTemperatura.MAX_TEMP - DnevnaTemperatura.MIN_TEMP) / 10 + 1;
        razmakY = getHeight()/brojPodeoka;
        razmakX = razmakY;
        int brojElemenata = temperature.size();        
        if (getWidth() / brojElemenata < razmakX)
        	razmakX = getWidth() / brojElemenata;                    
        
        iscrtajOse(g2);        
        
        float temperatura = temperature.get(0);
        float x = razmakX;       
        float y = racunajY(temperatura);        		
        
        float prevX = x;
        float prevY = y;        
		
        g2.setPaint(Color.BLACK);
        Font font = new Font("Serif", Font.BOLD, 12);
        g.setFont(font);
        
        //Iscrtavanje prve tačke
        iscrtajTacku(g2, x, y, temperatura);        
        
        //iscrtavanje preostalih tačaka spojenih linijom
        for (int i = 1; i < brojElemenata; i++) {
        	x += razmakX;
        	temperatura = temperature.get(i);
        	y = racunajY(temperatura);  
        	iscrtajTacku(g2, x, y, temperatura);
        	
        	g2.drawLine(Math.round(prevX), Math.round(prevY), Math.round(x), Math.round(y));        	
        	prevX = x;
        	prevY = y;
        }     
    }
    
    /**
	 *  iscrtajOse - metoda za iscrtavanje osa, radi lakše orijentacije na grafiku 
	 */     
    private void iscrtajOse(Graphics2D g2) {
    	// x osa
        g2.setPaint(Color.BLUE);
        g2.drawLine(0, getHeight()/2, getWidth(),  getHeight()/2);
        // y osa
        g2.drawLine(Math.round(razmakX), 0, Math.round(razmakX),  getHeight());
    }
    
    /**
  	 *  racunajY - Računanje y koordinate tačke u odnosu na sredinu panela 
  	 */   
    private float racunajY(float temperatura) {    	
    	return getHeight()/2 - temperatura / 10 * razmakY;    	
    }    
    
    /**
  	 *  iscrtajTacku - Iscrtavanje tačke na grafiku 
  	 */
    private void iscrtajTacku(Graphics2D g2, float x, float y, float temperatura) {
    	DecimalFormat df = new DecimalFormat("0.0");
    	
    	g2.drawString(df.format(temperatura), x, y - 10);
    	g2.fillRect(Math.round(x-3), Math.round(y-3), 6, 6);
    }    
 
}
