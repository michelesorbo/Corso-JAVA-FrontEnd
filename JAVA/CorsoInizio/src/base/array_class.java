package base;

import java.util.Random;
import java.util.Scanner;

public class array_class {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		Random rm = new Random();
		
		String[] simboli = {"Carta", "Sasso", "Forbici"}; //Array di stinghe
		
		int[] ar = new int[3]; //Array Vuoto di 3 elementi
		
		int[] ra_numeri = {1,58,23,65}; //Array con 4 elementi numerici
		
		//Insericsco elementi in array
		ar[0] = 11;
		ar[1] = 24;
		ar[2] = 3;
		
		ra_numeri[1] = 12;
		
		System.out.println("Inserisci il nuvo valora alla prima posizione dell'arrai ar");
		//Inserire elemnti nell'array
		for(int i = 0; i < ar.length; i++) {
			System.out.println("Inserisci il valoe all'indice "+i);
			ar[i] = scanner.nextInt();
		}
		
		System.out.println("Stampo nuovo array");
		
		//Stamppo a video gli elementi dell'arry
		for(int el:ar) {
			System.out.println(el);
		}

 
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
		
		System.out.println("è uscito "+ simboli[rm.nextInt(3)]);
		
		
	}

}
