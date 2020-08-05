#include <bits/stdc++.h>
using namespace std;





int main(){
    
    string ss;
    cin >> ss;
    int n = ss.size();
    vector<int>a(n, 0);
    vector<int>previous(n, 1);
    
    int idx = 0;
    while(idx < 100000){
        for(int i = 0; i < n ; i++){
            if(ss[i] == 'L' && previous[i] > 0){
                a[i-1] += previous[i];
                //previous[i] = 0;
            }else if(ss[i] == 'R' && previous[i] > 0){
                a[i + 1]  += previous[i];
                 //previous[i] = 0;
            }
        }
        previous = a;
        fill(a.begin(), a.end(), 0);
        idx += 1;
    }
    
    for(int i = 0; i < n; i++){
        cout << previous[i] << " ";
    }cout << endl;
    
    
    
    return 0;
}
