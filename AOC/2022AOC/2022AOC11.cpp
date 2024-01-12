#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    vector<queue<ll>> m(8,queue<ll>());
    vector<ll> count(8,0);
    m[0].push(59);m[0].push(65);m[0].push(86);m[0].push(56);m[0].push(74);m[0].push(57);m[0].push(56);
    m[1].push(63);m[1].push(83);m[1].push(50);m[1].push(63);m[1].push(56);
    m[2].push(93);m[2].push(79);m[2].push(74);m[2].push(55);
    m[3].push(86);m[3].push(61);m[3].push(67);m[3].push(88);m[3].push(94);m[3].push(69);m[3].push(56);m[3].push(91);
    m[4].push(76);m[4].push(50);m[4].push(51);
    m[5].push(77);m[5].push(76);
    m[6].push(74);
    m[7].push(86);m[7].push(85);m[7].push(52);m[7].push(86);m[7].push(91);m[7].push(95);

    ll item;
    for(int i=1;i<=10000;i++){
        while(!m[0].empty()){
            item = m[0].front(); m[0].pop();
            count[0]++;
            item *=17;
            item %= 9699690;
            if(item%3==0) m[3].push(item);
            else m[6].push(item);
        }
        while(!m[1].empty()){
            item = m[1].front(); m[1].pop();
            count[1]++;
            item +=2;
            item %= 9699690;
            if(item%13==0) m[3].push(item);
            else m[0].push(item);
        }
        while(!m[2].empty()){
            item = m[2].front(); m[2].pop();
            count[2]++;
            item +=1;
            item %= 9699690;
            if(item%2==0) m[0].push(item);
            else m[1].push(item);
        }
        while(!m[3].empty()){
            item = m[3].front(); m[3].pop();
            count[3]++;
            item +=7;
            item %= 9699690;
            if(item%11==0) m[6].push(item);
            else m[7].push(item);
        }
        while(!m[4].empty()){
            item = m[4].front(); m[4].pop();
            count[4]++;
            item *=item;
            item %= 9699690;
            if(item%19==0) m[2].push(item);
            else m[5].push(item);
        }
        while(!m[5].empty()){
            item = m[5].front(); m[5].pop();
            count[5]++;
            item +=8;
            item %= 9699690;
            if(item%17==0) m[2].push(item);
            else m[1].push(item);
        }
        while(!m[6].empty()){
            item = m[6].front(); m[6].pop();
            count[6]++;
            item *=2;
            item %= 9699690;
            if(item%5==0) m[4].push(item);
            else m[7].push(item);
        }
        while(!m[7].empty()){
            item = m[7].front(); m[7].pop();
            count[7]++;
            item +=6;
            item %= 9699690;
            if(item%7==0) m[4].push(item);
            else m[5].push(item);
        }
    }
    sort(count.begin(), count.end());
    cout<<count[6]*count[7]<<endl;
}