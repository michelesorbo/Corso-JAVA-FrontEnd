package es_interface;

import java.util.Scanner;

public class Distributori implements Comparable {
	
	private String citta;
	private String proprietario;
	private int capacita;
	private String TipoBenzina;
	private double CostoLitro;
	//ArrayList per il calcolo dell'incasso giornaliero
	
	Scanner in = new Scanner(System.in);
	
	Distributori(String citta, String proprietario, int capacita, String TipoBenzina, double CostoLitro){
		this.citta = citta;
		this.proprietario = proprietario;
		this.capacita = capacita;
		this.TipoBenzina = TipoBenzina;
		this.CostoLitro = CostoLitro;
	}
	
	void start() {
		System.out.println("Scegli l'operazione da compiere");
		System.out.println("1) Rifornimento\n2) Rifornimento Pompa\n3) Incasso Giornaliero\n4) Comparazione");
		
	}
	
	void Rifornimento(int litri) {
		capacita = capacita - litri;
	}
	
	void RifornimentoPompa(int litri) {
		capacita = capacita + litri;
	}

	@Override
	public int compareTo(Distributori h) {
		// TODO Auto-generated method stub
		return (this.capacita - h.capacita);
	}

}
