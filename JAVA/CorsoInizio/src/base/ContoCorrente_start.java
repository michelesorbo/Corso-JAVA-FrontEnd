package base;

import java.util.Scanner;

public class ContoCorrente_start {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		ContoCorrente cc1 = new ContoCorrente(50000, "Vittorio Lama", "IT001");
		int scelta, somma;
		
		do {
			System.out.println("Benvenuto nella gestione del conto corrente");
			System.out.println("\t1 - Vesamento\n\t2 - Prelievo\n\t3 - Saldo Attuale\n\t4 - Ultimi 5 movimenti\n\t5 - Info Conto\n\t0 - Esci");
			
			scelta = scanner.nextInt();
			
			if(scelta == 1) {
				System.out.println("Quanto vuoi versare?");
				somma = scanner.nextInt();
				cc1.versa(somma);
				
			}else if(scelta == 2) {
				System.out.println("Quanto vuoi prelevare?");
				somma = scanner.nextInt();
				cc1.preleva(somma);
				
			}else if(scelta == 3) {
				cc1.stampa_saldo();
				
			}else if(scelta == 4) {
				
				cc1.stampa_movimenti();
				
			}else if(scelta == 5) {
				
				cc1.info_conto();
				
			}else{
				
				System.out.println("Scelta non valida");
				
			}
		}while(scelta != 0);
		
		System.out.println("Sessione chiusa");
		
		

	}

}