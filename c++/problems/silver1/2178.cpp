#include <bits/stdc++.h>
using namespace std;


int dist[101][101];
string maze[101];


int main(void){
    int n, m;

    cin >> n >> m;

    for (int i = 0; i < n; i++)
        cin >> maze[i];

    int dir_x[4] = {0, 1, 0, -1};
    int dir_y[4] = {1, 0, -1, 0};

    queue<pair<int, int>> bfs_queue;
    bfs_queue.push({0, 0});
    dist[0][0] = 1;

    while (!bfs_queue.empty()){
        pair<int, int> node = bfs_queue.front();
        bfs_queue.pop();

        for (int i = 0; i < 4; i++){
            int x = node.first + dir_x[i];
            int y = node.second + dir_y[i];

            if (x < 0 || x >= n || y < 0 || y >= m) continue;
            if (dist[x][y] > 0 || maze[x][y] == '0') continue;

            dist[x][y] = dist[node.first][node.second] + 1;
            bfs_queue.push({x, y});
        }
    }
    cout << dist[n-1][m-1];
}