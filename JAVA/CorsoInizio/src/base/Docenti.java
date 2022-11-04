package base;

public class Docenti extends Persone {
	
	String materiaInsegnata;

	public Docenti(String nome, String cognome, int eta, String citta, String materiaInsegnata) {
		super(nome, cognome, eta, citta); //Richiamo il costruttore del padre
		this.materiaInsegnata = materiaInsegnata;
		
	}
	
	public void Insegna() {
		System.out.println("Sono il docente della materia: " + materiaInsegnata);
	}
	
	public void saluta() {
		System.out.println("Ciao sono l'insegnante di " + materiaInsegnata);
	}

}
