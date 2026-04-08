class Solution {
    public List<String> letterCombinations(String digits) {
        String[] letters={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        ArrayList<String> arr=new ArrayList<>();
        combinations(0,new StringBuilder(),digits,letters,arr);
        return arr;
    }
    static void combinations(int i,StringBuilder sb,String in,String[] letters,ArrayList<String> arr){
        if(i==in.length()){
            arr.add(sb.toString());
            return;
        }
        String key=letters[in.charAt(i)-'0'];
        for(int j=0;j<key.length();j++){
            sb.append(key.charAt(j));
            combinations(i+1,sb,in,letters,arr);
            sb.deleteCharAt(sb.length()-1);
        }
    }
}
