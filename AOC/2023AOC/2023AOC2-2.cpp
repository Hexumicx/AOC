#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    string s;
    ll curval = 0;
    ll count = 0;
    ll red = 0;
    ll blue = 0;
    ll green = 0; 
    ll game = 1;
    getline(cin, s);
    while(s != "end"){
        red = 0;
        blue = 0;
        green = 0;
        int start = s.find(":");
        for(int i=start+1; i<s.size(); i++){
            
            if(s[i] >= '0' && s[i] <= '9'){
                curval = s[i] - '0';
                if(s[i+1] >= '0' && s[i+1] <= '9'){
                    curval = curval*10 + (s[i+1] - '0');
                    i++;
                }
            }
            if(s[i] == 'r'){
                red = max(red,curval);
                curval = 0;
            }
            else if(s[i] == 'b'){
                blue = max(blue,curval);
                curval = 0;
            }
            else if(s[i] == 'g'){
                green = max(green,curval);
                curval = 0;
            }
        }
        count += red*blue*green;
        getline(cin, s);
    }
    cout<<count<<endl;
    return 0;
}