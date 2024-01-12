#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    ll f1;
    ll f2;
    ll s1;
    ll s2;
    char c;
    ll count = 0;
    do{
        cin>>f1>>c>>f2>>c>>s1>>c>>s2;
        if(f2>=s1 && f1<=s1){
            count++;
        }
        else if(s2>=f1 && s1<=f1){
            count++;
        }
        cout<<count<<endl;
    }while(true);
}