#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    while (n--){
        string keylog;
        list<char> password;
        list<char>::iterator cursor;
        cursor = password.begin();

        cin >> keylog;

        for (auto key : keylog){
            if (key == '<'){
                if (cursor != password.begin()) cursor--;
            }
            else if (key == '>'){
                if (cursor != password.end()) cursor++;
            }
            else if (key == '-'){
                if (cursor != password.begin()) cursor = password.erase(--cursor);
            }
            else {
                password.insert(cursor, key);
            }
        }

        for (auto word : password) cout << word;

        cout << '\n';
    }
}