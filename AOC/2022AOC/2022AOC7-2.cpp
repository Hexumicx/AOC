#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll space = 70000000;
ll req = 30000000;
ll diff = 1e9;
vector<ll> arr(10000);
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
    arr.push_back(size);
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
    ll unused = space - size;
    sort(arr.begin(),arr.end());
    for(auto k:arr){
        if(k>(req-unused)){
            cout<<k<<endl;
            return 0;
        }
    }
}