package DBPa;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.*;

public class test2 {
	
	public static void main(String[] args)
	  {
	    try
	    {
	      // create our mysql database connection
	      String myDriver = "org.gjt.mm.mysql.Driver";
	      String myUrl = "jdbc:mysql://localhost/test";
	      Class.forName(myDriver);
	      Connection conn = DriverManager.getConnection(myUrl, "root", "");
	      
	      // our SQL SELECT query. 
	      // if you only need a few columns, specify them by name instead of using "*"
	      String query = "SELECT * FROM users";

	      // create the java statement
	      Statement st = conn.createStatement();
	      
	      // execute the query, and get a java resultset
	      ResultSet rs = st.executeQuery(query);
	      
	      // iterate through the java resultset
	      while (rs.next())
	      {
	        int id = rs.getInt("id");
	        String firstName = rs.getString("first_name");
	        String lastName = rs.getString("last_name");
	        Date dateCreated = rs.getDate("date_created");
	        boolean isAdmin = rs.getBoolean("is_admin");
	        int numPoints = rs.getInt("num_points");
	        
	        // print the results
	        System.out.format("%s, %s, %s, %s, %s, %s\n", id, firstName, lastName, dateCreated, isAdmin, numPoints);
	      }
	      st.close();
	    }
	    catch (Exception e)
	    {
	      System.err.println("Got an exception! ");
	      System.err.println(e.getMessage());
	    }
	  }

}
