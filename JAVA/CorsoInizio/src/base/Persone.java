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
	
	public void saluta() {
		System.out.println("Piacere sono " + nome);
	}
	
	public void getEta() {
		System.out.println("Ho " + eta);
	}
}
