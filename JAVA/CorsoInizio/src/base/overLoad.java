package base;

public class overLoad {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		somma(4,8);
		somma(3,6,8);
		somma(4.7,9);
		double ris = somma(4,6,9.8); //Non stampa nulla
		System.out.println(ris);
	}
	
	public static void somma(int a, int b) {
		int risultato = a + b;
		System.out.println("Primo " + risultato);
	}
	
	public static double somma(int a, int b, double c) {
		return a + b + c;
	}
	
	public static void somma(int a, int b, int c) {
		int risultato = a + b + c;
		System.out.println("Secondo " + risultato);
	}
	
	public static void somma(double a, double b) {
		double risultato = a + b;
		System.out.println("Terzo " + risultato);
	}
	

}
