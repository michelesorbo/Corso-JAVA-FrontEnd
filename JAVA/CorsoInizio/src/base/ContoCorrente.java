package base;

import java.util.ArrayList;

public class ContoCorrente {
	
	int saldo;
	String proprietario;
	String n_conto;
	String[] movimenti = new String[5];
	int conta_movimenti = 0;
	ArrayList<String> movimenti_cc = new ArrayList<String>();
	
	ContoCorrente(int saldo_iniziale, String proprietario, String conto){
		this.saldo = saldo_iniziale;
		this.proprietario = proprietario;
		this.n_conto = conto;
	}
	
	void versa(int somma) {
		saldo = saldo + somma;
		System.out.println("Versamento effettuato.");
		this.movimentiConto("Vesato " + somma);
	}
	
	void preleva(int somma) {
		if(somma > saldo) {
			System.out.println("Non puoi prelevare saldo inferiore");
		}else {
			saldo = saldo - somma;
			System.out.println("Prelievo effettuato.");
			this.movimentiConto("Prelevato " + somma);
		}
	}
	
	void stampa_saldo() {
		System.out.println("Il saldo attuale è: " + saldo);
	}
	
	void info_conto() {
		System.out.println("Proprietario: " + proprietario);
		System.out.println("N° Conto: " + n_conto);
		System.out.println("Il saldo attuale è: " + saldo);
		System.out.println("Hai effettuato " + conta_movimenti + " movimenti sul conto");
	}
	
	//Metodo che aggiunge i movimenti nell'array movimenti classico
//	void movimentiConto(String movimento) {
//		int i;
//		
//		if(conta_movimenti > 4) {
//			for(i = 1; i < movimenti.length; i++) {
//				movimenti[i-1] = movimenti[i]; //Sposto gli elementi di un indice
//			}
//			movimenti[i-1] = movimento; //Mette il versamento nell'ultima posizione dell'array
//		}else{
//			movimenti[conta_movimenti] = movimento;
//		}
//		
//		conta_movimenti++;//Incremento il contatore di movimenti
//	}
	
	void movimentiConto(String movimento) {
		if(movimenti_cc.size() > 4) {
			movimenti_cc.remove(0);
			movimenti_cc.add(movimento);
		}else {
			movimenti_cc.add(movimento);
		}
	}
	
	//Metodo che stampa a video il contenuto dell'array movimenti
//	void stampa_movimenti() {
//		for(String el:movimenti) {
//			System.out.println(el);
//		}
//	}
	
	void stampa_movimenti() {
		for(int i = 0; i < movimenti_cc.size(); i++) {
			System.out.println(movimenti_cc.get(i));
		}
	}

}