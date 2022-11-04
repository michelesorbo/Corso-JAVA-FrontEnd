package lezione04;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class GestioneDelleDate {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		//Data Corrente
		LocalDate data = LocalDate.now();
		System.out.println(data);
		
		//Ora Corrente
		LocalTime ora = LocalTime.now();
		System.out.println(ora);
		
		//Data + ora
		LocalDateTime data_completa = LocalDateTime.now();
		System.out.println(data_completa);
		
		DateTimeFormatter it_format = DateTimeFormatter.ofPattern("dd/MM/yyyy");
		System.out.println("Data in formato italiano " + data.format(it_format));
		
		//Faccio scrivere il mese con il nume del mese
		DateTimeFormatter it_format_mese = DateTimeFormatter.ofPattern("dd - MMMM - yyyy");
		System.out.println("Data in formato italiano " + data.format(it_format_mese));
		
		//Faccio scrivere il giorno con il nome
		DateTimeFormatter it_format_giorno = DateTimeFormatter.ofPattern("EEEE, dd MMMM yyyy");
		System.out.println("Data in formato italiano " + data.format(it_format_giorno));
		
		//Faccio scrivere il mese con il nume del mese
		DateTimeFormatter it_format_ora = DateTimeFormatter.ofPattern("EEEE, dd MMMM yyyy - HH:mm");
		System.out.println("Data in formato italiano " + data_completa.format(it_format_ora));
		
	}

}
