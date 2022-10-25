package base;

import java.util.Random;
import java.util.Scanner;

public class es_doWhile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Esercizio 1: Le vocali preferite dai bambini
//		Una maestra chiede ai bambini quale sia la loro vocale preferita. Realizzare un programma che permetta alla maestra di inserire iterativamente le vocali preferite dai propri alunni di prima elementare. Dopo ogni singolo inserimento si deve chiedere alla maestra se intende proseguire inserendo un'altra preferenza oppure no. 
//		Terminata la fase di inserimento delle preferenze, il programma deve mostrare la lettera (o più lettere se a parimeritro) preferita dagli alunni.
		esercizio3();
		
//		Esercizio 2: Indovina l'età del professor Random (tentativi illimitati)
//		Il professor Random ha un'età casuale tra 20 e 60 anni. Realizzare un programma che permetta all’utente di provare a indovinare l'età del professore. L’utente avrà a disposizione illimitati tentativi in cui:
//		Se l’utente inserisce proprio il numero scelto dal computer, il programma mostrerà la scritta “hai vinto” e terminerà la sua esecuzione.
//		Se l’utente inserisce un numero più piccolo rispetto a quello pensato dal computer, il programma mostrerà la scritta “Il professor Random è più grande”.
//		Se l’utente inserisce un numero più grande rispetto a quello pensato dal computer, il programma mostrerà la scritta “Il professor Random è più giovane”.
//		Qunti tentativi ho fatto per indovinare
		
		//Esercizio 3
		// Creare un array di 10 elementi e riempirlo in modo randomico con numeri da 1 a 100;
		//Fare: La somma dei numeri inseriti
		//Fare: La media dei numeri inseriti
		//Fare: La ricerca del numero minimo e del massimo nell'array
	}
	
	public static void esercizio1() {
		//Esecuzione dell'esercizio 1
		Scanner scanner = new Scanner(System.in);
		String vocale;
		System.out.println("Esito esercizio 1");
		int ContaA = 0;
		int ContaE = 0;
		int ContaI = 0;
		int ContaO = 0;
		int ContaU = 0;
		
		do {
			System.out.println("Inserisci la vocale scelta 'f' per terminare");
			vocale = scanner.nextLine();
			if(vocale.toLowerCase().equals("a")) {
				ContaA++;
			}else if(vocale.toLowerCase().equals("e")) {
				ContaE++;
			}else if(vocale.toLowerCase().equals("i")) {
				ContaI++;
			}else if(vocale.toLowerCase().equals("o")) {
				ContaO++;
			}else if(vocale.toLowerCase().equals("u")) {
				ContaU++;
			}else {
				System.out.println("Non è una vocale");
			}
		}while(!vocale.toLowerCase().equals("f"));
		
		System.out.println("La vocale a è stata scelta "+ ContaA + " volte");
		System.out.println("La vocale e è stata scelta "+ ContaE + " volte");
		System.out.println("La vocale i è stata scelta "+ ContaI + " volte");
		System.out.println("La vocale o è stata scelta "+ ContaO + " volte");
		System.out.println("La vocale u è stata scelta "+ ContaU + " volte");
		
	}
	
	public static void esercizio2() {
		//Esecuzione
	}
	
	public static void esercizio3() {
		int[] ar_ran = new int[10]; //Array di 10 elementi vuoto
		Random rm = new Random();
		
		for(int i = 0; i < ar_ran.length; i++) {
			ar_ran[i] = rm.nextInt(100) + 1;
		}
		
		for(int el:ar_ran) {
			System.out.println(el);
		}
	}

}
