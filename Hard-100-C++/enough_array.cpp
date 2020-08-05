#include <bits/stdc++.h>
using namespace std;


int binary_search(int start, int end, long long value, vector<long long>&pref){
    
    while(start < end){
        int mid = (start) + (end - start)/2;
        if(value <= pref[mid]){
            end = mid;
        }else{
            start = mid + 1;
        }
    }
    
    return start;
}




int main(){
    
    int n; long long k;
    cin >> n >> k;
    vector<int>a(n);
    
    vector<long long>p(n+1, 0);
    
    for(int i = 0; i < n; i++){
        cin >> a[i];
        p[i+1] = p[i] + a[i]; 
        //cout << p[i+1] << " ";  
    }
    
    long long res = 0;
    for(int i = 1; i <= n; i++){
        
        long long value_to_find = k + p[i-1];
        int idx = binary_search(0, n, value_to_find, p);
        //int idx = lower_bound(p.begin(), p.end(), value_to_find) - p.begin();
        
        if(idx == n){
            if(value_to_find <= p[n]){
                res += 1;
            }

        }else{
            res += (n - idx + 1);
        }
        //cout << i << " " << " " << value_to_find << " " <<  res << " " << idx << endl; 
        // binary search the first idx that is >= value_to_find 
    }
    
    cout << res << endl;
    
}
