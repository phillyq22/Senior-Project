import java.util.ArrayList;
import java.util.List;

public class Driver {
	
	public static void main (String[] args) {
		
		//DistanceCalculator dc = new DistanceCalculator();
		//System.out.println(dc.distance(-77.0532, 38.8589, -77.0533, 38.8572, "M"));
	
		Station s1 = new Station(1,-77.0532, 38.8589, .9);
		Station s2 = new Station(2, -77.0533, 38.8572, .5);
		Station s3 = new Station(3, -77.0492, 38.8564, .5);
		Station s4 = new Station(4, -77.0495, 38.8601, .7);
		Station s5 = new Station(5, -77.0594, 38.8578, .2);
		//System.out.println(s1.nec);
		/**
		 * (2, 8197.279333117633
		   (4, 8174.369282634508
		   (3, 8172.094288372427
		 */
		/**
		Station s0 = new Station(1,0,0);
		Station s1 = new Station(2, 0, 2);
		Station s2 = new Station(3, 0, 1);
		Station s3 = new Station(4, 0, 8);
		Station s4 = new Station(5, 0, 4);
		*/
		List<Station> sl = new ArrayList<Station>();
		sl.add(s1);
		sl.add(s2);
		sl.add(s3);
		sl.add(s4);
		sl.add(s5);
		BikeAlg ba = new BikeAlg();
		EndLocation loc = new EndLocation(-77.0512, 38.8588);
		double d = 0.3;//5
		/**
		ba.preProcess(sl);
		ba.getSuggest(s1, d);
		//System.out.println(s0.sortedAdj);
		System.out.println("Stations within: " + d + " miles");
		System.out.println();
		System.out.println("Ordered by ascending distance");
		for(int i = 0; i < ba.getWithin(s1, d); i++) {
			System.out.println(s1.sortedAdj.get(i));
		}
		System.out.println();
		System.out.println("Ordered by descending priority");

		for(int i = 0; i < s1.sortedSug.size(); i++) {
			System.out.println(s1.sortedSug.get(i));
		}
		//[2,4,3] vs. [3,4,2]
		/**
		Station[] statArray = new Station[]{ s0,s1,s2,s3,s4}; 
		BikeAlg ba = new BikeAlg();
		ba.preProcess(statArray);
		int[] retArr = ba.getWithin(s0, .3);
		int[] retArr1 = ba.getSuggest(s0, .3);
		for(int i = 0; i < s0.sortedAdj.length; i++) {
			System.out.println(s0.sortedAdj[i].stationID + ", " + s0.sortedAdj[i].dist + ", " + s0.sortedAdj[i].prio);
		}
		for(int i = 0; i < retArr.length; i++) {
			System.out.println(retArr[i]);
		}
		System.out.println("---------");
		for(int i = 0; i < retArr.length; i++) {
			
			System.out.println(retArr1[i]);
		}
		*/
		
		ba.preProcessS(sl, loc);
		ba.getSuggestS(loc, d);
		
		System.out.println("Stations within: " + d + " miles");
		System.out.println();
		System.out.println("Ordered by ascending distance");
		for(int i = 0; i < ba.getWithinS(loc, d); i++) {
			System.out.println(loc.sortedAdj.get(i));
		}
		
		System.out.println();
		System.out.println("Ordered by descending priority");

		for(int i = 0; i < loc.sortedSug.size(); i++) {
			System.out.println(loc.sortedSug.get(i));
		}
	}
}
