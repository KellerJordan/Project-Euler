// non dynamic solution in c++

#include <iostream>
#include <cmath>

using namespace std;

// counts prize strings of n length with previous characters c0, c1
int count_substrings_helper(char c0, char c1, int n) {
    int count = 0;
    if (n > 0) {
        // can always have next character be 'O'
        count += count_substrings_helper(c1, 'O', n - 1);

        // if last two characters aren't 'AA', then can have next char be 'A'
        if (!(c0 == 'A' && c1 == 'A'))
            count += count_substrings_helper(c1, 'A', n - 1);
    } else {
        count += 1;
    }
    return count;
}

// count number of prize strings with only 'A', 'O' characters and length n
int count_substrings(int n) {
    return count_substrings_helper('O', 'O', n);
}

// counts number of prize strings of length n
int count_prizestrings(int n) {
    int count = 0;

    for (int i = 0; i < n; i++) {
        int j = n - 1 - i;
        count += count_substrings(i) * count_substrings(j);
    }

    count += count_substrings(n);
    return count;
}

int main() {
    int n = 30;

    int count = count_prizestrings(n);
    cout << count << endl;
}
