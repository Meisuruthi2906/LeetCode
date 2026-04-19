class Solution 
{
    public int maxDistance(int[] nums1, int[] nums2) 
    {
        int i=0;
        int j=0;
        int len1=nums1.length;
        int len2=nums2.length;
        int ans=0;
        while(i<len1 && j<len2)
        {
            if(i>j)
            {
                j++;
                continue;
            }

            if(nums1[i]<=nums2[j])
            {
                ans=Math.max(ans, j-i);
                j++;
            }
            else
            {
                i++;
            }
        }    
        return ans;
    }
}