package lezione04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.AbstractAction;
import java.awt.event.ActionEvent;
import javax.swing.Action;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import javax.swing.JLabel;
import javax.swing.JTextArea;

public class LabelDemo extends JFrame {

	private JPanel contentPane;
	private final Action action = new SwingAction();
	private JTextField textField;
	private JLabel lblNewLabel;
	private JTextArea textArea;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					LabelDemo frame = new LabelDemo();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public LabelDemo() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblNewLabel = new JLabel("New label");
		lblNewLabel.setBounds(20, 16, 61, 16);
		contentPane.add(lblNewLabel);
		
		textField = new JTextField();
		textField.setBounds(129, 11, 130, 26);
		contentPane.add(textField);
		textField.setColumns(10);
		
		textArea = new JTextArea();
		textArea.setEditable(false);
		textArea.setBounds(20, 61, 406, 190);
		contentPane.add(textArea);
		
		JButton btnEnter = new JButton("Enter");
		btnEnter.setBounds(264, 10, 122, 29);
		btnEnter.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.out.println(textField.getText());
				//lblNewLabel.setVisible(false);
				textArea.setText(textField.getText());
			}
		});
		btnEnter.setAction(action);
		contentPane.add(btnEnter);
		
	}

	private class SwingAction extends AbstractAction {
		public SwingAction() {
			putValue(NAME, "SwingAction");
			putValue(SHORT_DESCRIPTION, "Some short description");
		}
		public void actionPerformed(ActionEvent e) {
		}
	}
}
