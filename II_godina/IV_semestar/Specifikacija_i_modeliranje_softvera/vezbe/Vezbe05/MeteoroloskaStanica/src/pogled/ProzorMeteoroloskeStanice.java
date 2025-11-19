package pogled;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

import dogadjaj.Observer;
import dogadjaj.UpdateEvent;
import kontroler.KontrolerStanice;
import model.DnevnaTemperatura;
import net.miginfocom.swing.MigLayout;


/**
 *  ProzorMeteoroloskeStanice - prozor koji omogućava unos i pregled dnevnih temperatura i njihovih statistika
 *  Demonstrira upotrebu Model-View-Controller šablona kombinovanog sa Observer šablonom
 */
public class ProzorMeteoroloskeStanice extends JDialog implements Observer {
	//kontroler
	private KontrolerStanice kontrolerStanice;
	//model
	private DnevnaTemperatura dnevnaTemperatura;	
	
	// Grafičke komponente
	private JLabel lblUnosTemperature = new JLabel("Unos temperature");
	private JTextField tfUnosTemperature = new JTextField(15);
	private JButton btnUnosTemperature = new JButton("Unos");
	
	private JLabel lblMinTemperatura = new JLabel("Minimalna temperatura");		
	private JLabel lblMaxTemperatura = new JLabel("Maksimalna temperatura");		
	private JLabel lblSrednjaTemperatura = new JLabel("Srednja temperatura");
	private JTextField tfMinTemperatura = new JTextField(15);
	private JTextField tfMaxTemperatura = new JTextField(15);
	private JTextField tfSrednjaTemperatura = new JTextField(15);	
		
	public ProzorMeteoroloskeStanice(DnevnaTemperatura dnevnaTemperatura, KontrolerStanice kontrolerStanice) {
		this.dnevnaTemperatura = dnevnaTemperatura;
		this.kontrolerStanice = kontrolerStanice;
		
		//Prozor se registruje za praćenje događaja o promeni podataka u modelu  
		this.dnevnaTemperatura.addObserver(this);							
		
		setTitle("Meteorološka stanica");		
		setSize(700, 600);
		
		setLayout(new BorderLayout());
		dodajKomponente();
	}		
	
	/**
	 * dodajKomponente - metoda za dodavanje grafičkih komponenti na prozor	 
	 */
	public void dodajKomponente() {		
		JPanel panel = new JPanel();
		//Najefikasniji layout manager u javi!
		panel.setLayout(new MigLayout());
		
		panel.add(lblUnosTemperature);
		panel.add(tfUnosTemperature);
		panel.add(btnUnosTemperature, "wrap");
			
		tfMinTemperatura.setEditable(false);
		tfMaxTemperatura.setEditable(false);
		tfSrednjaTemperatura.setEditable(false);
			
		panel.add(lblMinTemperatura);		
		panel.add(tfMinTemperatura, "wrap");		
		panel.add(lblMaxTemperatura);	
		panel.add(tfMaxTemperatura, "wrap");			
		panel.add(lblSrednjaTemperatura);	
		panel.add(tfSrednjaTemperatura, "wrap");
		
		add(panel, BorderLayout.NORTH);
		
		PanelGrafik pnlGrafik = new PanelGrafik(dnevnaTemperatura);
		add(pnlGrafik, BorderLayout.CENTER);
		
		btnUnosTemperature.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				unosTemperature();
			}
		});		
		
		getRootPane().setDefaultButton(btnUnosTemperature);
	}
	
	/**
	 * unosTemperature - metoda koja se poziva kada korisnik klikne na dugme "Unos" 	 
	 */
	public void unosTemperature () {
		try {
			kontrolerStanice.unosNoveTemperature(tfUnosTemperature.getText());
			tfUnosTemperature.setText(null);			
		}
		catch(NullPointerException ex){
			JOptionPane.showMessageDialog(this, "Temperatura nije uneta!", "Greška", JOptionPane.ERROR_MESSAGE);			
		}
		catch(NumberFormatException ex){
			JOptionPane.showMessageDialog(this, "Temperatura mora biti uneta kao broj!", "Greška", JOptionPane.ERROR_MESSAGE);
		}
		catch(IllegalArgumentException ex){
			JOptionPane.showMessageDialog(this, ex.getMessage(), "Greška", JOptionPane.ERROR_MESSAGE);
		}
		finally {
			tfUnosTemperature.grabFocus();
		}
	}			
	
	/**
	 * updatePerformed - metoda koja implementira Observer interfejs. Nju poziva Publisher kada dođe do promene njegovih podataka ili stanja 	 
	 */
	public void updatePerformed(UpdateEvent e) {
		//model je promenjen, treba osvežiti statističke podatke:
		prikaziStatistiku();
	}
	
	/**
	 *  prikaziStatistiku - metoda koja osvežava vrednosti minimalne, maksimalne i prosečne temperature na prozoru  	 
	 */
	private void prikaziStatistiku() {
		try {
			DecimalFormat df = new DecimalFormat("0.0");		
			tfMaxTemperatura.setText(df.format(dnevnaTemperatura.getMaxVrednost()));
			tfMinTemperatura.setText(df.format(dnevnaTemperatura.getMinVrednost()));
			tfSrednjaTemperatura.setText(df.format(dnevnaTemperatura.srednjaVrednost()));
		}
		catch(NullPointerException ex){
			JOptionPane.showMessageDialog(this, "Nema unetih temperatura!", "Greška", JOptionPane.ERROR_MESSAGE);			
		}
	}	
}
