#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define ll long long
#define M 1e9 + 7

void solve(){
    int n,q;
    cin>>n>>q;
    vector<int> vi(n+2);
    for(int i=1;i<=n;i++)
        cin>>vi[i];
    vector<int> fd=vi,bd=vi;
    for(int i=1;i<=n;i++)
        fd[i] = __gcd(fd[i],fd[i-1]);
    for(int i=n;i>=0;i--)
        bd[i] = __gcd(bd[i],bd[i+1]);
    while(q--){
        int l,r;
        cin>>l>>r;
        cout<<__gcd(fd[l-1],bd[r+1])<<endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int tc = 1;
    cin >> tc;
    while (tc--)
    {
        solve();
    }
}
