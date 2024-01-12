#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main()
{
    string s3;
    string s1;
    string s2;
    ll score = 0;
    do{
        cin>>s1>>s2>>s3;
        for(ll i=0; i<s3.length();i++){
            if(s1.find(s3[i])!=string::npos && s2.find(s3[i])!=string::npos){
                cout<<s3[i]<<endl;
                if(s3[i]<='Z'){
                    score += s3[i] - 'A' + 27;
                }
                else{
                    score += s3[i] - 'a' + 1;
                }
                break;
            }
        }
        cout<<score<<endl;
    }while(true);
}