package base;

public class ereditarieta_start {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Persone persona1 = new Persone("Michele", "Sorbo", 43, "Caserta");
		Docenti docente1 = new Docenti("Vittorio", "Lama", 24, "Mapoli", "Inglese");
		Studenti st1 = new Studenti("Simone", "Biascioli", 22, "Napoli", "5A");
		studentiPrivatisti stp1 = new studentiPrivatisti("Federico", "Padulano", 19, "Napoli", "5C", "Torre");
	
		
		persona1.saluta();
		docente1.saluta();
		st1.saluta();
		stp1.saluta();
		st1.getEta();
		stp1.getEta();
		docente1.getEta();

	}

}
