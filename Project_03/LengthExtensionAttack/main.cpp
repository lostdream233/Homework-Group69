#include "SM3.h"

int main() {
    string m1 = "Hello, world!";
    string m2 = "2023";
    SM3 sm3;

    string m2_bin = sm3.strTobin(m2);
    string message_pad = sm3.messagePadding(m1) + m2_bin;
    int len = message_pad.length();

    string padOfLen = bitset<32>(len).to_string();
    string zeroString(64 - padOfLen.length(), '0');
    padOfLen = zeroString + padOfLen;
    message_pad = message_pad + "1" + string(959 - len, '0') + padOfLen;

    string M_hex;
    for (int i = 0; i < 1024; i += 4) {
        bitset<4> bits(message_pad.substr(i, 4));
        unsigned long long intValue = bits.to_ullong();
        stringstream ss;
        ss << std::hex << intValue;
        string hexValue = ss.str();
        M_hex += hexValue;
    }
    cout << "M(padding): " << M_hex << '\n';

    int blockNum = message_pad.length() / 512;
    vector<vector<u_32>> B;
    B.reserve(blockNum);
    for (int i = 0; i < blockNum; i++) {
        string group = message_pad.substr(i * 512, 512);
        B.emplace_back(sm3.messageExtension(group));
    }

    string IV1 = sm3.IV;
    string IV2 = sm3.CF(IV1, B[0]);

    cout << "IV1: " << IV1 << '\n';
    cout << "IV2: " << IV2 << '\n';

    string V = sm3.IV;
    for (int i = 0; i < blockNum; i++)
        V = sm3.CF(V, B[i]);

    vector<u_32> B_attack = B[1];
    string V_attack = IV2;
    string res = sm3.CF(IV2, B[1]);

    cout << "Target hash: " << V << '\n';
    cout << "Attack hash: " << res << '\n';


    return 0;
}
