#include <bits/stdc++.h>
using namespace std;


int main(void){
    list<char> editor;
    list<char>::iterator cursor = editor.begin();
    string start;
    int m;
    char command, word;

    cin >> start;
    cin >> m;

    for (auto i : start){
        editor.push_back(i);
    }
    cursor = editor.end();

    while (m--){
        cin >> command;

        if (command == 'L'){
            if (cursor != editor.begin()) cursor--;
        }
        else if (command == 'D'){
            if (cursor != editor.end()) cursor++;
        }
        else if (command == 'B'){
            if (cursor != editor.begin()){
                cursor--;
                cursor = editor.erase(cursor);
            }
        }
        else if (command == 'P'){
            cin >> word;
            editor.insert(cursor, word);
        }
    }

    for (auto i : editor) cout << i;
}