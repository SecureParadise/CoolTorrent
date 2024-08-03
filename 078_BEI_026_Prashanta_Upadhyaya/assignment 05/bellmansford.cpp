 //Network Delay Time
 class Solution {

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n+1, INT_MAX);
        dist[k]=0;
        for(int i=0; i<n;i++){
            for (vector<int> e : times) {
                int s = e[0], d = e[1], w = e[2];
                if(dist[s]!=INT_MAX && dist[d]>dist[s]+w){
                    dist[d] = dist[s] + w;
                }
            }
        }

        int maxw = 0;
        for (int i = 1; i <= n; i++)
            maxw = max(maxw, dist[i]);
        return maxw == INT_MAX ? -1 : maxw;
    }
};