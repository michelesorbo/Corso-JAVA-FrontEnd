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
