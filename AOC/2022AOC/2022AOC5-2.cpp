#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main()
{
    vector<stack<char>> m(10,stack<char>());
    m[1].push('H'); m[1].push('R'); m[1].push('B'); m[1].push('D'); 
    m[1].push('Z'); m[1].push('F'); m[1].push('L'); m[1].push('S');

    m[2].push('T'); m[2].push('B'); m[2].push('M'); m[2].push('Z'); m[2].push('R');

    m[3].push('Z'); m[3].push('L'); m[3].push('C'); m[3].push('H'); m[3].push('N'); m[3].push('S');

    m[4].push('S'); m[4].push('C'); m[4].push('F'); m[4].push('J');

    m[5].push('P'); m[5].push('G'); m[5].push('H'); m[5].push('W');
    m[5].push('R'); m[5].push('Z'); m[5].push('B');

    m[6].push('V'); m[6].push('J'); m[6].push('Z'); m[6].push('G');
    m[6].push('D'); m[6].push('N'); m[6].push('M'); m[6].push('T');

    m[7].push('G'); m[7].push('L'); m[7].push('N'); m[7].push('W');
    m[7].push('F'); m[7].push('S'); m[7].push('P'); m[7].push('Q');

    m[8].push('M'); m[8].push('Z'); m[8].push('R');

    m[9].push('M'); m[9].push('C'); m[9].push('L'); m[9].push('G');
    m[9].push('V'); m[9].push('R'); m[9].push('T');

    string c;
    ll x,y,z;
    stack<char> s;
    do{
        cin>>c>>x>>c>>y>>c>>z;
        for(ll i=0;i<x;i++){
            s.push(m[y].top());
            m[y].pop();
        }
        while(!s.empty()){
            m[z].push(s.top());
            s.pop();
        }
        for(ll i=1;i<10;i++){
            if(m[i].empty()){
                cout<<' ';
                continue;
            }
            cout<<m[i].top();
        }
        cout<<endl;
    }while(true);

}