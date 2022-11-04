package lezione04;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class ScritturaFileAppend {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String path = "prova.txt";
		
		try {
			File file = new File(path);
			FileWriter fw = new FileWriter(file, true); //Mi apre il file in append
			fw.append("\nProva di Append");
			fw.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
		

	}

}
