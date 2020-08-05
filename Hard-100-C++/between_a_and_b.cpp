#include <bits/stdc++.h>
using namespace std;

int main(){
    
    
    long long a, b, x;
    cin >> a >> b >> x;
    
    long long r;
    if(a != 0){
        r = a%x;
    }else{
        r = a;
    }
    
    long long last = b%x;
    b -= last;
    if(r != 0)a += (x - r);
    
    
    //cout << a << " " << b << " " << endl;
    if(a > b){
        cout << 0 << endl;
        return 0;
    }
    
    
    //cout << a << " " << b << " " << endl;
    long long value = (b - a)/x + 1;
    
    cout << value << endl;
    
    
}
