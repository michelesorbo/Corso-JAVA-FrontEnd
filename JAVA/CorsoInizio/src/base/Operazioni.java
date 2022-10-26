package base;

import java.util.Random;

public class Operazioni {
	
	double a,b;
	
	
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
