package base;

import java.util.Scanner;

public class minimi {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		//Dati 3 numeri trovare il massimo dei numeri
		final String docente = "Michele"; //Creo una costante	
		System.out.println(docente);
		saluto("Vittorio");
		saluto(docente);
		int somma = somma(3,6);
		System.out.println("Stampo dalla funzione MAIN: "+somma);
		int n1 = 12, n2 = 45;
		int somma2 = somma(n1,n2);
		System.out.println(somma2);
		int max = max(5,7,6);
		System.out.println("Il max è: "+max);
		System.out.println("Il massimo tra 9 6 e 13 è: "+max(9,6,13));
		System.out.println("Inserisci 3 numeri e per sapere il massimo");
		
		int primo = scanner.nextInt();
		int secondo = scanner.nextInt();
		int terzo = scanner.nextInt();
		System.out.println("Il maggiore è: "+max(primo,secondo,terzo));

	}
	
	public static void saluto(String nome) {
		System.out.println("Ciao dalla funzione saluto il nome passato alla funzione è: "+nome);
		int somma3 = somma(2,4);
		System.out.println("Somma da funzione saluto: "+somma3);
	}
	
	public static int somma(int a, int b) {
		return a+b;
	}
	
	public static int max(int a, int b, int c) {
		if(a > b && a > c) {
			return a;
		}else if(b > a && b > c) {
			return b;
		}else {
			return c;
		}
	}

}
