#include "SM3.h"

int main() {
    string data = "Hello, world!";
    SM3 sm3;

    string hashValue;
    auto t1 = chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++)
        hashValue = sm3.hash(data);
    auto t2 = chrono::high_resolution_clock::now();
    auto t3 = chrono::duration_cast<chrono::milliseconds>(t2 - t1);

    cout << "Message: " << data << '\n';
    cout << "Hash value: " << hashValue << '\n';
    cout << "Time of 1000000 times encryption: " << t3.count() << "ms\n";
    cout << "Average time: " << t3.count() / double(1000000) << "ms\n";

    return 0;
}
