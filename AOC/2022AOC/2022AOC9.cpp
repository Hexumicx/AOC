#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    vector<vector<ll>> m(1000,vector<ll>(1000,0));
    pair<ll,ll> h = make_pair(500,500);
    pair<ll,ll> t = make_pair(500,500);
    m[500][500] = 1;
    char a;
    ll b;
    while(true){
        cin>>a>>b;
        if(a=='E') break;
        for(ll i=0;i<b;i++){
            if(a=='U'){
                h.first--;
                if((abs(t.first-h.first)>1) && (abs(t.second-h.second)==1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if((abs(t.first-h.first)==1) && (abs(t.second-h.second)>1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if(abs(t.first-h.first)>1){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                }else if(abs(t.second-h.second)>1){
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }
            }
            if(a=='D'){
                h.first++;
                if((abs(t.first-h.first)>1) && (abs(t.second-h.second)==1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if((abs(t.first-h.first)==1) && (abs(t.second-h.second)>1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if(abs(t.first-h.first)>1){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                }else if(abs(t.second-h.second)>1){
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }
            }
            if(a=='L'){
                h.second--;
                if((abs(t.first-h.first)>1) && (abs(t.second-h.second)==1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if((abs(t.first-h.first)==1) && (abs(t.second-h.second)>1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if(abs(t.first-h.first)>1){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                }else if(abs(t.second-h.second)>1){
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }
            }
            if(a=='R'){
                h.second++;
                if((abs(t.first-h.first)>1) && (abs(t.second-h.second)==1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if((abs(t.first-h.first)==1) && (abs(t.second-h.second)>1)){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }else if(abs(t.first-h.first)>1){
                    if(t.first<h.first) t.first++;
                    else t.first--;
                }else if(abs(t.second-h.second)>1){
                    if(t.second<h.second) t.second++;
                    else t.second--;
                }
            }
            m[t.first][t.second] = 1;
        }
    }
    ll count=0;
    for(int i=0;i<1000;i++){
        for(int j=0;j<1000;j++){
            if(m[i][j]==1) count++;
        }
    }
    cout<<count;
}