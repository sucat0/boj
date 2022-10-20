#include <bits/stdc++.h>
using namespace std;


int main(void){
    queue<tuple<int, int, int>> bfs_queue;
    int dir_x[4] = {1, 0, -1, 0};
    int dir_y[4] = {0, 1, 0, -1};

    int tomato[1001][1001];
    int n, m;

    cin >> m >> n;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> tomato[i][j];

            if (tomato[i][j] == 1) bfs_queue.push({i, j, 0});
        }
    }

    int count;

    while (!bfs_queue.empty()){
        tuple<int, int, int> node = bfs_queue.front();
        bfs_queue.pop();

        for (int i = 0; i < 4; i++){
            int x = get<0>(node) + dir_x[i];
            int y = get<1>(node) + dir_y[i];

            if (x < 0 || x >= n || y < 0 || y >= m) continue;
            if (tomato[x][y] != 0) continue;

            bfs_queue.push({x, y, get<2>(node)+1});
            tomato[x][y] = 1;
        }
        
        count = get<2>(node);
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (tomato[i][j] == 0){
                cout << -1;
                return 0;
            }
        }
    }

    cout << count;
}