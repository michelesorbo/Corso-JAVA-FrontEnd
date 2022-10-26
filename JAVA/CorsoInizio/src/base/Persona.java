package base;

public class Persona {

	//Attributi della classe
	String nome;
	String cognome;
	int eta;
	String citta;
	
	//Costruttore di una classe deve avere lo stesso nome della classe
	Persona(String nome, String cognome, int eta, String citta){
		this.nome = nome;
		this.cognome = cognome;
		this.eta = eta;
		this.citta = citta;
		
	}
	
	//OverLoad del costruttore
	Persona(String nome, String cognome){
		this.nome = nome;
		this.cognome = cognome;
		this.eta = 0;
		this.citta = "";
	}
	
	//Metodi della classe
	
	void eta() {
		System.out.println(nome + " ha "+ eta);
	}
	
	void saluta() {
		System.out.println("Ciao da " + nome);
	}
	
	void cammina() {
		System.out.println("Sto camminando...");
	}
	
	void stop() {
		System.out.println("Mi sono fermato");
	}
}
