class Solution {
    public boolean canReach(int[] arr, int start) {
        
        int n = arr.length;

 
        boolean[] visited = new boolean[n];

        Queue<Integer> queue = new LinkedList<>();

        queue.offer(start);

        while (!queue.isEmpty()) {

            int current = queue.poll();

            if (visited[current]) {
                continue;
            }
            if (arr[current] == 0) {
                return true;
            }

            visited[current] = true;

            int left = current - arr[current];
            if (left >= 0) {
                queue.offer(left);
            }

            int right = current + arr[current];
            if (right < n) {
                queue.offer(right);
            }
        }

        return false;
    }
}