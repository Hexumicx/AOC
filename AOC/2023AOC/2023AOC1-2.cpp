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
            if(s[i]=='o' && s[i+1]=='n' && s[i+2]=='e'){
                curval = 1;
                break;
            }
            if(s[i]=='t' && s[i+1]=='w' && s[i+2]=='o'){
                curval = 2;
                break;
            }
            if(s[i]=='t' && s[i+1]=='h' && s[i+2]=='r' && s[i+3]=='e' && s[i+4]=='e'){
                curval = 3;
                break;
            }
            if(s[i]=='f' && s[i+1]=='o' && s[i+2]=='u' && s[i+3]=='r'){
                curval = 4;
                break;
            }
            if(s[i]=='f' && s[i+1]=='i' && s[i+2]=='v' && s[i+3]=='e'){
                curval = 5;
                break;
            }
            if(s[i]=='s' && s[i+1]=='i' && s[i+2]=='x'){
                curval = 6;
                break;
            }
            if(s[i]=='s' && s[i+1]=='e' && s[i+2]=='v' && s[i+3]=='e' && s[i+4]=='n'){
                curval = 7;
                break;
            }
            if(s[i]=='e' && s[i+1]=='i' && s[i+2]=='g' && s[i+3]=='h' && s[i+4]=='t'){
                curval = 8;
                break;
            }
            if(s[i]=='n' && s[i+1]=='i' && s[i+2]=='n' && s[i+3]=='e'){
                curval = 9;
                break;
            }
        }
        for(int i=s.length()-1;i>=0;i--){
            if(s[i]>='0' && s[i]<='9'){
                curval = curval*10 + (s[i]-'0');
                break;
            }
            if(s[i]=='e' && s[i-1]=='n' && s[i-2]=='o'){
                curval = curval*10 + 1;
                break;
            }
            if(s[i]=='o' && s[i-1]=='w' && s[i-2]=='t'){
                curval = curval*10 + 2;
                break;
            }  
            if(s[i]=='e' && s[i-1]=='r' && s[i-2]=='h' && s[i-3]=='t'){
                curval = curval*10 + 3;
                break;
            }
            if(s[i]=='r' && s[i-1]=='u' && s[i-2]=='o' && s[i-3]=='f'){
                curval = curval*10 + 4;
                break;
            }
            if(s[i]=='e' && s[i-1]=='v' && s[i-2]=='i' && s[i-3]=='f'){
                curval = curval*10 + 5;
                break;
            }
            if(s[i]=='x' && s[i-1]=='i' && s[i-2]=='s'){
                curval = curval*10 + 6;
                break;
            }
            if(s[i]=='n' && s[i-1]=='e' && s[i-2]=='v' && s[i-3]=='e' && s[i-4]=='s'){
                curval = curval*10 + 7;
                break;
            }
            if(s[i]=='t' && s[i-1]=='h' && s[i-2]=='g' && s[i-3]=='i' && s[i-4]=='e'){
                curval = curval*10 + 8;
                break;
            }
            if(s[i]=='e' && s[i-1]=='n' && s[i-2]=='i' && s[i-3]=='n'){
                curval = curval*10 + 9;
                break;
            }
        }
        cout<<curval<<endl;
        total += curval;
    }while(s!="end");
    cout<<total<<endl;

    return 0;
}