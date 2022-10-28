package base;

public class es4_start {

	public static void main(String[] args) {
		prodotti pr1 = new prodotti("120034", 12, "Prodotto di eccellenza");
		
		System.out.println(pr1.getCBarre());
		pr1.setCBarre("00134");
		System.out.println(pr1.getCBarre());
	}

}
