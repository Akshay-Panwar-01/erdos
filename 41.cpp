#include <bits/stdc++.h>
using namespace std;

long long int count(long long int x){
    int res=0;
    while (x>0){
        if (x%10==1) res++;
        x/=10;
    }
    return res ;
}

int main() {
    long long int a=123456789;
    long long int ans = 0;

    for (long long int i = a; i <= 10 * a; ++i) {
        ans+=count(i);
        if (i%a==0){
            cout<<i<<endl;
        }
    }
    cout <<"answer is :"<< ans << endl;

    return 0;
}

//answer is 1298765422
// fastest possible way is to use c++ in this way , almost 2 minutes 40 seconds of time 
