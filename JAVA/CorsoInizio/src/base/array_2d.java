package base;

public class array_2d {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		//Creare un array per i nomi di 5 bambini in 3 classi
		
		String[][] classi = new String[3][3];
		
		classi[0][0] = "Primo bambino della prima classe";
		classi[0][1] = "Secondo bambino della prima classe";
		classi[0][2] = "Terzo bambino della prima classe";
		classi[1][0] = "Primo Bambino della seconda classe";
		classi[2][0] = "Primo Bambino della terza classe";
		
		for(int i = 0; i < classi.length; i++) {
			for(int j = 0; j < classi[i].length; j++) {
				System.out.println(classi[i][j]);
			}
			System.out.println("");
		}
	}

}
