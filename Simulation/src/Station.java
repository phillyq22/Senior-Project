import java.util.ArrayList;
import java.util.List;

public class Station {
  public double x, y;
  public int id;
  public double nec; //neccessity??
  public int bikesDis;
  public int bikesAvail;
  public int docsAvail;
  public int docSize;
  public int bikesGained;
  public int bikesLost;
  public List<Pair> sortedAdj; //INDEXES DO NOT MAP TO STATION IDS IN THIS ARRAY
  public List<SugPair> sortedSug;
  
  public Station(int id, double x, double y,double nec) { // int bikesAvail, int bikesDis, int docsAvail
	  this.id = id;
	  this.x = x;
	  this.y = y;
	  this.nec = nec;
	  this.bikesAvail = bikesAvail;
	  this.docsAvail = docsAvail;
	  this.docSize = docsAvail + bikesDis + bikesAvail;
	  sortedAdj = new ArrayList<Pair>();
	  sortedSug = new ArrayList<SugPair>();
  }
  
  
  public boolean stateChange(double nec, int bikesAvail, int bikesDis, int docsAvail) {
	  this.nec = nec;
	  this.bikesGained = bikesAvail = this.bikesAvail;
	  this.bikesAvail = bikesAvail;
	  this.bikesDis = bikesDis;
	  this.docsAvail = docsAvail;
	  
	  return true;
  }
  
  public String toString() {
	  return "";
  }
  
  
}