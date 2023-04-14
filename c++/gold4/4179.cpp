#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<pair<int, int>> F_bfs_queue;
    queue<pair<int, int>> J_bfs_queue;
    int dir_x[4] = {0, 1, 0, -1};
    int dir_y[4] = {1, 0, -1, 0};

    int r, c;
    string maze[1000];

    cin >> r >> c;

    int F_time[1001][1001];
    int J_time[1001][1001];
    for (int i = 0; i < r; i++){
        fill_n(F_time[i], c, -1);
        fill_n(J_time[i], c, -1);
    }

    for (int i = 0; i < r; i++){
        cin >> maze[i];
        for (int j = 0; j < c; j++){
            if (maze[i][j] == 'J'){
                J_bfs_queue.push({i, j});
                J_time[i][j] = 0;
            }
            if (maze[i][j] == 'F'){
                F_bfs_queue.push({i, j});
                F_time[i][j] = 0;
            }
        }
    }

    while (!F_bfs_queue.empty()){
        pair<int, int> F_bfs_node = F_bfs_queue.front();
        F_bfs_queue.pop();
        
        for (int i = 0; i < 4; i++){
            int x = F_bfs_node.first + dir_x[i];
            int y = F_bfs_node.second + dir_y[i];
            int prev_time = F_time[F_bfs_node.first][F_bfs_node.second];

            if (x < 0 || x >= r || y < 0 || y >= c) continue;
            if (F_time[x][y] != -1 || maze[x][y] == '#') continue;

            F_bfs_queue.push({x, y});
            F_time[x][y] = prev_time + 1;
        }
    }

    while (!J_bfs_queue.empty()){
        pair<int, int> J_bfs_node = J_bfs_queue.front();
        J_bfs_queue.pop();

        for (int i = 0; i < 4; i++){
            int x = J_bfs_node.first + dir_x[i];
            int y = J_bfs_node.second + dir_y[i];
            int prev_time = J_time[J_bfs_node.first][J_bfs_node.second];

            if (x < 0 || x >= r || y < 0 || y >= c) {
                cout << prev_time + 1;
                return 0;
            }
            if (J_time[x][y] != -1 || maze[x][y] == '#') continue;
            if (F_time[x][y] != -1 && prev_time+1 >= F_time[x][y]) continue;

            J_bfs_queue.push({x, y});
            J_time[x][y] = prev_time + 1;
        }
    }
    cout << "IMPOSSIBLE";
}