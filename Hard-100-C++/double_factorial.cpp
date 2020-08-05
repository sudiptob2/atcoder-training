#include <bits/stdc++.h>
using namespace std;

int main(){
    
    long long n;
    cin >> n;
    
    if(n&1){
        cout << 0 << endl;
        return 0;
    }
    
    long long res = 0;
    long long deno = 10;
    while(deno <= n){
        res += n/(deno);
        deno *= 5;
        //idx += 1;
    }
    
    cout << res << endl;
    
    
    return 0;
    
}
