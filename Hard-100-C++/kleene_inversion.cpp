#include <bits/stdc++.h>
using namespace std;


const int mod = (int)1e+9 + 7;

int solve(vector<int>&a, int n, long long k){
    
    long long res1 = 0;
    vector<long long>original(n, 0);
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            if(a[i] > a[j]){
                res1 += 1;
            }
        }
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(a[i] > a[j]){
                original[i] += 1;
            }
        }
    }
    
    long long final_result = ((k%mod)*(res1%mod))%mod;;
    for(int i = 0; i < n; i++){
        long long mul;
        if(k&1){
            mul = (long long)(k%mod)*(((k-1)/2)%mod);
        }else{
            mul = (long long)((k/2)%mod)*((k-1)%mod);
        }
        final_result += ((mul%mod)*original[i]%mod)%mod;
        //final_result %= mod;
    }
    
    
    return final_result%mod;
    
    
}





int main(){
    
    int n, k;
    cin >> n >> k;
    vector<int>a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    cout << solve(a, n, (long long)k) << endl;
    
    
    
}
