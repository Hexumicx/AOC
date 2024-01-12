#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    string c;
    ll count = 0;
    ll mx = 0;
    ll t1 = 0;
    ll t2 = 0;
    ll t3 = 0;
    do{
        getline(cin,c);
        if(c==""){
            if(count>t3){
                t1 = t2;
                t2 = t3;
                t3 = count; 
            }else if(count>t2){
                t1 = t2;
                t2 = count;
            }else if(count>t1){
                t1 = count;
            }
            count = 0;
        }else{
            count += stoi(c);
        }
        cout<<"mx:"<<t1+t2+t3<<endl;
    }while(true);

}