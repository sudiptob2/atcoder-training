#include <bits/stdc++.h>
using namespace std;


string solve(vector<string>&a, vector<string>&b){
    
    int n = a.size();
    int m = b.size();
    
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            
            // Implement the conv layer here
            int res = 0;
            for(int k = 0; k < m; k++){
                for(int l = 0; l < m; l++){
                    if(i + k < n && j + l < n && a[i+k][j+l] == b[k][l]){
                        res += 1;
                    }
                }
            }
            if(res == m*m){
                return "Yes";
            }
            
        }
    }
    
    return "No";
    
    
}





int main(){
    
    int n, m;
    cin >> n >> m;
    vector<string>a(n), b(m);
    
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < m; i++){
        cin >> b[i];
    }
    
    cout << solve(a, b) << endl;
    
}
