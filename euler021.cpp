#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


vector<int> amicable_numbers;

int sum_divisors(unsigned int n) {
    int s = 1;
    for (int i = 2; i <= sqrt(n); i++) {
        if(n % i == 0)
            s += i + (int)n/i;
    }
    return s;
}

int sum_amicable_numbers(int n) {
    int sum = 0;
    for (int i = 0; i < amicable_numbers.size(); i++) {
        int a = amicable_numbers[i];
        if (a <= n) sum += a;
        else break;
    }
    return sum;
}

int main() {
    for (int a = 2; a <= 100000; a++) {
        int b = sum_divisors(a);
        if (b != a && sum_divisors(b) == a) amicable_numbers.push_back(a);
    }
    
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        int ans = sum_amicable_numbers(n);
        cout << ans << endl;
    }
    return 0;
}