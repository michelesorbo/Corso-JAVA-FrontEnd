package base;

import java.util.InputMismatchException;
import java.util.Scanner;

public class tryCatch_es {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		try {
			System.out.println("Dammi due numeri e te li divido");
			
			System.out.println("Dammi il primo numero");
			int x = scanner.nextInt();
			
			System.out.println("Dammi il secondo numero");
			int y = scanner.nextInt();
			
			int result = x/y;
			System.out.println("Risultato: "+ result);
		}catch(ArithmeticException e) {
			System.out.println("Non puoi divedere un numero per zero - "+ e);
		}catch(InputMismatchException e) {
			System.out.println("Non puoi dividere un numero per una stringa");
		}
		
		
		
		System.out.println("\n\nProgramma terminato");

	}

}
