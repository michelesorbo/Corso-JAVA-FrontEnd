package lezione04;
import base.*;

public class Polimorfismo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Studenti st1 = new Studenti("Vittorio", "Lama", 24, "Napoli", "JAVA");
		Studenti st2 = new Studenti("Mario", "Rossi", 23, "Milano", "JAVA");
		Docenti dc1 = new Docenti("Michele", "Sorbo", 43, "Caserta", "Informatica");
		
		Persone[] classe = {st1, st2, dc1};
		
		for(Persone persona : classe) {
			persona.saluta();
			persona.getEta();
		}

	}

}
