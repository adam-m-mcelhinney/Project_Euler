using System;
namespace euler
{
    public class Divisors
    {
        int n;
        int i;
        public Divisors(int n)
        {
            this.n = n;
            int maxN = (n/2)+1;
            // Array to hold the resulting output set
            int [] output = new int[maxN];
            List<int> output = new List<int>();

            for (i=0; i< maxN; i++){
                output[i] = i;
                Console.WriteLine(i);
                }
            //Console.WriteLine("Hello World!" + n + maxN );

        }
    }
}
