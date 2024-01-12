#include <bits/stdc++.h>
using namespace std;
using ll = long long;


int main()
{
    char o; char p;
    ll score = 0;
    do{
        cin>>o>>p;
        if(p=='Z'&& o=='A'){
            score+=2;
        }
        if(p=='Z'&& o=='B'){
            score+=3;
        }
        if(p=='Z'&& o=='C'){
            score+=1;
        }
        if(p=='Z'){
            score+=6;
        }
        if(p=='Y'){
            score+=3;
            score+=(o-'A'+1);
        }
        if(p=='X'){
            if(o=='A'){
                score+=3;
            }
            if(o=='B'){
                score+=1;
            }
            if(o=='C'){
                score+=2;
            }
        }
        cout<<score<<endl;
    }while(true);
}