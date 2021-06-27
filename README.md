# kspcfgparse - KSP .cfg file parser
 
An incomplete parser intended to parse very large saves and craft files from Kerbal Space Program.

*Working on this might just be a waste of time but who knows...*

A few key design choices were kept in mind to keep the project clean and performant:
* Leverages a bit of functional programming using a simple Parser Combinator
* Does not copy or reallocate the source data

## Features:

TODO

Some test results with parsing craft files:
```
[TEST] Crafts:
Loading craft: Kaytrav TN7.craft
* Parsing (70869 chars)...
* [successful: True] [time: 13.43ms] [chars/s: 5278006.7]
* Part Count: 43
Loading craft: Suwubi - 37C.craft
* Parsing (7348540 chars)...
* [successful: True] [time: 1096.8ms] [chars/s: 6700003.8]
* Part Count: 5872
Loading craft: YF-23 backup 69.craft
* Parsing (225590 chars)...
* [successful: True] [time: 56.71ms] [chars/s: 3977760.5]
* Part Count: 6900
```

TODO: document this, and adhere to more proper python conventions
