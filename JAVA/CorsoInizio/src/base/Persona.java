package base;

public class Persona {

	//Attributi della classe Se li rendo tutti private vado ad incapsulare la classe
	private String nome;
	private String cognome;
	private int eta;
	private String citta;
	
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
	
	Persona(String nome, String cognome, int eta){
		this.nome = nome;
		this.cognome = cognome;
		this.eta = eta;
		this.citta = "";
	}
	
	Persona(String nome, String cognome, String citta){
		this.nome = nome;
		this.cognome = cognome;
		this.eta = 0;
		this.citta = citta;
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
	
	//Metodi Getters e Setters per incapsulamento della Classe
	//I metodi Get servono a restituire il valore di un attributo
	public int getEta() {
		return eta;
	}
	
	//I Metodi set servono a settare un attributo
	public void setEta(int eta) {
		this.eta = eta;
	}
	
	public String getCitta(){
		return citta;
	}
	
	public void setCitta(String citta) {
		this.citta = citta;
	}
	
}
