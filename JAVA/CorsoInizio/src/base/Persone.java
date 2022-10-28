package base;

public class Persone {

	String nome;
	String cognome;
	int eta;
	String citta;
	
	Persone(String nome, String cognome, int eta, String citta){
		this.nome = nome;
		this.cognome = cognome;
		this.eta = eta;
		this.citta = citta;
	}
	
	void saluta() {
		System.out.println("Piacere sono " + nome);
	}
	
	void getEta() {
		System.out.println("Ho " + eta);
	}
}
