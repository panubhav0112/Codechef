#include "bits/stdc++.h"
using namespace std;

#define F first
#define S second
#define int long long
#define all(x) (x).begin(), (x).end()

const int M = 1e9 + 7;

string solve() {
    int n,google_mins,end_time;
    cin>>n>>google_mins>>end_time;
    vector<pair<int,int>> v;
    for(int i=0;i<n;i++){
        pair<int,int> p;
        cin>>p.F>>p.S;
        v.push_back(p);
    }
    sort(all(v));
    int a=0;
    for(auto e:v){
        if(a<e.F)
            google_mins= google_mins - (e.F - a);
        a = max(a,e.S);
    }
    google_mins = google_mins - (end_time-a);
    return google_mins>0?"NO":"YES";
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
