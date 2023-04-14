#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int piece = 0;
    string input;
    bool laser = true;
    stack<bool> iron;

    cin >> input;

    for (auto bracket : input){
        if (bracket == '('){
            iron.push(true);
            laser = true;
        }
        else {
            if (laser){
                piece += iron.size()-1;
                laser = false;
            }
            else {
                piece++;
            }

            iron.pop();
        }
    }

    cout << piece;
}