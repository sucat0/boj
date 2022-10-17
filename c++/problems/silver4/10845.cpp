#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<int> q;
    int n, x;
    string command;

    cin >> n;

    while (n--){
        cin >> command;

        if (command == "push"){
            cin >> x;
            q.push(x);
        }
        else if (command == "pop"){
            if (q.empty()){
                cout << -1 << '\n';
            }
            else {
                cout << q.front() << '\n';
                q.pop();
            }
        }
        else if (command == "size"){
            cout << q.size() << '\n';
        }
        else if (command == "empty"){
            cout << q.empty() << '\n';
        }
        else if (command == "front"){
            if (q.empty()) cout << -1 << '\n';
            else cout << q.front() << '\n';
        }
        else {
            if (q.empty()) cout << -1 << '\n';
            else cout << q.back() << '\n';
        }
    } 
}