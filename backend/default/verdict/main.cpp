#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]){
    string out = argv[1];
    string user_out = argv[2];
    ifstream f_out(out.c_str());
    ifstream f_user_out(user_out.c_str());
    vector<string> a, b;
    string tmp;
    while(f_out >> tmp)
        a.push_back(tmp);
    while(f_user_out >> tmp)
        b.push_back(tmp);
    if(a == b)
        printf("AC 1.0");
    else
        printf("WA 0.0");
    return 0;
}


