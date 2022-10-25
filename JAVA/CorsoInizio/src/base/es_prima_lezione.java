package base;

import java.util.Scanner;
import java.util.Random;

public class es_prima_lezione {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner imp = new Scanner(System.in);
		
		//int[] ar = new int[3];
		int[] ar = {1,3,5};
		
//		System.out.println(ar.length);
//		for(int numero: ar) {
//			System.out.println(numero);
//		}
		
//		for(int i = 0;i<ar.length; i++ ) {
//			System.out.println(ar[i]);
//		}
//		
		
		//1° Esercizio
		//Chiedere all'utente quanti numeri vuole inserire
		//Chiedere i numeri e ritornare il minore
		
		//2°
		//Creare una funzione che passato un prezzo e uno scontpo ritorni il prezzo scontato
		
		//3°
//		Scrivere una funzione per calcolare l’importo di una tassa secondo la seguente tabella:
//			Fino a 10.000 €, l’importo della tassa è del 10%
//			Fino a 20.000 €, l’importo della tassa è del 10% per i primi 10.000 €, del 7 % sul restante.
//			Fino a 30.000 €, l’importo è ancora del 10% per i primi 10.000 €, poi del 7% fino a 20.000 ed infine il 5% sul restante.
//			Oltre i 30.000 € ci si comporta come prima, aggiungendo un ulteriore 3% è sulla porzione oltre i 30.000 €.
//			Per ogni importo non valido si ritorni -1 (qualunque importo che non sia un numero reale e positivo).
		
//		Esempi:Un importo di 10, dovrebbe tornare 1 (1 è il 10% di 10)
//		Un importo di 21, dovrebbe tornare 1.75 (10% di 10 + 7% di 10 + 5% di 1)

//		4°
//		Scrivere un metodo che prende in ingresso due stringhe e ritorni la stringa vincitrice, 
//		le stringhe possono valere solo: “carta”, “forbice” o “sasso”. 
//		Il programma dovrà quindi effettuare i dovuti controlli e dichiarare il vincitore 
//		secondo le note regole della “morra cinese” 
//		(forbice vince su carta, carta vince su sasso, sasso vince su forbice).
		
		
		//1° Esercizio Soluzione (Fare a casa, trasformare tutto in metodo restiruisci_minore)
//		int min, n;
//		System.out.println("Quanti numeri vuoi inserire?");
//		int numeri = imp.nextInt();
//		System.out.println("Dammi il primo numero");
//		min = imp.nextInt();
//		for(int i = 2; i<=numeri; i++) {
//			System.out.println("Dammi il "+i+"° numero");
//			n = imp.nextInt();
//			if(n < min) {
//				min = n;
//			}
//		}
//		
//		System.out.println("Il minore è: "+min);
		
		Random rm = new Random();
		System.out.println(rm.nextInt(4)+1);
		
		int i = 1;
//		while(i <= 10) {
//			//Esecuzione
//			System.out.println(i);
//			i++;
//		}
		int numero, tentativi = 1;
		int num_indovinare = rm.nextInt(4) + 1;
		
		do {
			System.out.println("Indovina il numero");
			numero = imp.nextInt();
			if(numero != num_indovinare) {
				System.out.println("Errato");
				tentativi++;
			}
			
		}while(numero != num_indovinare);
		
		System.out.println("Indovinato in " + tentativi + " tentativi");

	}
	
	public static void morra_cinese(String s1, String s2) { 
		
		//1 = Sasso
		//2 = Carta
		//3 = Forbice
		
		if(s1.equals("sasso") && s2.equals("sasso")) { 
			System.out.println("Pareggio"); 
		}else if(s1.equals("sasso") && s2.equals("forbice")) { 
			System.out.println("Ha vinto sasso"); 
		}else if(s1.equals("sasso") && s2.equals("carta")) { 
			System.out.println("Ha vinto carta"); 
		}else if(s1.equals("carta") && s2.equals("carta")) { 
			System.out.println("Pareggio"); 
		} else if(s1.equals("carta") && s2.equals("forbice")) { 
			System.out.println("Ha vinto forbice"); 
		} else if(s1.equals("carta") && s2.equals("sasso")) { 
			System.out.println("Ha vinto carta"); 
		}else if(s1.equals("forbice") && s2.equals("forbice")) { 
			System.out.println("Pareggio"); 
		}else if(s1.equals("forbice") && s2.equals("sasso")) { 
			System.out.println("Ha vinto sasso"); 
		}else if(s1.equals("forbice") && s2.equals("carta")) { 
			System.out.println("Ha vinto forbice"); 
		} 

		 
	}

}
