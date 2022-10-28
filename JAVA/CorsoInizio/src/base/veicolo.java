package base;

public abstract class veicolo {
	
	abstract void muovi();
	abstract void ferma();
	abstract void ruote();
	
	void marca() {
		System.out.println("Saluta");
	}
	
}
