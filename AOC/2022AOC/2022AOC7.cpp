#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll space = 0;
int i = 0;

int file(){
    i++;
    cout<<i<<endl;
    char c;
    string s;
    cin>>c>>s;
    getline(cin,s);
    string f,n;
    ll size = 0;
    while(cin.peek()!='$'){
        cout<<"while";
        cin>>f>>n;
        getline(cin,s);
        if(f!="dir"){
            size+=stoi(f);
        }
    }
    cin>>c>>s>>s;
    while(s!=".."){
        size += file();
        cin>>c>>s;
        if(s=="cd") cin>>s;
    }
    cout<<"back";
    if(size<100000){
        space+=size;
    }
    i--;
    cout<<i<<endl;
    return size;
}


int main()
{
    char c;
    string s;
    cin>>c>>s;
    ll size = 0;
    size += file();
    if(size<100000){
        space+=size;
    }
    cout<<space;
}