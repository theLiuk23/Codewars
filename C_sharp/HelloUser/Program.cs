﻿using System;

namespace HelloUser
{
    class Program
    {
        static void Main(string[] args)
        {
            string username = Environment.UserName;
            Console.WriteLine("Hello {0}!", Environment.UserName);
        }
    }
}
