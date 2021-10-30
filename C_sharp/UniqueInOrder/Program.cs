using System;
using System.Collections.Generic;

namespace UniqueInOrder
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Convert.ToString(UniqueInOrder("ASDAWFAS")));
        }

        public static IEnumerable<T> UniqueInOrder<T>(IEnumerable<T> iterable)
        {
            IEnumerable<T> usedItems = new T[]{};
            IEnumerable<T> solution = new T[]{};

            foreach (IEnumerable<T> item in iterable)
            {
                if (!usedItems.Contains(item))
                {
                    solution = solution.add(item);
                    usedItems.Concat(item);
                }
            }

            return solution;
        }
    }
}
