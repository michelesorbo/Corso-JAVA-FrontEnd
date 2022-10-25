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
		
		Scanner scanner = new Scanner(System.in);
		int vittorie = 0, pareggi = 0, sconfitte = 0, giocate = 0;
		String scelta;
		
		System.out.println("Giochiamo alla marra cinese, scrivi Carta, Sasso o Forbici.\nScrivi fine per termminare.");
		
		do {
			System.out.println("Fai la tua scelta: Sasso - Carta - Forbici\nFine per terminare");
			scelta = scanner.nextLine();
			
			if(scelta.toLowerCase().equals("carta") || scelta.toLowerCase().equals("sasso") || scelta.toLowerCase().equals("forbici")) {
				if(esito(scelta) == 0) {
					System.out.println("Preggio");
					pareggi++;
					giocate++;
				}else if(esito(scelta) == 1) {
					System.out.println("Hai Vinto");
					vittorie++;
					giocate++;
				}else {
					System.out.println("Hai Perso");
					sconfitte++;
					giocate++;
				}
			}else {
				System.out.println("Scelta non valida ritenta");
			}
			
		}while(!scelta.toLowerCase().equals("fine"));
		
		
		System.out.println("Hai fatto "+ giocate + " giocate");
		System.out.println("Hai vinto "+ vittorie + " volte");
		System.out.println("Hai perso "+ sconfitte + " volte");
		System.out.println("Hai pareggiato "+ pareggi + " volte");
		

	}
	
	public static int esito(String giocata) {
		//i ritorni sono:
		//1 Vinto
		//2 Perso
		//0 Pareggio
		
		Random rm = new Random();
		
		String[] simboli = {"carta", "sasso", "forbici"}; //Array delle scelte
		
		String computer = simboli[rm.nextInt(3)]; //Scelgo la giocata Randomica del pc
		
		System.out.println("Computer: " + computer); //Stampare a video la giocata del computer
		
		if(giocata.toLowerCase().equals(computer)){
			return 0; //Pareggio
		}else if(giocata.toLowerCase().equals("forbici") && computer.equals("carta") || giocata.toLowerCase().equals("sasso") && computer.equals("forbici") || giocata.toLowerCase().equals("carta") && computer.equals("sasso")) {
			return 1; //Vittoria
		}else {
			return 2; //Sconfitta
		}
			
	}

}
