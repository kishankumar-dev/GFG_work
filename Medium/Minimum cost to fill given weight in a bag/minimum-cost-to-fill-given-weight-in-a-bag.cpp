//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &A, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A) {
        for (int i = 0; i < A.size(); i++) {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
  public:
    int dp[300][300];
    int solve(int ind, int w, int n, vector<int> &cost)
    {
        if(w < 0) return 1e9;
        if(w == 0) return 0;
        if(ind == n) return 1e9;
        int ans = 1e9;
        if(dp[ind][w] != -1) return dp[ind][w];
        ans = min(ans, solve(ind + 1, w, n, cost));
        ans = min(ans, cost[ind] + solve(ind, w - (ind+1), n, cost));
        ans = min(ans, cost[ind] + solve(ind+1, w-(ind+1), n, cost));
        return dp[ind][w] = ans;
    }
    int minimumCost(int n, int w, vector<int> &cost) {
        memset(dp, -1, sizeof(dp));
        int ans = solve(0, w, n, cost);
        if(ans >= 1e9) return -1;
        return ans;
    }
};




//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        int w;
        scanf("%d", &w);

        vector<int> cost(n);
        Array::input(cost, n);

        Solution obj;
        int res = obj.minimumCost(n, w, cost);

        cout << res << endl;
    }
}

// } Driver Code Ends