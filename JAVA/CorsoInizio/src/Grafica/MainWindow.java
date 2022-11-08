package Grafica;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MainWindow extends JFrame {

	private JPanel contentPane;
	private JTextField clienteField;
	private static JTextArea clientiArea;
	private JLabel lblNewLabel_1, lblInserisci;
	private JButton btnInserisci;
	
	private static GestioneClienti gs = new GestioneClienti();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainWindow frame = new MainWindow();
					frame.setVisible(true);
					clientiArea.setText(gs.leggi());
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MainWindow() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 650, 400);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblInserisci = new JLabel("Inserisci Nuovo Cliente");
		lblInserisci.setHorizontalAlignment(SwingConstants.LEFT);
		lblInserisci.setBounds(6, 22, 638, 16);
		contentPane.add(lblInserisci);
		
		clienteField = new JTextField();
		clienteField.setBounds(6, 50, 474, 40);
		contentPane.add(clienteField);
		clienteField.setColumns(10);
		
		btnInserisci = new JButton("Inserisci");
		btnInserisci.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
//				String ricordo = clientiArea.getText() + " " + clienteField.getText();//Mi salvo quello che c'è nella text area
//				clientiArea.setText(ricordo);
//				clienteField.setText("");
				gs.scrivi(clienteField.getText()); //Scrivo ne file
				clienteField.setText(""); //Pulisco la casella di testo
				clientiArea.setText(gs.leggi()); //Leggo il file e scrivo nella text Area
			}
		});
		btnInserisci.setBounds(492, 51, 152, 40);
		contentPane.add(btnInserisci);
		
		lblNewLabel_1 = new JLabel("Utenti Presenti");
		lblNewLabel_1.setBounds(6, 116, 638, 16);
		contentPane.add(lblNewLabel_1);
		
		clientiArea = new JTextArea();
		clientiArea.setEditable(false);
		clientiArea.setBounds(6, 144, 638, 222);
		contentPane.add(clientiArea);
	}
}
