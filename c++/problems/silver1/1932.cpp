#include <bits/stdc++.h>
using namespace std;

int triangle_dp[501][501];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            int max_num, cur_num;
            max_num = max(triangle_dp[i-1][j], triangle_dp[i-1][j-1]);
            
            cin >> cur_num;

            triangle_dp[i][j] = cur_num + max_num;
        }
    }

    cout << *max_element(triangle_dp[n]+1, triangle_dp[n]+n+1);
}