#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int z = 1;
    while (i != 100) {
        z = z * 2;
        cout << "#" << i << "#" << z << endl;
        i = i + 1;
    }
    return 0;
}