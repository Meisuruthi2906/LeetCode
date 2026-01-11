import java.util.*;
class Solution {
    public long countPairs(String[] words) {
        Map<String, Integer> map=new HashMap<>();
        for(String word:words){
            String key=getKey(word);
            map.put(key,map.getOrDefault(key,0)+1);
        }
        long result=0;
        for(int count:map.values()){
            result+=(long)count*(count-1)/2;}
        return result;
    }
    private String getKey(String word){
        StringBuilder sb=new StringBuilder();
        char first=word.charAt(0);
        for(char c:word.toCharArray()){
            int diff =(c-first+26)%26;
            sb.append(diff).append('.');
        }
        return sb.toString();
    }
}