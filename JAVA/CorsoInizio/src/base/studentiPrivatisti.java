package base;

public class studentiPrivatisti extends Studenti {
	
	String istituto;

	studentiPrivatisti(String nome, String cognome, int eta, String citta, String classe, String Istituto) {
		super(nome, cognome, eta, citta, classe);
		this.istituto = istituto;
	}
	
	@Override
	public void saluta() {
		System.out.println("Sono lo studente privatista " + nome);
	}
	
	@Override
	public void getEta() {
		System.out.println("non ti voglio dire la mia età");
	}

}
