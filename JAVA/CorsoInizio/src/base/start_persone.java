package base;

public class start_persone {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Auto a1 = new Auto();
		Persona p1 = new Persona("Michele", "Sorbo", 43, "Caserta"); //Oggetto di tipo persona Si chiama istanza
		Persona p2 = new Persona("Vittorio", "Lama", 24, "Napoli");
		Persona p3 = new Persona("Luca", "Torre");
		
		a1.muovi();
		a1.ferma();
		
		p1.eta();
		p2.eta();
		p3.eta();
		
		//p3.eta = 19; //Sbagliata ma per ora va bene si fa con i metodi get e set
		p3.setEta(19);
		
		p3.eta();
		
		//p1.nome = "Mauro";
		
		p1.saluta();
	
	
	}

}
