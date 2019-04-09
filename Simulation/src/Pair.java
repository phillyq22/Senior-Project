public class Pair implements Comparable<Pair>{
  public Station station;
  public double dist;
  public double prio; //distance priority
 
   
  public Pair(Station station, double dist){ //fix according to that
    this.station = station;
    this.dist = dist; 
    prio = 1 - dist;
  }
  public int compareTo(Pair pair){
	  
		  if(this.dist - pair.dist > 0) {
			  return 1;
		  }
		  if(this.dist - pair.dist == 0) {
			  return 0;
		  }
		  return -1;
	  }
	  
  public String toString() {
	  String tostring =  "(" + station.id + ", " + dist + ")";
	  return tostring;
  }
  
  }

  


