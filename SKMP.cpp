#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int u=0;u<t;u++)
    {
        string s,p,res;
        cin>>s>>p;
        int n=p.length();
        char c1=p[0];
        char ch=c1;
        int H[26]={0};
        for(int i=0;i<s.length();i++)
        {
            H[s[i]-'a']++;
            if(i<n)
            {
                H[p[i]-'a']--;
                if(ch==c1)
                    ch=p[i];
            }
            
        }
        char c2;
        for(int i=0;i<26;i++)
        {
            c2=i+'a';
            if(c1!=c2)
            {
                for(int k=H[i];k>0;k--)
                {
                    res.push_back((char)(i+'a'));
                }
            }
            else
            {
                if(ch<c1)
                {
                    for(int j=0;j<n;j++)
                    {
                        res.push_back(p[j]);
                    }
                    for(int k=H[i];k>0;k--)
                    {
                        res.push_back((char)(i+'a'));
                    }
                    
                }
                else
                {
                    for(int k=H[i];k>0;k--)
                    {
                        res.push_back((char)(i+'a'));
                    }
                    for(int j=0;j<n;j++)
                    {
                        res.push_back(p[j]);
                    }
                }
            }
        }
        cout<<res<<"\n";
    }
}