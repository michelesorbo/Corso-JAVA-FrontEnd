package base;

import java.util.ArrayList;

public class wrapper_ArrayList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int n = 5; //Tipo primitivo sono sempre da considerare
		
		//Wrapper Class
		Integer numero = 5; //int
		Character carattere = 'a'; //char
		Double numero_virgola = 5.25; //double
		Boolean vero = true; //boolen
		String str = "Vittorio"; //Costrutto
		
		//ArrayList finalmente un array come lo conoscevi
		//ArrayList vogliono solo le WrapperClass
		ArrayList<String> alunni = new ArrayList<String>();
		
		alunni.add("Vittorio"); //aggiungo elemnti all'ArrayList
		alunni.add("Luca");
		alunni.add("Federico");
		//Conoscere quanti elimenti ci sono
		System.out.println(alunni.size());
		
		//Stampare un elemnto ad un detrminato indice
		System.out.println(alunni.get(0));
		
		
		System.out.println("\nStampo tutti gli alunni\n");
		//Stampare gli elementi di un ArrayList
		for(int i = 0; i<alunni.size(); i++) {
			System.out.println(alunni.get(i));
		}
		
		//Modificare valora ad un indice dell'ArrayList
		alunni.set(1, "Errico");
		
		System.out.println("\nStampo gli alunni nuovi\n");
		//Stampare gli elementi di un ArrayList
		for(int i = 0; i<alunni.size(); i++) {
			System.out.println(alunni.get(i));
		}
		
		//Eliminare un elemento ad un determinato indice
		alunni.remove(1);
		System.out.println("\nStampo gli alunni dopo remove\n");
		//Stampare gli elementi di un ArrayList
		for(int i = 0; i<alunni.size(); i++) {
			System.out.println(alunni.get(i));
		}
		System.out.println("Nuova posizione 1 " + alunni.get(1));
		
		//Cancellare tutto l'ArrayAlist
		alunni.clear();
		System.out.println(alunni.size());
		
	}

}
