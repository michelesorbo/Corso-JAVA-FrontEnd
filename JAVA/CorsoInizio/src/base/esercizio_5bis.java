package base;

import java.util.InputMismatchException;
import java.util.Scanner;

public class esercizio_5bis {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int ar[] = new int[5];
		int i, num, pos;
		
		try {
			System.out.println("ins. num: ");
			num = in.nextInt();
			System.out.println("Ins. pos: ");
			pos = in.nextInt();
			
			ar[pos] = num;
			
		}catch(InputMismatchException e) {
			System.out.println("Puoi inserire solo numeri");
		}catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("Le posizioni dell'array sono da 0 a 4");
		}catch(Exception e){
			System.out.println("Errore generico: " + e);
		}
		
		
		for(int el:ar) {
			System.out.println(el);
		}
	}

}
