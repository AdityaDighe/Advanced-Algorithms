#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main()
{
    vector<int> s;
    vector<int> p;
   
    int arr[]={8,6,7,5,2,6,7,1,2,3,2,2,2,2,2,2,2,2,2,2};
    int cost=0;
    int maxlen=1;
    int c=0;
    int potential=0;
   
    p.push_back(0);
    s.push_back(arr[0]);
    cost=1;
    potential=2*s.size()-maxlen;
    p.push_back(potential);
    c=cost+(p[1]-p[0]);
    cout<<"Table size: "<<maxlen<<"     Actual Cost: "<<cost<<"     Assumed Cost: "<<c<<"     Potential Diff: "<<potential<<endl;
   
    for(int i=1;i<20;i++)
    {
        if(maxlen>s.size())
        {
            s.push_back(arr[i]);
            cost=1;
            potential=2*s.size()-maxlen;
            p.push_back(potential);
            c=cost+(p[i+1]-p[i]);
        }
        else
        {
           
            cost=s.size()+1;
            s.push_back(arr[i]);
            maxlen=maxlen*2;
            potential=2*s.size()-maxlen;
            p.push_back(potential);
            c=cost+(p[i+1]-p[i]);
        }
       
        cout<<"Table size: "<<maxlen<<"     Actual Cost: "<<cost<<"     Assumed Cost: "<<c<<"     Potential Diff: "<<potential<<endl;
    }

    return 0;
}