#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    string a,b;
    string c;
    ll cycle=1;
    ll x=1;
    ll res=0;
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
            if(cycle==20 || cycle==60 || cycle==100 || cycle==140 || cycle==180 || cycle==220){
                res += cycle*x;
            }
        }
        if(b!="" && b[0]=='-'){
            x-=stoi(b.substr(1));
        }else if(b!=""){
            x+=stoi(b);
        }
        cycle++;
        if(cycle==20 || cycle==60 || cycle==100 || cycle==140 || cycle==180 || cycle==220){
            res += cycle*x;
        }
        cout<<res<<endl;
    }

}