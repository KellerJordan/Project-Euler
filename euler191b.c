// dynamic solution in c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int t(int n, int* r) {
    if (n <= 0) return 1;
    if (r[n - 1] != 0) return r[n - 1];
    
    int count = t(n - 2, r) + t(n - 1, r);
    if (n > 1) count += t(n - 3, r);

    r[n - 1] = count;
    return count;
}

int T(int n, int* r) {
    int count = t(n, r);
    for (int i = 0; i < n; i++) count += t(i, r) * t(n - 1 - i, r);
    return count;
}


int main() {
    clock_t begin = clock();
    static int r[30 + 1];
    printf("Result = %d\n", T(30, r));
    clock_t end = clock();
    printf("Computation took %lf time", (double)(end - begin) / CLOCKS_PER_SEC);
}
