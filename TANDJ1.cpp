#include "bits/stdc++.h"
using namespace std;

#define F first
#define S second
#define int long long
#define all(x) (x).begin(), (x).end()

const int M = 1e9 + 7;

string solve() {
    int a,b,c,d,e;
    cin>>a>>b>>c>>d>>e;
    int x = abs(c-a)+abs(d-b);
    x = e-x;
    if(x<0 || x&1) return "NO";
    return "YES";
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    cin >> tc;
    while (tc--)
        cout<<solve()<<endl;
}
