#include <bits/stdc++.h>
using namespace std;
using ll = long long;



void movetail(pair<ll,ll>& h, pair<ll,ll>& t){
    if((abs(t.first-h.first)>1) && (abs(t.second-h.second)>1)){
        if(t.first<h.first) t.first++;
        else t.first--;
        if(t.second<h.second) t.second++;
        else t.second--;
    }else if((abs(t.first-h.first)>1) && (abs(t.second-h.second)==1)){
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

int main()
{
    vector<vector<ll>> m(1000,vector<ll>(1000,0));
    vector<pair<ll,ll>> tail(12,make_pair(500,500));
    pair<ll,ll> h = make_pair(500,500);
    m[500][500] = 1;
    char a;
    ll b;
    while(true){
        cin>>a>>b;
        // for(int i=480;i<520;i++){
        //     for(int j=480;j<520;j++){
        //         cout<<m[i][j];
        //     }
        //     cout<<endl;
        // }
        if(a=='E') break;
        for(ll i=0;i<b;i++){
            // for(int x=0;x<12;x++){
            //     cout<<tail[x].first<<' '<<tail[x].second<<endl;
            // }
            cout<<endl;
            if(a=='U'){
                h.first--;
                movetail(h,tail[1]);
                for(int j=1;j<10;j++){
                    movetail(tail[j],tail[j+1]);
                }
            }
            if(a=='D'){
                h.first++;
                movetail(h,tail[1]);
                for(int j=1;j<10;j++){
                    movetail(tail[j],tail[j+1]);
                }
            }
            if(a=='L'){
                h.second--;
                movetail(h,tail[1]);
                for(int j=1;j<10;j++){
                    movetail(tail[j],tail[j+1]);
                }
            }
            if(a=='R'){
                h.second++;
                movetail(h,tail[1]);
                for(int j=1;j<10;j++){
                    movetail(tail[j],tail[j+1]);
                }
            }
            m[tail[9].first][tail[9].second] = 1;
        }
    }
    ll count=0;
    for(int i=0;i<1000;i++){
        for(int j=0;j<1000;j++){
            if(m[i][j]==1) count++;
        }
    }
    for(int i=0;i<12;i++){
        cout<<tail[i].first<<' '<<tail[i].second<<endl;
    }
    cout<<count;
}