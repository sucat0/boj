#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (1){
        string line;
        stack<bool> braket;
        bool balance = true;

        getline(cin, line);

        if (line == ".") break;

        for (auto letter : line){
            if (letter == '('){
                braket.push(1);
            }
            else if (letter == '['){
                braket.push(0);
            }
            else if (letter == ')'){
                if (braket.top()) braket.pop();
                else {
                    balance = false;
                    break;
                }
            }
            else if (letter == ']'){
                if (!braket.top()) braket.pop();
                else {
                    balance = false;
                    break;
                }
            }
        }

        if (balance) cout << "yes" << '\n';
        else cout << "no" <<'\n';
    }
}