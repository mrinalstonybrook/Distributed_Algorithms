import threading;
import sys;
import random;
import time;

#Global variables
NoOfThreads = 0;
NoOfRequests = 0;
b = [];
y = 0;
x = 0;
choosing = [];
num = [];


# Lamport's Bakery algorithm

class BakeryThreadProcess(threading.Thread):
   tId = 0;
   requestNo=0;
  
   def __init__(self,tId,requestNo):
     threading.Thread.__init__(self);
     self.tId = tId;
     self.requestNo = requestNo;

   def run(self):
     self.reqcriticalsection();
	 
   def criticalsection(self):
     print(" Inside critical section by thread "+  str(self.tId) + " after doing the request " + str(self.requestNo) + "\n");
	 
   def reqcriticalsection(self):
     global choosing;
     global num;
     global NoOfRequests;
     global NoOfThreads;
     print(" Requesting for critical section by thread "+  str(self.tId) + " for the request " + str(self.requestNo) + "\n");
     choosing[self.requestNo] = 1;
     max = 0;
     for i in range(NoOfRequests):
        if(max < num[i]):
           max = num[i];
     num[self.requestNo] = max + 1;
     choosing[self.requestNo] = 0;
     for j in range(NoOfRequests):
        while choosing[j] != 0:
           pass;
        while num[j] != 0 and num[j] < num[self.requestNo]: #and not(num[j] == num[self.requestNo] and j < self.requestNo):
           pass;
     print(" Entering critical section by thread "+  str(self.tId) + " for doing the request " + str(self.requestNo) + "\n");
     self.criticalsection();
     print(" Exiting critical section by thread "+  str(self.tId) + " after doing the request " + str(self.requestNo) + "\n");
     num[self.requestNo]=0;

#Lamport's fast mutual exclusion algorithm
     
class FastThreadProcess(threading.Thread):
   tId = 0;
   requestNo=0;
  
   def __init__(self,tId,requestNo):
     threading.Thread.__init__(self);
     self.tId = tId;
     self.requestNo = requestNo;

   def run(self):
     self.reqcriticalsection();
	 
   def criticalsection(self):
     print(" Inside critical section by thread "+  str(self.tId) + " after doing the request " + str(self.requestNo) + "\n");
	 
   def reqcriticalsection(self):
     global b;
     global y;
     global x;
     global NoOfThreads;
     global NoOfRequests;
     start = True;
     print(" Requesting for critical section by thread "+  str(self.tId) + " for the request " + str(self.requestNo) + "\n");
     while start:
        b[self.requestNo] = 1;
        x = self.requestNo;
        if y != 0:
             b[self.requestNo]=0;
             while y != 0:
               pass;
             continue;
        else:
           y = self.requestNo;
           if x != self.requestNo:
              b[self.requestNo] = 0;
              for i in range(NoOfRequests):
                 while b[i] != 0:
                    pass;
              if (y!= self.requestNo):
                 while y != 0:
                    pass;
                 continue;
        start = False;
        
     print(" Entering critical section by thread "+  str(self.tId) + " and for doing the request " + str(self.requestNo) + "\n");
     self.criticalsection();
     print(" Exiting critical section by thread "+  str(self.tId) + " and for doing the request " + str(self.requestNo) + "\n");
     y=0;
     b[self.tId]=0;


#Initial setup for both the algorithms
     
def intialsetup(arg_NoOfThreads,arg_NoOfRequests,arg_AlgoType):
   global NoOfThreads;
   global NoOfRequests;
   NoOfThreads = arg_NoOfThreads;
   NoOfRequests = arg_NoOfRequests;
   print("No of Threads (starting from 0) : " + str(NoOfThreads));
   print("No of Requests (starting from 0) : " + str(NoOfRequests) + "\n\n");
   threadList = [];

   if (arg_AlgoType == "Fast"):
      print("Running Lamport's fast algorithm\n\n");
      for i in range(NoOfRequests):
         b.append(0);
         
   if (arg_AlgoType == "Bakery"):
      print("Running Lamport's bakery algorithm\n\n");
      for i in range(NoOfRequests):
         choosing.append(0);
         num.append(0);

   requestList = list(range(NoOfRequests));
   random.shuffle(requestList);
   print("Thread request assignment started:")

   for j in range(len(requestList)):
      newRequest = random.choice(requestList);
      requestList.remove(newRequest);
      if (arg_AlgoType == "Fast"):
         newThread = FastThreadProcess(j%NoOfThreads,newRequest);
      if (arg_AlgoType == "Bakery"):
         newThread = BakeryThreadProcess(j%NoOfThreads,newRequest);
      threadList.append(newThread);
      print("Thread " + str(j%NoOfThreads) + " is assigned with Request" + str(newRequest));	  
   
   random.shuffle(threadList);
   for count in range(NoOfRequests):
     threadList[count].start();
   for count in range(NoOfRequests):
      threadList[count].join();

      
#Calling both the algorithms with a small gap
      
intialsetup(int(sys.argv[1]),int(sys.argv[2]),"Fast");
time.sleep(1);
intialsetup(int(sys.argv[1]),int(sys.argv[2]),"Bakery");
