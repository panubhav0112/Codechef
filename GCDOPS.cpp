#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin>>t;
  while(t--){
    int n,temp;
    cin>>n;
    bool valid=true;
    for(int i=1;i<=n;i++){
      cin>>temp;
      if(i%temp!=0) valid=false;
    }
    if(valid) cout<<"YES";
    else cout<<"NO";
    cout<<endl;
  }
}
