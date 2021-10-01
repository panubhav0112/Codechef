#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int u=0;u<t;u++)
    {
        int n;
        cin>>n;
        long long int k;
        cin>>k;
        int check=0;
        int l=0;
        int K=0;
        long long int p[n];
        for(int i=0;i<n;i++)
            cin>>p[i];
        long long int ans[n];
        long long int res[n];
        for(int i=0;i<n;i++)
        {
            if(p[i]==k)
            {
                ans[K++]=1;
                res[l++]=p[i];
                check++;
                break;
            }
            else if(p[i]>k)
            {
                continue;
            }
            else
            {
                if(k%p[i]==0)
                {
                    check++;
                    ans[K++]=k/p[i];
                    res[l++]=p[i];
                }    
            }
        }
        if(check==0)
        {
            cout<<-1<<"\n";
        }
        else
        {
            int min=INT_MAX;
            int pos=0;
            for(int i=0;i<K;i++)
            {
                if(ans[i]<min)
                {
                    min=ans[i];
                    pos=i;
                }
            }
            cout<<res[pos]<<"\n";
        }
    }
    return 0;
}