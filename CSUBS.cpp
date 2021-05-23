#include "bits/stdc++.h"
using namespace std;

#define F first
#define S second
#define int long long
#define all(x) (x).begin(), (x).end()

const int M = 1e9 + 7;

int solve() {
    int n,k;
    cin>>n>>k;
    vector<unordered_map<int,int>> vm(k);
    for(int i=0;i<n;i++){
        int e;
        cin>>e;
        vm[i%k][e]++;
    }
    int ans=0;
    for(auto m:vm){
        int mx=0,sum=0;
        for(auto e:m){
            mx = max(mx,e.S);
            sum+= e.S;
        }
        ans+= sum-mx;
    }
    return ans;
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
