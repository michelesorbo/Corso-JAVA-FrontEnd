package base;

public class Studenti extends Persone {
	
	String classe;

	Studenti(String nome, String cognome, int eta, String citta, String classe) {
		super(nome, cognome, eta, citta);
		this.classe = classe;
	}
	
	void Frequenta() {
		System.out.println("Frequento la classe: " + classe);
	}
	
	@Override
	void saluta() {
		System.out.println("Piacere sono lo studente " + nome);
	}
	

}
