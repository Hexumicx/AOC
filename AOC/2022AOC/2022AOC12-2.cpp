#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main()
{
    vector<vector<char>> m(42, vector<char>(160, 'z'));
    tuple<int, int, int> end;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> starts;
    for (int i = 0; i < 41; i++)
    {
        for (int j = 0; j < 159; j++)
        {
            cin >> m[i][j];
            if (m[i][j] == 'E')
                end = make_tuple(99, i, j);
            if (m[i][j] == 'S' || m[i][j] == 'a')
            {
                starts.push(make_tuple(0, i, j));
                m[i][j] = 'a';
            }
        }
    }
    int mn = 1e9;
    while (!starts.empty())
    {
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> q;
        vector<vector<int>> visited(42, vector<int>(160, 0));
        q.push(starts.top()); starts.pop();
        tuple<int, int, int> cur;
        while (!q.empty())
        {
            cur = q.top();
            q.pop();
            if (get<1>(cur) == get<1>(end) && get<2>(cur) == get<2>(end))
            {
                mn = min(mn,get<0>(cur));
                break;
            }
            if (visited[get<1>(cur)][get<2>(cur)] == 1)
                continue;
            cout << get<1>(cur) << get<2>(cur) << endl;
            visited[get<1>(cur)][get<2>(cur)] = 1;
            if (get<1>(cur) != 0 && visited[get<1>(cur) - 1][get<2>(cur)] == 0 && m[get<1>(cur) - 1][get<2>(cur)] <= (m[get<1>(cur)][get<2>(cur)] + 1))
            {
                q.push(make_tuple(get<0>(cur) + 1, get<1>(cur) - 1, get<2>(cur)));
            }
            if (get<1>(cur) != 159 && visited[get<1>(cur) + 1][get<2>(cur)] == 0 && m[get<1>(cur) + 1][get<2>(cur)] <= (m[get<1>(cur)][get<2>(cur)] + 1))
            {
                q.push(make_tuple(get<0>(cur) + 1, get<1>(cur) + 1, get<2>(cur)));
            }
            if (get<2>(cur) != 0 && visited[get<1>(cur)][get<2>(cur) - 1] == 0 && (m[get<1>(cur)][get<2>(cur) - 1] <= (m[get<1>(cur)][get<2>(cur)] + 1)))
            {
                q.push(make_tuple(get<0>(cur) + 1, get<1>(cur), get<2>(cur) - 1));
            }
            if (get<2>(cur) != 159 && visited[get<1>(cur)][get<2>(cur) + 1] == 0 && (m[get<1>(cur)][get<2>(cur) + 1] <= (m[get<1>(cur)][get<2>(cur)] + 1)))
            {
                q.push(make_tuple(get<0>(cur) + 1, get<1>(cur), get<2>(cur) + 1));
            }
        }
    }
    cout<<mn<<endl;
}