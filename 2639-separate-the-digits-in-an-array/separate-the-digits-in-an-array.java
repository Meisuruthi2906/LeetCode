class Solution {
    public int[] separateDigits(int[] nums) {
        int n = nums.length;
        List<Character> list = new ArrayList<>();
        for(int i=0;i<n;i++){
            int num = nums[i];
            String str = Integer.toString(num);
            for(int j=0;j<str.length();j++){
                list.add(str.charAt(j));
            }
        }
        int[] res = new int[list.size()];
        for(int i=0;i<res.length;i++){
            res[i] = Character.getNumericValue(list.get(i));
        }
        return res;
    }
}