#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin>>t;
  while(t--){
    int n,temp;
    cin>>n;
    long s=0;
    for(int i=0;i<n;i++){
      cin>>temp;
      s+=temp;
    }
    if(s<0) cout<<"NO";
    else cout<<"YES";
    cout<<endl;
  }
}
