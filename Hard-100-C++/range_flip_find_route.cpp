#include <bits/stdc++.h>
using namespace std;

int h, w;
vector<string>a;

const int inf = (int)1e+9 + 7;

map<pair<int, int>, int>m;
int solve(int row, int col){
    
    if(m.find({row, col}) != m.end()){
        return m[{row, col}];
    }
    int current_min;
    if(row == h-1 && col == w-1){
        if(a[row][col] == '#') return 1;
        else return 0;
    }
    if(row >= h || col >= w){
        return inf;
    }
    
    int min1 = solve(row, col + 1);
    int min2 = solve(row + 1, col);
    if(a[row][col] == '#'){
        current_min = min(min1, min2) + 1;
    }else{
        current_min = min(min1, min2);
    }
    
    //cout << row << " " << col << " " << current_min << endl;
    
    return m[{row, col}] = current_min;
    
}




int main(){
    
    cin >> h >> w;
    a.resize(h);
    m.clear();
    for(int i = 0; i < h; i++){
        cin >> a[i];
    }
    
    cout << solve(0, 0) << endl;
    
}
