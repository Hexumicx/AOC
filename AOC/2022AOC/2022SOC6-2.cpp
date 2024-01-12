#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    ll count = 14;
    vector<char> c(15);
    ll mx = 13*7;
    ll m = 0;
    for(int i=1;i<15;i++){
        cin>>c[i];
    }
    while(true){
        m = 0;
        for(int i=1;i<15;i++){
            for(int j=i+1;j<15;j++){
                if(c[i]!=c[j]){
                    m+=1;
                }
            }
        }
        if(m == mx){
            cout<<count<<endl;
            return 0;
        }
        for(int i=1;i<14;i++){
            c[i] = c[i+1];
        }
        
        cin>>c[14];
        count++;
    }
}