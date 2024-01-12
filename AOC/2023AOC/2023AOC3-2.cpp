#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    vector<vector<char>> m(300, vector<char>(150, '.'));
    for(int i=0; i<140;i++){
        string s;
        cin>>s;
        for(int j=0; j<s.size(); j++){
            m[i][j] = s[j];
        }
    }
    ll curval = 0;
    ll total = 0;
    pair<int,int> gear;
    vector<vector<vector<ll>>> mm(140,vector<vector<ll>>(140,vector<ll>()));
    bool t = false;
    for(int i=0;i<m.size();i++){
        for(int j=0;j<m[i].size();j++){
            if(m[i][j] >= '0' && m[i][j]<='9'){
                curval *= 10;
                curval += m[i][j] - '0';
                if(i!=0 && j!=0 && (m[i-1][j-1]<'0' || m[i-1][j-1]>'9') && m[i-1][j-1] == '*'){
                    t = true;
                    gear = {i-1,j-1};
                }
                if(i!=0 && (m[i-1][j]<'0' || m[i-1][j]>'9') && m[i-1][j] == '*'){
                    t = true;
                    gear = {i-1,j};
                }
                if(i!=0 && j!=140 && (m[i-1][j+1]<'0' || m[i-1][j+1]>'9') && m[i-1][j+1] == '*'){
                    t = true;
                    gear = {i-1,j+1};
                }
                if(j!=0 && (m[i][j-1]<'0' || m[i][j-1]>'9') && m[i][j-1] == '*'){
                    t = true;
                    gear = {i,j-1};
                }
                if(j!=140 && (m[i][j+1]<'0' || m[i][j+1]>'9') && m[i][j+1] == '*'){
                    t = true;
                    gear = {i,j+1};
                }
                if(i!=140 && j!=0 && (m[i+1][j-1]<'0' || m[i+1][j-1]>'9') && m[i+1][j-1] == '*'){
                    t = true;
                    gear = {i+1,j-1};
                }
                if(i!=140 && (m[i+1][j]<'0' || m[i+1][j]>'9') && m[i+1][j] == '*'){
                    t = true;
                    gear = {i+1,j};
                }
                if(i!=140 && j!=140 && (m[i+1][j+1]<'0' || m[i+1][j+1]>'9') && m[i+1][j+1] == '*'){
                    t = true;
                    gear = {i+1,j+1};
                }
            }
            else{
                if(t){
                    mm[gear.first][gear.second].push_back(curval);
                    t = false;
                }
                curval = 0;
            }
        }
    }
    for(int i=0;i<mm.size();i++){
        for(int j=0;j<mm[i].size();j++){
            if(mm[i][j].size() == 2){
                total += mm[i][j][0]*mm[i][j][1];
            }
        }
    }
    cout<<"words"<<endl;
    cout<<total<<endl;
    return 0;
}