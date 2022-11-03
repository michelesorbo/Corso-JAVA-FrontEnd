package es_interface;

public class Pesce implements Predatore, Preda{

	@Override
	public void scappa() {
		// TODO Auto-generated method stub
		System.out.println("Nuoto via velocemnte");
		
	}

	@Override
	public void caccia() {
		// TODO Auto-generated method stub
		System.out.println("Nuoto lentamente verso la preda");
		
	}

}
