#include <bits/stdc++.h>
using namespace std;
 
 
void solve(string &s){
    
    int n = s.size();
    vector<int>result(n);
    
    int current_l = -1;
    int final_l = -1; 
    int start_r = 0;
    for(int i = 0; i < n; i++){
        if(s[i] == 'L' && current_l == -1){
            current_l = i;
        }
        if((s[i] == 'L' && s[i+1] == 'R') || i == n-1){
            final_l = i;
        }
        
        if(current_l != -1 && final_l != -1){
            int border_idx_1 = current_l;
            int border_idx_2 = current_l - 1;
            
            //cout << start_r << " " << current_l << " " << final_l << endl;
            // Now the odd idxs will go in the border_idx that is odd and vice versa
            int total_values = final_l - start_r + 1;
            
            if((border_idx_1 - start_r)%2){
                result[border_idx_2] = (final_l - start_r + 1)/2;
                result[border_idx_1] = (final_l - start_r + 1)/2;
                if(total_values%2){
                    result[border_idx_2] += 1;
                }
            }else{
                result[border_idx_2] = (final_l - start_r + 1)/2;
                result[border_idx_1] = (final_l - start_r + 1)/2 ;
                if(total_values%2){
                    result[border_idx_1] += 1;
                }
            }
            
            start_r = final_l + 1;
            current_l = -1;
            final_l = -1;
        }
    }
    
    for(int i = 0; i < n; i++){
        cout << result[i] << " ";
    }cout << endl;
    
    
    
}
 
 
 
 
 
int main(){
    
    string s;
    cin >> s;
    
    solve(s);
    
    
} 
