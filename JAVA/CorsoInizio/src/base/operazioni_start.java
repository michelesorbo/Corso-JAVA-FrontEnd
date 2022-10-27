package base;

public class operazioni_start {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Operazioni op1 = new Operazioni(5,9.6);
		Operazioni op2 = new Operazioni(3,5);
		
		//op1.somma(); //Metodo che non ritorna e stampa a video
		double div_op1 = op1.divisione(); //Metodo che ritorna il risultato 
		
		//System.out.println(div_op1);
		
		int[] ar_num = new int[10];
		int[] ar2 = new int[3];
		
		
		String[] str = new String[5];
		
		System.out.println(str.length);
		//System.out.println(ar_num.length);
//		ar_num = op1.riempi_ar(ar_num);
//		ar2 = op2.riempi_ar(ar2);//Riempire l'array
//		
//		
//		op2.stampa_ar(ar_num); //Stampo l'array
//		
//		op2.stampa_maggiore(ar_num);
		
		op1.lista_movimenti();

	}

}
