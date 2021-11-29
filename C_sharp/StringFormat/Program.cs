using System.Collections.Generic;
using System;

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

List<string> names = new List<string>()
{
    "Luca",
    "Matteo",
    "Thomas"
};

Console.WriteLine(String.Format("Il mio nome è {0}, ma i miei amici si chiamano {1} e {2}", names[0], names[1], names[2]));