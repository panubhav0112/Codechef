#include "bits/stdc++.h"
using namespace std;

#define F first
#define S second
#define int long long
#define all(x) (x).begin(), (x).end()

const int M = 1e9 + 7;

vector<vector<int>> vv(1001,vector<int>(1001));

int solve() {
    int ans=0;
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    a--;b--;c--;d--;
    for(int i=a;i<=c;i++)
        ans+= vv[i][b];
    for(int i=b+1;i<=d;i++)
        ans+= vv[c][i];
    return ans;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    cin >> tc;
    vv[0][0]=1;
    for(int i=1;i<=1000;i++)
        vv[0][i] = vv[0][i-1]+i;
    for(int i=1;i<=1000;i++){
        vv[i][0] = vv[i-1][0] + i+1;
        for(int j=i;j<i+1000;j++)
            vv[i][j-i+1] = vv[i][j-i]+j+1;
    }

    while (tc--)
        cout<<solve()<<endl;
}
