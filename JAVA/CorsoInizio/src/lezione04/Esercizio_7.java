package lezione04;

import java.io.File;
//import java.time.LocalDateTime;
//import java.time.format.DateTimeFormatter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Esercizio_7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		String cliente;
		int scelta;
		
		
		
		do{
			System.out.println("1) per inserire 2) Per leggere 0) Chiudi il programma");
			scelta = in.nextInt();
			in.nextLine(); //Per BUG di Scanner
			
			if(scelta == 1) {
				System.out.println("Inserisci cliente");
				cliente = in.nextLine();
				scrivi(cliente);
			}else if(scelta == 2) {
				leggi();
			}else {
				System.out.println("Scelta non valida");
			}
			
		}while(scelta != 0);
		
		System.out.println("Chiusura del programma tutti i dati sono stati salvati sul file");
		

	}
	
	public static void scrivi(String testo) {
		
//		LocalDateTime data = LocalDateTime.now();
//		DateTimeFormatter it_format_ora = DateTimeFormatter.ofPattern("EEEE, dd MMMM yyyy - HH:mm");
		
		String path = "clienti.txt";
		
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
	
	public static void leggi() {
		String path = "clienti.txt";
		
		try {
			File file = new File(path);
			
			FileReader fr = new FileReader(file);
			
			int data = fr.read();
			
			while(data != -1) {
				System.out.print((char)data);
				data = fr.read();
			}
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
