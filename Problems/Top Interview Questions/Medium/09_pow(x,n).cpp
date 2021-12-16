// https://leetcode.com/problems/powx-n/

class Solution {
public:
    double myPow(double x, long int n) {
        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            return 1.0 / myPow(x, -n);
        }
        double pow = 1.0;
        while (n > 0) {
            if (n % 2 == 1) {
                pow *= x;
            }
            x *= x;
            n /= 2;
        }
        return pow;
    }
};
