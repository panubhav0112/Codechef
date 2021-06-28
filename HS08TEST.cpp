#include <bits/stdc++.h>
using namespace std;

int main() {
  int a;
  double b;
  cin>>a>>b;
  if((a+0.5 > b) || (a%5)!=0)
    cout<<fixed<<setprecision(2)<<b;
  else cout<<fixed<<setprecision(2)<<(b-a-0.5);  
}
