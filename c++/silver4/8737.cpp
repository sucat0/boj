/*
다음 작업으로 카드 덱을 섞습니다.

A - 첫 번째 카드를 더미의 맨 위에서 맨 아래로 놓기
B - 더미의 맨 위에서 두 번째 카드를 맨 아래에 놓습니다.
당신의 임무는 k번의 작업 후에 어떤 카드가 n-조각 덱의 맨 위에 있을 것인지 계산하는 것입니다. 
카드는 1에서 n까지의 숫자로 위에서부터 연속적으로 번호가 매겨집니다.

입력
첫 번째 줄에는 두 개의 정수 n과 k가 있습니다(1 ≤ n, m ≤ 2,000,000). 
두 번째 줄에는 카드 데크에 대한 후속 작업 유형을 나타내는 A 또는 B와 같은 k 문자가 있습니다.

연장
첫 번째이자 유일한 출력 라인에는 스택 맨 위에 있는 카드 번호인 하나의 정수가 포함되어야 합니다.*/


#include <bits/stdc++.h>
using namespace std;


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    list<int> cards;
    list<int>::iterator it;
    int n, k;
    char i;

    cin >> n >> k;

    while (n--) {
        cards.push_front(n+1);
    }

    while (k--) {
        cin >> i;
        
        if (i == 'A'){
            cards.push_back(cards.front());
            cards.pop_front();
        } else {
            it = ++cards.begin();
            cards.push_back(*it);
            cards.erase(it);
        }
    }

    cout << cards.front();
}