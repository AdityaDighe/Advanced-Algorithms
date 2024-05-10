#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main()
{
    vector<int> s;
   
    int arr[]={8,6,7,5,2,6,7,1,2,3,2,2,2,2,2,2,2,2,2,2};
    int cost=0;
    int maxlen=1;
    int bank=0;
    int c=3;
   
    s.push_back(arr[0]);
    cost=1;
    bank=bank+c-cost;
    cout<<"Table size: "<<maxlen<<"     Actual Cost: "<<cost<<"     Bank: "<<bank<<endl;
   
    for(int i=1;i<20;i++)
    {
        if(maxlen>s.size())
        {
            cost=1;
            bank=bank+c-cost;
            s.push_back(arr[i]);
        }
        else
        {
            maxlen=maxlen*2;
            cost=s.size()+1;
            bank=bank+c-cost;
            s.push_back(arr[i]);
        }
       
        cout<<"Table size: "<<maxlen<<"     Actual Cost: "<<cost<<"     Bank: "<<bank<<endl;
    }

    return 0;
}
