#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    string command;
    stack<int> s;

    cin >> n;
    
    while (n--){
        cin >> command;

        if (command == "push"){
            cin >> x;
            s.push(x);
        }
        else if (command == "pop"){
            if (s.empty()){
                cout << -1 << '\n';
            }
            else {
                cout << s.top() << '\n';
                s.pop();
            }
        }
        else if (command == "size"){
            cout << s.size() << '\n';
        }
        else if (command == "empty"){
            cout << s.empty() << '\n';
        }
        else if (command == "top"){ 
            if (s.empty()) cout << -1 << '\n';
            else cout << s.top() << '\n';
        }
    }
}