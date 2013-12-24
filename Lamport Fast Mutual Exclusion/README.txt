NAME : Mrinal Priyadarshi
SBU Id: 109281632
Assignment 2:

1. Lamport's Fast Mutual Exclusion algorithm:

For this algorithm, I have created two inputs as 

1. No of Threads
2. No of Requests

I have created a class 'FastThreadProcess' for implementing the algorithm.
It creates the threads and handle the request for critical section and the critical section itself.

Global variables used:
1. Array b
2. Var X
3. Var Y

The functions implemented by the class:
1. Criricalsection : The code in critical section
2. reqcriticalsection: The code for requesting the critical section.


Sample Output:

No of Threads (starting from 0) : 2
No of Requests (starting from 0) : 4


Running Lamport's fast algorithm


Thread request assignment started:

Thread 0 is assigned with Request2
Thread 1 is assigned with Request1
Thread 0 is assigned with Request3
Thread 1 is assigned with Request0

 Requesting for critical section by thread 0 for the request 3

 Entering critical section by thread 0 and for doing the request 3

 Inside critical section by thread 0 after doing the request 3

 Exiting critical section by thread 0 and for doing the request 3

 Requesting for critical section by thread 1 for the request 0

 Entering critical section by thread 1 and for doing the request 0

 Inside critical section by thread 1 after doing the request 0

 Exiting critical section by thread 1 and for doing the request 0

 Requesting for critical section by thread 1 for the request 1

 Entering critical section by thread 1 and for doing the request 1

 Inside critical section by thread 1 after doing the request 1

 Exiting critical section by thread 1 and for doing the request 1

 Requesting for critical section by thread 0 for the request 2

 Entering critical section by thread 0 and for doing the request 2

 Inside critical section by thread 0 after doing the request 2

 Exiting critical section by thread 0 and for doing the request 2


2. Lamport's Bakery algorithm:

For this algorithm, I have created two inputs as 

1. No of Threads
2. No of Requests

I have created a class 'FastThreadProcess' for implementing the algorithm.
It creates the threads and handle the request for critical section and the critical section itself.

Global variables used:
1. Array choosing
2. Array Num

The functions implemented by the class:
1. Criricalsection : The code in critical section
2. reqcriticalsection: The code for requesting the critical section.

Sample output:

No of Threads (starting from 0) : 2
No of Requests (starting from 0) : 4


Running Lamport's bakery algorithm

Thread request assignment started:

Thread 0 is assigned with Request0
Thread 1 is assigned with Request3
Thread 0 is assigned with Request1
Thread 1 is assigned with Request2


 Requesting for critical section by thread 1 for the request 3

 Entering critical section by thread 1 for doing the request 3

 Inside critical section by thread 1 after doing the request 3

 Exiting critical section by thread 1 after doing the request 3

 Requesting for critical section by thread 0 for the request 1

 Entering critical section by thread 0 for doing the request 1

 Inside critical section by thread 0 after doing the request 1

 Exiting critical section by thread 0 after doing the request 1

 Requesting for critical section by thread 0 for the request 0

 Entering critical section by thread 0 for doing the request 0

 Inside critical section by thread 0 after doing the request 0

 Exiting critical section by thread 0 after doing the request 0

 Requesting for critical section by thread 1 for the request 2

 Entering critical section by thread 1 for doing the request 2

 Inside critical section by thread 1 after doing the request 2

 Exiting critical section by thread 1 after doing the request 2