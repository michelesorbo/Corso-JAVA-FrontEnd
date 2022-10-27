package base;

import java.util.Random;

public class Operazioni {
	
	double a,b;
	
	String[] movimenti = new String[5];
	
	

	
	
	Operazioni(double a, double b){
		this.a = a;
		this.b = b;
	}
	
	//Metodo con ritorno
	double divisione() {
		double risultato = a/b;
		return risultato;
	}
	
	
	//Metodo senza ritorno
	void somma() {
		double risultato = a + b;
		System.out.println("Sonoi il risultato del metodo somma: " + risultato);
	}
	
	void lista_movimenti() {
		int ap, m;
		movimenti[0] = "1 - Prelievo 500"; //FIFO 
		movimenti[1] = "2 - Versato 500";
		movimenti[2] = "3 - Prelievo 500";
		movimenti[3] = "4 - Verso 1500";
		
		String[] appoggio = new String[5];
		
		
		//1° i=1  appoggio[0]= movimenti[1]
		if(movimenti.length >= 5 ) {
			for(ap = 0, m = 1; m < movimenti.length; m++, ap++) {
				if(movimenti[m] == null) {
					break;
				}
				appoggio[ap] = movimenti[m];
			}
			appoggio[ap] = "6 - Versato 700";
		}
		
		System.out.println("Array Movimenti");
		this.stampa_ar(movimenti);
		System.out.println("\n\nArray Appoggio");
		this.stampa_ar(appoggio);
		
	}
	
	
	int[] riempi_ar(int[] ar){

		Random rm = new Random();
		
		for(int i = 0; i < ar.length; i++) {
			ar[i] = rm.nextInt(100) + 1;
		}
		
		return ar;
		
	}
	
	
	void stampa_ar(int[] ar) {
		for(int el:ar) {
			System.out.println(el);
		}
	}
	
	void stampa_ar(String[] ar) {
		for(String el:ar) {
			System.out.println(el);
		}
	}
	
	//Metodo che stampi a video l'elemento maggiore di un array
	void stampa_maggiore(int[] ar) {
		int maggiore = ar[0]; //Imposto il maggiore come 1° elemento dell'array
		
		for(int el:ar) {
			if(el > maggiore) {
				maggiore = el;
			}
		}
		
		System.out.println("L'elemento maggiore è: " + maggiore);
	}
	
	//Metodo che ritorni la somma di tutti gli elementi dell'array
	
	
	
}
