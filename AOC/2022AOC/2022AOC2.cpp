#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main()
{
    char o; char p;
    ll score = 0;
    do{
        cin>>o>>p;
        if(p=='Y' && o=='A'){
            score+=6;
        }
        if(p=='Z' && o=='B'){
            score+=6;
        }
        if(p=='X' && o=='C'){
            score+=6;
        }
        if((p-'X')==(o-'A')){
            score+=3;
        }
        if(p=='X'){
            score+=1;
        }
        if(p=='Y'){
            score+=2;
        }
        if(p=='Z'){
            score+=3;
        }
        cout<<score<<endl;
    }while(true);
}