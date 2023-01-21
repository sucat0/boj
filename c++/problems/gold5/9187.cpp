#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    while (true) {
        // Keyword input
        string keyword;
        getline(cin, keyword);
        if (keyword == "999") break;

        // Make chiper table
        pair<int, int> locations[91];
        char square_table[5][5];

        int count = 0;
        for (int i = 0; i < keyword.length(); i++) {
            int alpha_num = keyword[i] == 'J' ? 'I' : keyword[i];  // make I, J same
            if (locations[alpha_num].first == 0) {
                locations[alpha_num].first = count/5 + 1;  // row (start with 1)
                locations[alpha_num].second = count%5 + 1;  // column (start with 1)

                square_table[count/5][count%5] = alpha_num;
                count++;
            }
        }

        for (int i = 65; i <= 73; i++) {
            if (locations[i].first == 0) {
                locations[i].first = count/5 + 1;
                locations[i].second = count%5 + 1;

                square_table[count/5][count%5] = i;
                count++;
            }
        }

        for (int i = 75; i <= 90; i++) {
            if (locations[i].first == 0) {
                locations[i].first = count/5 + 1;
                locations[i].second = count%5 + 1;

                square_table[count/5][count%5] = i;
                count++;
            }
        }

        // Message input
        string message;
        getline(cin, message);

        // Add Q, Z to message
        char tmp = message[0] == 'J' ? 'I' : message[0];
        string added_message;
        added_message.push_back(tmp);

        for (int i = 1; i < message.length(); i++) {
            char cur = message[i] == 'J' ? 'I' : message[i];
            if (cur == ' ') continue;

            if (cur == tmp) {
                if (cur == 'Q') added_message.push_back('Z');
                else added_message.push_back('Q');
            }

            added_message.push_back(cur);
            tmp = cur;
        }

        if (added_message.length()%2 == 1) {
            if (added_message.back() == 'Q') added_message.push_back('Z');
            else added_message.push_back('Q');
        }

        // Encrypt
        for (int i = 0; i < added_message.length(); i+=2) {
            int x_one = locations[added_message[i]].first-1;
            int y_one = locations[added_message[i]].second-1;
            int x_two = locations[added_message[i+1]].first-1;
            int y_two = locations[added_message[i+1]].second-1;
            
            char enc_one, enc_two;
            if (x_one == x_two) {
                enc_one = square_table[x_one][(y_one+1)%5];
                enc_two = square_table[x_two][(y_two+1)%5];
            } else if (y_one == y_two) {
                enc_one = square_table[(x_one+1)%5][y_one];
                enc_two = square_table[(x_two+1)%5][y_two];
            } else {
                enc_one = square_table[x_one][y_two];
                enc_two = square_table[x_two][y_one];
            }

            cout << enc_one << enc_two << " ";
        }

        cout << "\n";
    }
}