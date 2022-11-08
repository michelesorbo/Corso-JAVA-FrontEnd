package DataBase;

import  java.sql.*;

public class Es_Studenti {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			//Creaimo la connessione al Data Base
			String Driver = "com.mysql.cj.jdbc.Driver"; //Drivere di J/Connect
			String DBURL = "jdbc:mysql://localhost:8889/corso";
			Class.forName(Driver);
			Connection con = DriverManager.getConnection(DBURL, "root", "root");
			
			//Creiamo la Query
	  		String query = "SELECT * FROM studenti"; //Query di selezione
	  		
	  		//Creaiamo lo statement
	  		Statement st = con.createStatement();
	  		
	  		//Eseguo la query
	  		ResultSet rs = st.executeQuery(query);
	  		
	  		//Stamapre i risultati della query
	  		while(rs.next()) {
	  			String nome = rs.getString("nome");
	  			String cognome = rs.getNString("cognome");
	  			Date dataNascita = rs.getDate("data_nascita");
	  			
	  			//Stampo a video il sirusltato
	  			System.out.println(nome + " " + cognome + " " + dataNascita);
	  		}
	  		st.close();
			
		}catch(Exception e) {
			System.err.println("Got an exception! ");
		    System.err.println(e.getMessage());
		}

	}

}
