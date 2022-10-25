package base;

public class array_class {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] ar = new int[3]; //Array Vuoto di 3 elementi
		
		int[] ra_numeri = {1,58,23,65}; //Array con 4 elementi numerici
		
		ar[0] = 11;
		ar[1] = 24;
		ar[2] = 3;
		
		String[] simboli = {"Carta", "Sasso", "Forbici"};
 
		//System.out.println(ra_numeri.length);
		
		//Stampare tutti gli ementi di un array?
//		for(int i = 0; i < ra_numeri.length; i++) {
//			System.out.println(ra_numeri[i]);
//		}
		
		//Tipo for each (For abbreviato)
		for(String el:simboli) {
			System.out.println(el);
		}
		
		
		for(int i = 0; i < simboli.length; i++) {
			System.out.println(simboli[i]);
		}
		
		
	}

}
