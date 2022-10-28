package base;

public class prodotti {
	
	private String cBarre;
	int prezzo;
	String descrizione;
	
	prodotti(String cBarre, int prezzo, String descrizione){
		this.cBarre = cBarre;
		this.prezzo = prezzo;
		this.descrizione = descrizione;
		
	}
	
	//Ritorno l'attributo cBarre
	String getCBarre() {
		return cBarre;
	}
	
	void setCBarre(String newBarre) {
		cBarre = newBarre;
		System.out.println("Modifica avvenuta");
	}

}
