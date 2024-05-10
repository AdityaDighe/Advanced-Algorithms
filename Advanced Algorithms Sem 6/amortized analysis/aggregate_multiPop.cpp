#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

void print(vector<int> s)
{
    for (int i = 0; i < s.size(); i++)
    {
        cout << s[i] << " ";
    }
    cout<<endl;
}

int main()
{
    vector<int> s;
   
    int arr[]={8,6,7,5,2,6,7,1};
    int total=0;
   
    for(int i=0;i<8;i++)
    {
        if(arr[i]<=s.size())
        {
            for(int j=0;j<arr[i];j++)
            {
                s.pop_back();
            }
            s.push_back(arr[i]);
           
            print(s);
            cout<<"Cost = "<<arr[i]+1<<endl;
            total=total+arr[i]+1;
        }
        else
        {
            s.push_back(arr[i]);
            print(s);
            cout<<"Cost = 1"<<endl;
            total=total+1;
        }
    }
   
    float a_cost=float(total)/8;
   
    cout<<"Total cost = "<<total<<endl;
    cout<<"Ammortized cost = "<<a_cost;

    return 0;
}
