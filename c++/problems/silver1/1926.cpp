#include <bits/stdc++.h>
using namespace std;


bool canvas[501][501];
bool visited[501][501];


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int dir_x[4] = {1, 0, -1, 0}, dir_y[4] = {0, 1, 0, -1};
    int n, m;

    cin >> n >> m;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> canvas[i][j];
        }
    }

    int paint_num = 0, max_size = 0;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (!canvas[i][j] || visited[i][j]) continue;

            int size = 0;

            paint_num++;
            visited[i][j] = 1;

            queue<pair<int, int>> bfs_queue;
            bfs_queue.push({i, j});

            while (!bfs_queue.empty()){
                size++;
                pair<int, int> node = bfs_queue.front();
                bfs_queue.pop();

                for (int k = 0; k < 4; k++){
                    int x = node.first + dir_x[k];
                    int y = node.second + dir_y[k];

                    if (x < 0 || x >= n || y < 0 || y >= m) continue;
                    if (!canvas[x][y] || visited[x][y]) continue;

                    visited[x][y] = 1;
                    bfs_queue.push({x, y});
                }
            }

            max_size = max(max_size, size);
        }
    }

    cout << paint_num << '\n' << max_size; 
}