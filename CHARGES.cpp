#include "bits/stdc++.h"
using namespace std;

#define F first
#define S second
#define int long long
#define all(x) (x).begin(), (x).end()

const int M = 1e9 + 7;

void solve() {
    int n,k;
    cin>>n>>k;
    string s;
    cin>>s;
    vector<char> v(s.begin(),s.end());
    int charge = 0;
    for(int i=1;i<n;i++){
        if(v[i]==v[i-1])
            charge+=2;
        else charge++;
    }
    // cout<<charge<<"\n";
    for(int i=0;i<k;i++){
        int x;
        cin>>x;
        x--;
        v[x]^=1;
        if(x>0){
            if(v[x]==v[x-1]) charge++;
            else charge--;
        }
        if(x<(n-1)){
            if(v[x]==v[x+1]) charge++;
            else charge--;
        }
        cout<<charge<<endl;
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int tc = 1;
    cin >> tc;
    while (tc--)
        solve();
}
