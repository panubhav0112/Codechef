#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define int long long
#define FASTIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

const int M = 1e9+7;

int solve(){
    int n,m;
    cin>>n>>m;
    int ans=0;
    vector<int> rem(n,1);
    for(int i=2;i<=n;i++){
        int r = m%i;
        ans+= rem[r];
        for(int j=r;j<n;j+=i)
            rem[j]++;
    }
    return ans;
}

int32_t main()
{
    FASTIO
    int tc = 1;
    cin>>tc;
    while (tc--)
    {
        cout << solve()<<endl;
    }
}