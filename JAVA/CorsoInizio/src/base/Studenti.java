package base;

public class Studenti extends Persone {
	
	String classe;

	public Studenti(String nome, String cognome, int eta, String citta, String classe) {
		super(nome, cognome, eta, citta);
		this.classe = classe;
	}
	
	public void Frequenta() {
		System.out.println("Frequento la classe: " + classe);
	}
	
	public void saluta() {
		System.out.println("Piacere sono lo studente " + nome);
	}
	

}
