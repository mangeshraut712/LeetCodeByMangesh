#include <math.h> // Required for pow, log10 if used, but can avoid

int countSymmetricIntegers(int low, int high) {
    int count = 0;
    for (int num = low; num <= high; ++num) {
        int temp = num;
        int num_digits = 0;
        if (temp == 0) {
            num_digits = 1; // Technically 0 isn't positive, but handle length
        } else {
             // Calculate number of digits without log10 or strings
             int n_temp = temp;
             while (n_temp > 0) {
                 n_temp /= 10;
                 num_digits++;
             }
        }

        if (num_digits % 2 == 0) {
            int first_half_sum = 0;
            int second_half_sum = 0;
            int divisor = 1;
            // Calculate divisor for the first half (10^(n/2))
            for(int i = 0; i < num_digits / 2; ++i) {
                divisor *= 10;
            }

            int first_half = temp / divisor;
            int second_half = temp % divisor;

            // Sum digits of second half
            temp = second_half;
            while (temp > 0) {
                second_half_sum += temp % 10;
                temp /= 10;
            }
            
             // Sum digits of first half
            temp = first_half;
             while (temp > 0) {
                first_half_sum += temp % 10;
                temp /= 10;
            }

            if (first_half_sum == second_half_sum && first_half_sum > 0) { // Ensure sums are non-zero if num > 0
                 count++;
            } else if (first_half_sum == 0 && second_half_sum == 0 && num == 0) {
                 // Handle case for 0 if needed, though problem asks for positive integers
                 // Symmetric definition applies to positive integers per description?
                 // Let's assume positive integers as per problem statement.
                 // If num=0, first_half=0, second_half=0, sums=0. But 0 has 1 digit (odd).
                 // Let's stick to the even digit count check.
            }
        }
    }
    return count;
}
