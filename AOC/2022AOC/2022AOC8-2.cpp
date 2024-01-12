#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    vector<vector<ll>> m(99,vector<ll>(99));
    string a;
    for(int i=0;i<99;i++){
        cin>>a;
        for(int j=0;j<99;j++){
            m[i][j] = a[j]-'0';
        }
    }

    bool up=true;
    bool down=true;
    bool left=true;
    bool right=true;
    ll count = 1;
    ll mx = 0;
    ll x,y;
    for(int i=1;i<98;i++){
        for(int j=1;j<98;j++){
            count = 1;
            up=true;
            down=true;
            left=true;
            right=true;
            x=i;y=j;
            while(true){
                if(x<1){
                    up = false;
                    break;
                }
                if(m[i][j]>m[x-1][y]) x--;
                else break;
            }
            if(!up){
                count *= (i-x);
            }else{
                count *= (i-x+1);
            }
            x=i;y=j;
            while(true){
                if(x>97){
                    down = false;
                    break;
                }
                if(m[i][j]>m[x+1][y]) x++;
                else break;
            }
            if(!down){
                count *= (x-i);
            }else{
                count *= (x-i+1);
            }
            x=i;y=j;
            while(true){
                if(y<1){
                    left = false;
                    break;
                }
                if(m[i][j]>m[x][y-1]) y--;
                else break;
            }
            if(!left){
                count *= (j-y);
            }else{
                count *= (j-y+1);
            }
            x=i;y=j;
            while(true){
                if(y>97){
                    right = false;
                    break;
                }
                if(m[i][j]>m[x][y+1]) y++;
                else break;
            }
            if(!right){
                count *= (y-j);
            }else{
                count *= (y-j+1);
            }
            mx = max(mx,count);
            
        }
    }
    cout<<mx<<endl;

}