import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.TreeMap;

//assumes ID maps exactly to indexes of arrays
public class BikeAlg{
  DistanceCalculator dc = new DistanceCalculator();
  List<Station> stationList;
  public void preProcess(List<Station> stationList) {
	  this.stationList = stationList;
    for(int i = 0; i < stationList.size(); i++) {
      for(int j = 0; j <  stationList.size(); j++) {
        if(i != j) {          
          //calculate dist from stationList[i] --> stationList[j]
          double dist = dc.distance(stationList.get(i).x, stationList.get(i).y, stationList.get(j).x, stationList.get(j).y, "M");
        
          //create pair and store at sortedAdjacentIDs[j]
          Pair pair = new Pair(stationList.get(j), dist);
          //System.out.println(pair.dist);
          stationList.get(i).sortedAdj.add(pair);
        }
      }
      //sort stationList[i].sortedAdj
      Collections.sort(stationList.get(i).sortedAdj);
    }
  }

  public void preProcessS(List<Station> stationList, EndLocation loc) {
	  this.stationList = stationList;
	  for(int i = 0; i < stationList.size(); i++) {
		  double dist = dc.distance(stationList.get(i).x, stationList.get(i).y, loc.x, loc.y, "M");

		  //create pair and store at sortedAdjacentIDs[j]
		  Pair pair = new Pair(stationList.get(i), dist);
		  //System.out.println(pair.dist);
		  loc.sortedAdj.add(pair);
	  }
	//sort stationList[i].sortedAdj
      Collections.sort(loc.sortedAdj);
  }
  
  public void getSuggestS(EndLocation loc, double dist) {
	  for(int i = 0; i < loc.sortedAdj.size() && loc.sortedAdj.get(i).dist <= dist ; i++) {
			//System.out.println(s.sortedAdj.get(i).station.nec);
			double sug = loc.sortedAdj.get(i).prio*(10) + loc.sortedAdj.get(i).station.nec*(10)*loc.sortedAdj.get(i).station.nec*(10); //FIXIIFIXI
			SugPair sp = new SugPair(loc.sortedAdj.get(i).station, sug);
			// test distance s.sortedAdj.get(i).dist
			loc.sortedSug.add(sp);
			//s.sortedSug[i] = sp;
		}
	  Collections.sort(loc.sortedSug, Collections.reverseOrder());
  }
  
  //binary searches s.sortedAdj for dist, returns array of ids of all stations <= dist 
  public void getSuggest(Station s, double dist){
	/**
    int index = binarySearch(s.sortedAdj, 0, s.sortedAdj.length - 1, dist);
    int retArr[] = new int[index + 1];
    for(int i = index; i >= 0; i--){
    	//System.out.println(index);
    	retArr[i] = s.sortedAdj[i].stationID;
    }
    return retArr;
    */
	
	for(int i = 0; i < s.sortedAdj.size() && s.sortedAdj.get(i).dist <= dist ; i++) {
		//System.out.println(s.sortedAdj.get(i).station.nec);
		double sug = s.sortedAdj.get(i).prio*(10) + s.sortedAdj.get(i).station.nec*(10)*s.sortedAdj.get(i).station.nec*(10); //FIXIIFIXI
		SugPair sp = new SugPair(s.sortedAdj.get(i).station, sug);
		// test distance s.sortedAdj.get(i).dist
		s.sortedSug.add(sp);
		//s.sortedSug[i] = sp;
	}
	//Collections.sort(s.sortedSug);
	Collections.sort(s.sortedSug, Collections.reverseOrder());
    /**
    //ArrayList<>
    for(int i = 0; s.sortedAdj[i].dist <= dist; i++) {
    	
    }
    */
  }
  
  
  public int getWithin(Station s, double dist) {
	  int i = 0;
	  for(;i < s.sortedAdj.size() && s.sortedAdj.get(i).dist < dist; i++) {
			
	  }
	  return i;
  }
  
  public int getWithinS(EndLocation loc, double dist) {
	  int i = 0;
	  for(;i < loc.sortedAdj.size() && loc.sortedAdj.get(i).dist < dist; i++) {
		  
	  }
	  return i;
  }
  

}