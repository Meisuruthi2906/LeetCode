/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int[] arr;
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        dfs(root,list);
        arr = new int[list.size()];
        int idx=0;
        for(int val: list){
            arr[idx++]=val;
        }
        return balance(0,arr.length-1);
    }
    private TreeNode balance(int start, int end){
        if(end<start)return null;
        int mid = (start+end)/2;
        TreeNode node = new TreeNode(arr[mid]);
        node.left=balance(start,mid-1);
        node.right = balance(mid+1,end);
        return node;
    }
    private void dfs(TreeNode root, List<Integer> list){
        if(root==null)return;
        dfs(root.left,list);
        list.add(root.val);
        dfs(root.right,list);
    }
}