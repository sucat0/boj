#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    deque<int> deq;
    int n;

    cin >> n;

    while (n--){
        string command;
        cin >> command;

        if (command == "push_front"){
            int x;
            cin >> x;

            deq.push_front(x);
        }
        else if (command == "push_back"){
            int x;
            cin >> x;

            deq.push_back(x);
        }
        else if (command == "pop_front"){
            if (deq.empty()) {
                cout << -1 << '\n';
                continue;
            }

            cout << deq.front() << '\n';
            deq.pop_front();
        }
        else if (command == "pop_back"){
            if (deq.empty()) {
                cout << -1 << '\n';
                continue;
            }

            cout << deq.back() << '\n';
            deq.pop_back();
        }
        else if (command == "size"){
            cout << deq.size() << '\n';
        }
        else if (command == "empty"){
            cout << deq.empty() << '\n';
        }
        else if (command == "front"){
            if (deq.empty()) {
                cout << -1 << '\n';
                continue;
            }

            cout << deq.front() << '\n';
        }
        else {
            if (deq.empty()) {
                cout << -1 << '\n';
                continue;
            }
            
            cout << deq.back() << '\n';
        }
    }
    
}