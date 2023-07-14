#include "SM4.h"
#include <sstream>

string decToHex(int_32 input){
    stringstream ss;
    ss<<std::hex<<input;

    return ss.str();
}

int main() {
    cout << "PT(HEX):  0123456789abcdeffedcba9876543210\n";
    cout << "Key(HEX): 0123456789abcdeffedcba9876543210\n";
    const int_32 MK[4] = {0x01234567, 0x89abcdef, 0xfedcba98, 0x76543210};
    const int_32 PT[4] = {0x01234567, 0x89abcdef, 0xfedcba98, 0x76543210};
    int_32 CT[4];
    auto t1 = chrono::high_resolution_clock::now();
    for (int i = 0; i < 640; i++) {
        SM4_Encrypt(MK, PT, CT);
    }
    auto t2 = chrono::high_resolution_clock::now();
    chrono::duration<double, milli> t3 = t2 - t1;
    cout << "Time cost: " << t3.count() / 640 << "ms\n";

    for (int i = 0; i < 4; i++) {
        if (i == 0) printf("CT: ");
        printf("%u ", CT[i]);
    }

    printf("\n");
    for (int i = 0; i < 4; i++) {
        if (i == 0) printf("CT(HEX):  ");
        cout<<decToHex(CT[i])<<" ";
    }

    return 0;
}
