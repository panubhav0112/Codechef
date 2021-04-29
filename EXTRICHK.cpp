#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define ll long long
#define M 1e9 + 7
#define round(x, y) fixed << setprecision(y) << x

int solve(){
    int a,b,c;
    cin>>a>>b>>c;
    if(a>=(b+c) || b>=(a+c) || c>=(a+b)) return -1;
    if(a==b && a==c) return 1;
    if(a==b || b==c || a==c) return 2;
    return 3;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<< solve();

}
