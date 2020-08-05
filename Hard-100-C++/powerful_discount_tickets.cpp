#include <bits/stdc++.h>
using namespace std;


long long solve(vector<int>&a, int n, int m){

    priority_queue<int>Q;
    for(int i = 0; i < n; i++){
        Q.push(a[i]);
    }
    
    while(m > 0){
        int top_element = Q.top();
        Q.pop();
        top_element = top_element/2;
        Q.push(top_element);
        
        m -= 1;
    }
    long long solution = 0;
    while(!Q.empty()){
        
        solution += Q.top();
        Q.pop();
    }
    
    
    return solution;
    
    
}





int main(){
    
    int n, m;
    cin >> n >> m;
    vector<int>a(n);
    
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    cout << solve(a, n, m) << endl;
    
    
    return 0;
    
}
