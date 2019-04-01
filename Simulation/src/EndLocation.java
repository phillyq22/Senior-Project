import java.util.ArrayList;
import java.util.List;

public class EndLocation {
	public String name;
	public double x;
	public double y;
	public List<Pair> sortedAdj; //INDEXES DO NOT MAP TO STATION IDS IN THIS ARRAY
	public List<SugPair> sortedSug;
	
	public EndLocation(double x, double y) {
		this.x= x;
		this.y =y;
		sortedAdj = new ArrayList<Pair>();
		sortedSug = new ArrayList<SugPair>();
	}
	
	
}
