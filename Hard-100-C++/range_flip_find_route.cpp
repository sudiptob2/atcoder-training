#include <bits/stdc++.h>
using namespace std;

long long h, w;
vector<string>a;

const long long inf = 1e+17;

long long solve(){
    long long dp[h][w][2];
    // [2] = {0 -- "#", 1 -- "."}
    //memset(dp, long long_MAX, sizeof(dp));
    for(long long i = 0; i < h; i++){
        for(long long j = 0; j < w; j++){
            //cout << dp[i][j][0] << dp[i][j][1] << " ";
            dp[i][j][0] = inf;
            dp[i][j][1] = inf;
        }
    }
    
    if(a[h-1][w-1] == '#'){
        dp[h-1][w-1][1] = 1;
    }else{
        dp[h-1][w-1][0] = 0;
    }
    
    // Fill the last row
    for(long long col = w-2; col >= 0; col --){
        long long row = h-1;
        long long current_value;
        if(a[row][col] == '.'){
                current_value = dp[row][col][0];
                current_value = min({current_value, dp[row][col+1][0], dp[row][col+1][1]});
                dp[row][col][0] = current_value;
            }else{
                current_value = dp[row][col][1];
                current_value = min({current_value, dp[row][col+1][0], dp[row][col+1][1]});
                
                if(current_value == dp[row][col+1][0] && a[row][col+1] == '.'){
                    current_value += 1;
                }
                dp[row][col][1] = current_value;
            }
    }
    
    // Fill the last column
    for(long long row = h-2; row >= 0; row--){
        long long col = w-1;
        long long current_value;
        if(a[row][col] == '.'){
                current_value = dp[row][col][0];
                current_value = min({current_value, dp[row+1][col][0], dp[row+1][col][1]});
                dp[row][col][0] = current_value;
            }else{
                current_value = dp[row][col][1];
                current_value = min({current_value, dp[row+1][col][0], dp[row+1][col][1] });
                
                if(current_value == dp[row+1][col][0] && a[row+1][col] == '.'){
                    current_value += 1;
                }
                dp[row][col][1] = current_value;
                
            }
    }
    
    
    
    
    // Fill everything else
    for(long long row = h-2; row >= 0; row--){
        for(long long col = w-2; col >= 0; col--){
            long long current_value;
            if(a[row][col] == '.'){
                current_value = dp[row][col][0];
                current_value = min({current_value, dp[row+1][col][0], dp[row+1][col][1], dp[row][col+1][0], dp[row][col+1][1]});
                dp[row][col][0] = current_value;
            }else{
                current_value = dp[row][col][1];
                current_value = min({current_value, dp[row+1][col][0], dp[row+1][col][1], dp[row][col+1][0], dp[row][col+1][1]});
                
                if(current_value == dp[row][col+1][0] && dp[row][col+1][0] < min(dp[row+1][col][1], dp[row][col+1][1]) && a[row][col+1] == '.'){
                    current_value += 1;
                }else if(current_value == dp[row+1][col][0] && dp[row+1][col][0] < min(dp[row+1][col][1], dp[row][col+1][1]) && a[row+1][col] == '.'){
                    current_value += 1;
                }
                dp[row][col][1] = current_value;
                
            }
        }
    }
    
    
    
    //for(long long i = 0; i < h; i++){
        //for(long long j = 0; j < w; j++){
            //long long one = dp[i][j][0];
            //long long two = dp[i][j][1];
            //printf("|. %lld # %lld| ", one, two);
        //}cout << endl;
    //}
    
    //for(long long i = 0; i < h; i++){
        //for(long long j = 0; j < w; j++){
            //cout << a[i][j] << " ";
        //}cout << endl;
    //}
    
    return min(dp[0][0][0], dp[0][0][1]);
    
    
}




int main(){
    
    cin >> h >> w;
    a.resize(h);
    for(long long i = 0; i < h; i++){
        cin >> a[i];
    }
    
    cout << solve() << endl;
    
}
