#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main()
{
    string s;
    string s1;
    string s2;
    ll score = 0;
    do{
        cin>>s;
        s1 = s.substr(0,s.length()/2);
        s2 = s.substr(s.length()/2);
        cout<<s1<<endl;
        cout<<s2<<endl;
        for(ll i=0; i<s2.length();i++){
            if(s1.find(s2[i])!=string::npos){
                cout<<s2[i]<<endl;
                if(s2[i]<='Z'){
                    score += s2[i] - 'A' + 27;
                }
                else{
                    score += s2[i] - 'a' + 1;
                }
                break;
            }
        }
        cout<<score<<endl;
    }while(true);
}