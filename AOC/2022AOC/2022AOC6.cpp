#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    char a,b,c,d;
    cin>>a>>b>>c>>d;
    ll count = 4;
    while(a==b || a==c || a==d || b==c || b==d || c==d){
        a=b;b=c;c=d;
        cin>>d;
        count++;
    }
    cout<<count<<endl;
}