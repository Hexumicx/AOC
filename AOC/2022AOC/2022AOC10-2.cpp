#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    vector<vector<char>> m(6,vector<char>(50,'.'));
    m[0][0] = '#';
    string a,b;
    string c;
    ll cycle=1;
    ll x=1;
    ll add;
    while(true){
        if(cin.peek()=='a'){
            cin>>a>>b;
        }else{
            cin>>a;
            b = "";
        }
        getline(cin,c);
        if(a[0]=='a'){
            cycle++;
            if(cycle%40 == x || cycle%40 == x+1 || cycle%40 == x+2){
                m[(cycle-1)/40][(cycle-1)%40] = '#';
            }
        }
        if(b!="" && b[0]=='-'){
            x-=stoi(b.substr(1));
        }else if(b!=""){
            x+=stoi(b);
        }
        cycle++;
        if(cycle%40 == x || cycle%40 == x+1 || cycle%40 == x+2){
            m[(cycle-1)/40][(cycle-1)%40] = '#';
        }
        for(int i=0;i<6;i++){
            for(int j=0;j<40;j++){
                cout<<m[i][j];
            }
            cout<<endl;
        }
    }

}