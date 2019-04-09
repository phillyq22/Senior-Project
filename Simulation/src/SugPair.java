
public class SugPair implements Comparable<SugPair>{
	 public Station station;
	  public double sug;
	  
	  public SugPair(Station station, double sug){
		    this.station = station;
		    this.sug = sug; 
		  }
	  
	  public int compareTo(SugPair pair){
		  
		  if(this.sug - pair.sug > 0) {
			  return 1;
		  }
		  if(this.sug- pair.sug == 0) {
			  return 0;
		  }
		  return -1;
	  }
	  
	  public String toString() {
		  String tostring =  "(" + station.id + ", " + sug + ")";
		  return tostring;
	  }
}
