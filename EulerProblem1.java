/**
 * PROBLEM DESCRIPTION:
 * If we list all the natural numbers below 10 that are multiples of 3 or 5,
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */


public class EulerProblem1 {
    /**
     * solves Euler problem 1 in a naive, brute force method.
     * @return the sum of all the multiples of 3 or 5 below 1000
     */
    public static int naiveMethod(){
        int sum = 0;
        for (int i = 0; i < 1000; i++){
            // as 15 is a multiple of both 3 and 5, 
            //we must prevent it from being double counted. Short-circuiting
            //helps ensure this
            if (i % 3 == 0 || i % 5 == 0 )
                    sum += i;
        }
    return sum;
    }
    
    /**
     * solve the problem in a more sophisticated way, using arithmetic
     * progression
     * @return the sum of all the multiples of 3 or 5 below 1000
     */
    public static int cleverMethod(){
        /**to solve the problem, we need the sum of the multiples up to 1000
         * less the multiples of 15
         * 
         * ~~written out, we can express this problem as below~~
         * sum = (multiples of 3) + (multiples of 5) - (multiples of 15)
         * 
         * ~~more formally we get the expanded equation~~
         *     = (3+6+9+...+ 999) + (5+10+15+...+995) - (15+30+45+...+990)
         * 
         * ~~we can further extract the greatest common factor from each term~~
         *     = 3(1+2+3+...+ 333) + 5(1+2+3+...+199) - 15(1+2+3+...+ 66)
         * 
         * we can quickly find the sum of the arithmetic progression
         * (AKA. a arithmetic series) by using the formula
         *                       n(a+b)/2
         * where 
         * a = the first number in the series
         * b = the last number in the series
         * n = the number of terms in the series
         * 
         * using this formula, we can simply call a method to find the
         * arithmetic series, multiply it by our greatest common factor, and
         * sum them together
         */
        //sum of multiples of 3
        int multsOf3 = findArithmeticSeries(1,333,333);
        //sum of multiples of 5
        int multsOf5 = findArithmeticSeries(1,199,199);
        //sum of multiples of 15
        int multsOf15 = findArithmeticSeries(1,66,66);
        int ans = (3 * multsOf3) + (5 * multsOf5) - (15 * multsOf15);
        return ans;
    }
    /**
     * sums the the sequence of n numbers from a to b in O(1)
     * @param a the first number in the arithmetic progression
     * @param b the last number in the arithmetic progression
     * @param n the number of terms in the arithmetic progression
     * @return the arithmetic sum/series of the n numbers from a to b
     */
    public static int findArithmeticSeries(int a, int b, int n){
        int ans = n * (a + b)/2;
        return ans;
        }

    public static void main(String[] args) {
        System.out.println(cleverMethod());
        System.out.println(naiveMethod());
    }

}
