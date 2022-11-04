package lezione04;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class GestioneFile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		File file = new File("prova.txt");
		///Users/michelesorbo/Desktop/vgsales.csv
		//C:\Users\Vittorio\Desctop\provas.txt
		//Controlle se il file esiste
		if(file.exists()) {
			System.out.println("Il file esiste");
			System.out.println("Il Path del file è: " + file.getPath());
			System.out.println("Il Path Assoluto del file è: " + file.getAbsolutePath());
			System.out.println("è un file? : " + file.isFile());
			//file.delete(); //Cancello il file
		}else {
			System.out.println("il file non esiste");
		}
		
		//Inzio a scrivere nel File
		try {
			FileWriter writer = new FileWriter("prova.txt");
			//Il metodo write cancella il contenuto del file e scrive il nuovo contenuto
			//writer.write("Ciao sono Vittorio\nPer ora JAVA lo odio"); //Scrivo nel file
			writer.write("Ciao sono JAVA e ho cancellato il contenuto del file");
			
			//Il metodo Append continua a scrivere dalla fine del file
			writer.append("\nSono Vittorio e sono ritornato");
			writer.close(); //Chiudo la scrittura
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		//Lettura di un File
		int data = 0;
		try {
			FileReader reader = new FileReader("prova.txt");
			data = reader.read(); //Ritorna la codifica in Ascii Code
			
			while(data != -1) {
				System.out.print((char)data);
				data = reader.read();
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println(data);
		
		

	}

}
