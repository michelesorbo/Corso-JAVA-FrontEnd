package base;

import java.util.Random;
import java.util.Scanner;

public class morra_cinese {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Gioca alla morra cinese con il PC
		//Il sistema esce quando viene scritto fine
		//L'utente deve inserire Carta, Forbici o Sasso (non importa minuscole o maiscole)
		//Quando facci un lancio devo conoscere l'esito (Vinto, Perso, Paraggio)
		//Quado finisco il gioco devo conoscere quate partite ho fatto e quante volte ho vinto perso o pareggiato
		
		System.out.println("Giochiamo alla marra cinese, scrivi Carta, Sasso o Forbici.\nScrivi fine per termminare.");
		
		

	}
	
	public static int esito(String giocata) {
		//i ritorni sono:
		//1 Vinto
		//2 Perso
		//0 Pareggio
		
		Random rm = new Random();
		
		String[] simboli = {"Carta", "Sasso", "Forbici"}; //Array delle scelte
		
		return 0;
	}

}
