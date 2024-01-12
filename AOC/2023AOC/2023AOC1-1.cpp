#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    string s;
    ll curval;
    ll total = 0;
    do{
        cin>>s;
        curval = 0;
        for(int i=0;i<s.length();i++){
            if(s[i]>='0' && s[i]<='9'){
                curval = s[i]-'0';
                break;
            }
        }
        for(int i=s.length()-1;i>=0;i--){
            if(s[i]>='0' && s[i]<='9'){
                curval = curval*10 + (s[i]-'0');
                break;
            }
        }
        cout<<curval<<endl;
        total += curval;
    }while(s!="end");
    cout<<total<<endl;

    return 0;
}