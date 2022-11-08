package Grafica;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class GestioneClienti {
	
	private String path = "clienti.txt";
	
	public void scrivi(String testo) {
		
		try {
			File file = new File(path);
			
			FileWriter fw = new FileWriter(file, true); //Apro il file in scrittura e append
			fw.append(testo + "\n");
			fw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public String leggi() {
		
		String fileLetto = "";
		
		try {
			File file = new File(path);
			
			FileReader fr = new FileReader(file);
			
			int data = fr.read();
			
			while(data != -1) {
				fileLetto = fileLetto + (char)data;
				data = fr.read();
			}	
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return fileLetto;
	}

}
