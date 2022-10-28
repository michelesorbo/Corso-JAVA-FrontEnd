package base;

public class Docenti extends Persone {
	
	String materiaInsegnata;

	Docenti(String nome, String cognome, int eta, String citta, String materiaInsegnata) {
		super(nome, cognome, eta, citta); //Richiamo il costruttore del padre
		this.materiaInsegnata = materiaInsegnata;
		
	}
	
	void Insegna() {
		System.out.println("Sono il docente della materia: " + materiaInsegnata);
	}
	
	@Override
	void saluta() {
		System.out.println("Ciao sono l'insegnante di " + materiaInsegnata);
	}

}
