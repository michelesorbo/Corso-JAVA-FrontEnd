package base;

import java.util.Scanner;

public class es_prima_lezione {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
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
		Scanner imp = new Scanner(System.in);
		int min, n;
		System.out.println("Quanti numeri vuoi inserire?");
		int numeri = imp.nextInt();
		System.out.println("Dammi il primo numero");
		min = imp.nextInt();
		for(int i = 2; i<=numeri; i++) {
			System.out.println("Dammi il "+i+"° numero");
			n = imp.nextInt();
			if(n < min) {
				min = n;
			}
		}
		
		System.out.println("Il minore è: "+min);

	}

}
