Readme file:

1. Algorithm : Ricart–Agrawala algorithm using timestamp
  File Name: rec_timestamp.da
  
  This algorithm uses timestamp to schedule the process in distributed systems.


Datasets for each process:
          d = []   //array to store deferred replies
          reqId = 0  //request id currently served
          reqc = -1  //current logical time stamp
          inCS = 0   //flag for showing whether the process is in critical section 
          isReq = 0  //flag for showing whether process is in request section or not

Functions/Methods used by each process:
 1. def setup(s,reqQueue,process_id,no_req)
 2. def cs(task,req_to_serve,flag):
 3. def main()
 4. def OnRequest(req)

Sample Output:

 STARTING RICART TIMESTAMP 

[2013-10-04 23:34:46,151]runtime:INFO: Creating instances of Ptimestamp..
[2013-10-04 23:34:46,170]runtime:INFO: 3 instances of Ptimestamp created.
[2013-10-04 23:34:46,173]runtime:INFO: Starting procs...
[2013-10-04 23:34:46,174]Ptimestamp(('mrinal-XPS-L501X', 22775)):INFO: Process no: 2 request cs for Request no: 6
[2013-10-04 23:34:46,174]Ptimestamp(('mrinal-XPS-L501X', 38473)):INFO: Process no: 1 request cs for Request no: 2
[2013-10-04 23:34:46,174]Ptimestamp(('mrinal-XPS-L501X', 39412)):INFO: Process no: 3 request cs for Request no: 1
[2013-10-04 23:34:46,176]Ptimestamp(('mrinal-XPS-L501X', 22775)):INFO: Process no: 2 in cs for Request No: 6
[2013-10-04 23:34:49,129]Ptimestamp(('mrinal-XPS-L501X', 22775)):INFO: Process no: 2 release cs for Request No: 6
[2013-10-04 23:34:49,130]Ptimestamp(('mrinal-XPS-L501X', 38473)):INFO: Process no: 1 in cs for Request No: 2
[2013-10-04 23:34:49,130]Ptimestamp(('mrinal-XPS-L501X', 22775)):INFO: Process no: 2 request cs for Request no: 5
[2013-10-04 23:34:50,963]Ptimestamp(('mrinal-XPS-L501X', 38473)):INFO: Process no: 1 release cs for Request No: 2
[2013-10-04 23:34:50,964]Ptimestamp(('mrinal-XPS-L501X', 38473)):INFO: Process no: 1 request cs for Request no: 4
[2013-10-04 23:34:50,964]Ptimestamp(('mrinal-XPS-L501X', 39412)):INFO: Process no: 3 in cs for Request No: 1
[2013-10-04 23:34:52,006]Ptimestamp(('mrinal-XPS-L501X', 39412)):INFO: Process no: 3 release cs for Request No: 1
[2013-10-04 23:34:52,007]Ptimestamp(('mrinal-XPS-L501X', 39412)):INFO: Process no: 3 request cs for Request no: 3
[2013-10-04 23:34:52,007]Ptimestamp(('mrinal-XPS-L501X', 22775)):INFO: Process no: 2 in cs for Request No: 5
[2013-10-04 23:34:53,609]Ptimestamp(('mrinal-XPS-L501X', 22775)):INFO: Process no: 2 release cs for Request No: 5
[2013-10-04 23:34:53,610]Ptimestamp(('mrinal-XPS-L501X', 38473)):INFO: Process no: 1 in cs for Request No: 4
[2013-10-04 23:34:54,582]Ptimestamp(('mrinal-XPS-L501X', 38473)):INFO: Process no: 1 release cs for Request No: 4
[2013-10-04 23:34:54,583]Ptimestamp(('mrinal-XPS-L501X', 39412)):INFO: Process no: 3 in cs for Request No: 3
[2013-10-04 23:34:56,695]Ptimestamp(('mrinal-XPS-L501X', 39412)):INFO: Process no: 3 release cs for Request No: 3



2.Algorithm : Ricart–Agrawala algorithm using timestamp (efficient)
  File Name: rec_timestamp_eff.da


The algorithm uses the same implementation but coded in a efficient way. The algorithm uses following techniques for enhancing the performance:

1. Maintaing a list of all the replies we have received till now. Using it we can avoid the any and or statements in the await condition.

2. Conversion of List Comprehensions into Loop: In the clear version, we used list comprehension for clarity. But in clear version we removed it.

3. Use of multiple assignments: In the efficient version we used multiple assignments to speed up the process.


4. Conversion of condition inside await to a function: Instead of evaluating the same complex expression multiple number of times, we have moved the expression to a function and returned a flag that denotes the truth of condition of expression.



Datasets for each process:
          d = []   //array to store deferred replies
          reqId = 0  //request id currently served
          reqc = -1  //current logical time stamp
          inCS = 0   //flag for showing whether the process is in critical section 
          isReq = 0  //flag for showing whether process is in request section or not
          rec_reply = {} //array to store which process has received reply
          rep_counter = 0 //counter to check how many replies we have received

Functions/Methods used by each process:
 1. def setup(s,reqQueue,process_id,no_req)
 2. def cs(task,req_to_serve,flag)
 3. def main()
 4. def OnRequest(req)
 5. def OnReply(time,reqs)

Sample Output:

 STARTING RICART TIMESTAMP EFFICIENT

[2013-10-04 23:35:12,744]runtime:INFO: Creating instances of Ptimestamp..
[2013-10-04 23:35:12,749]runtime:INFO: 3 instances of Ptimestamp created.
[2013-10-04 23:35:12,754]runtime:INFO: Starting procs...
[2013-10-04 23:35:12,755]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 request cs for Request no: 2
[2013-10-04 23:35:12,755]Ptimestamp(('mrinal-XPS-L501X', 22112)):INFO: Process no: 2 request cs for Request no: 1
[2013-10-04 23:35:12,756]Ptimestamp(('mrinal-XPS-L501X', 18205)):INFO: Process no: 3 request cs for Request no: 3
[2013-10-04 23:35:12,761]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 in cs for Request No: 2
[2013-10-04 23:35:13,762]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 release cs for Request No: 2
[2013-10-04 23:35:13,763]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 request cs for Request no: 4
[2013-10-04 23:35:13,764]Ptimestamp(('mrinal-XPS-L501X', 18205)):INFO: Process no: 3 in cs for Request No: 3
[2013-10-04 23:35:14,995]Ptimestamp(('mrinal-XPS-L501X', 18205)):INFO: Process no: 3 release cs for Request No: 3
[2013-10-04 23:35:14,997]Ptimestamp(('mrinal-XPS-L501X', 18205)):INFO: Process no: 3 request cs for Request no: 5
[2013-10-04 23:35:14,997]Ptimestamp(('mrinal-XPS-L501X', 22112)):INFO: Process no: 2 in cs for Request No: 1
[2013-10-04 23:35:15,798]Ptimestamp(('mrinal-XPS-L501X', 22112)):INFO: Process no: 2 release cs for Request No: 1
[2013-10-04 23:35:15,799]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 in cs for Request No: 4
[2013-10-04 23:35:15,799]Ptimestamp(('mrinal-XPS-L501X', 22112)):INFO: Process no: 2 request cs for Request no: 6
[2013-10-04 23:35:16,870]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 release cs for Request No: 4
[2013-10-04 23:35:16,872]Ptimestamp(('mrinal-XPS-L501X', 18205)):INFO: Process no: 3 in cs for Request No: 5
[2013-10-04 23:35:16,872]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 request cs for Request no: 7
[2013-10-04 23:35:18,123]Ptimestamp(('mrinal-XPS-L501X', 18205)):INFO: Process no: 3 release cs for Request No: 5
[2013-10-04 23:35:18,125]Ptimestamp(('mrinal-XPS-L501X', 22112)):INFO: Process no: 2 in cs for Request No: 6
[2013-10-04 23:35:19,927]Ptimestamp(('mrinal-XPS-L501X', 22112)):INFO: Process no: 2 release cs for Request No: 6
[2013-10-04 23:35:19,928]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 in cs for Request No: 7
[2013-10-04 23:35:19,979]Ptimestamp(('mrinal-XPS-L501X', 11390)):INFO: Process no: 1 release cs for Request No: 7


3. Algorithm : Ricart–Agrawala algorithm using token
  File Name: rec_token.da
  
  This algorithm uses timestamp to schedule the process in distributed systems.


Datasets for each process:
      reqc = 0  //the logical clock when the request is sent
      reqId = 0 // the request id which is currently served
      request = {} // array of logical time when last time process requested for critical section
      token = {}   //last time when token was given to a process
      token_present = False // flag to show whether the token is presently at process and its using it
      token_held = False  // flag to show whether token is held by the process
      processList = list(s) // the list of process in the order in which we need to send the token


Functions/Methods used by each process:
1. def setup(s,reqQueue,process_id)
2. def cs(task)
3. def main()
4. def OnRequest(req)

Sample Output:

 STARTING RICART TOKEN 

[2013-10-04 23:35:20,010]runtime:INFO: Creating instances of Ptoken..
[2013-10-04 23:35:20,014]runtime:INFO: 3 instances of Ptoken created.
[2013-10-04 23:35:20,017]runtime:INFO: Starting procs...
[2013-10-04 23:35:20,017]Ptoken(('mrinal-XPS-L501X', 35346)):INFO: Process no: 1 request cs for Request no: 1
[2013-10-04 23:35:20,018]Ptoken(('mrinal-XPS-L501X', 35346)):INFO: Process no: 1 in cs for Request No: 1
[2013-10-04 23:35:20,018]Ptoken(('mrinal-XPS-L501X', 19487)):INFO: Process no: 2 request cs for Request no: 4
[2013-10-04 23:35:20,018]Ptoken(('mrinal-XPS-L501X', 36340)):INFO: Process no: 3 request cs for Request no: 2
[2013-10-04 23:35:22,571]Ptoken(('mrinal-XPS-L501X', 35346)):INFO: Process no: 1 release cs for Request No: 1
[2013-10-04 23:35:22,572]Ptoken(('mrinal-XPS-L501X', 19487)):INFO: Process no: 2 in cs for Request No: 4
[2013-10-04 23:35:22,572]Ptoken(('mrinal-XPS-L501X', 35346)):INFO: Process no: 1 request cs for Request no: 3
[2013-10-04 23:35:24,925]Ptoken(('mrinal-XPS-L501X', 19487)):INFO: Process no: 2 release cs for Request No: 4
[2013-10-04 23:35:24,926]Ptoken(('mrinal-XPS-L501X', 19487)):INFO: Process no: 2 request cs for Request no: 6
[2013-10-04 23:35:24,926]Ptoken(('mrinal-XPS-L501X', 35346)):INFO: Process no: 1 in cs for Request No: 3
[2013-10-04 23:35:24,926]Ptoken(('mrinal-XPS-L501X', 19487)):INFO: Process no: 2 in cs for Request No: 6
[2013-10-04 23:35:28,050]Ptoken(('mrinal-XPS-L501X', 19487)):INFO: Process no: 2 release cs for Request No: 6
[2013-10-04 23:35:28,430]Ptoken(('mrinal-XPS-L501X', 35346)):INFO: Process no: 1 release cs for Request No: 3
[2013-10-04 23:35:28,431]Ptoken(('mrinal-XPS-L501X', 36340)):INFO: Process no: 3 in cs for Request No: 2
[2013-10-04 23:35:29,853]Ptoken(('mrinal-XPS-L501X', 36340)):INFO: Process no: 3 release cs for Request No: 2
[2013-10-04 23:35:29,854]Ptoken(('mrinal-XPS-L501X', 36340)):INFO: Process no: 3 request cs for Request no: 5
[2013-10-04 23:35:29,856]Ptoken(('mrinal-XPS-L501X', 36340)):INFO: Process no: 3 in cs for Request No: 5
[2013-10-04 23:35:31,488]Ptoken(('mrinal-XPS-L501X', 36340)):INFO: Process no: 3 release cs for Request No: 5


4.Algorithm : Ricart–Agrawala algorithm using token(efficient)
  File Name: rec_token_eff.da


The algorithm uses the same implementation but coded in a efficient way. The algorithm uses following techniques for enhancing the performance:
1. Conversion of List Comprehensions into Loop: In the clear version, we used list comprehension for clarity. But in clear version we removed it.

2. Use of multiple assignments: In the efficient version we used multiple assignments to speed up the process.

3. Conversion of condition inside await to a function: Instead of evaluating the same complex expression multiple number of times, we have moved the expression to a function and returned a flag that denotes the truth of condition of expression.


Datasets for each process:
      reqc = 0
      reqId = 0
      request = {}
      token = {}
      token_present = False
      token_held = False
      processList = list(s)

Functions/Methods used by each process:
1. def setup(s,reqQueue,process_id)
2. def cs(task)
3. def main()
4. def OnRequest(req)


Sample Output:

 STARTING RICART TOKEN EFFICIENT

[2013-10-04 23:35:42,521]runtime:INFO: Creating instances of Ptoken..
[2013-10-04 23:35:42,526]runtime:INFO: 3 instances of Ptoken created.
[2013-10-04 23:35:42,530]runtime:INFO: Starting procs...
[2013-10-04 23:35:42,531]Ptoken(('mrinal-XPS-L501X', 25392)):INFO: Process no: 2 request cs for Request no: 4
[2013-10-04 23:35:42,531]Ptoken(('mrinal-XPS-L501X', 14055)):INFO: Process no: 3 request cs for Request no: 3
[2013-10-04 23:35:42,531]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 request cs for Request no: 7
[2013-10-04 23:35:42,532]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 in cs for Request No: 7
[2013-10-04 23:35:43,233]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 release cs for Request No: 7
[2013-10-04 23:35:43,234]Ptoken(('mrinal-XPS-L501X', 25392)):INFO: Process no: 2 in cs for Request No: 4
[2013-10-04 23:35:43,234]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 request cs for Request no: 2
[2013-10-04 23:35:44,746]Ptoken(('mrinal-XPS-L501X', 25392)):INFO: Process no: 2 release cs for Request No: 4
[2013-10-04 23:35:44,747]Ptoken(('mrinal-XPS-L501X', 25392)):INFO: Process no: 2 request cs for Request no: 5
[2013-10-04 23:35:44,747]Ptoken(('mrinal-XPS-L501X', 14055)):INFO: Process no: 3 in cs for Request No: 3
[2013-10-04 23:35:44,748]Ptoken(('mrinal-XPS-L501X', 25392)):INFO: Process no: 2 in cs for Request No: 5
[2013-10-04 23:35:44,778]Ptoken(('mrinal-XPS-L501X', 14055)):INFO: Process no: 3 release cs for Request No: 3
[2013-10-04 23:35:44,779]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 in cs for Request No: 2
[2013-10-04 23:35:44,779]Ptoken(('mrinal-XPS-L501X', 14055)):INFO: Process no: 3 request cs for Request no: 6
[2013-10-04 23:35:44,780]Ptoken(('mrinal-XPS-L501X', 14055)):INFO: Process no: 3 in cs for Request No: 6
[2013-10-04 23:35:45,491]Ptoken(('mrinal-XPS-L501X', 14055)):INFO: Process no: 3 release cs for Request No: 6
[2013-10-04 23:35:45,549]Ptoken(('mrinal-XPS-L501X', 25392)):INFO: Process no: 2 release cs for Request No: 5
[2013-10-04 23:35:45,710]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 release cs for Request No: 2
[2013-10-04 23:35:45,711]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 request cs for Request no: 1
[2013-10-04 23:35:45,713]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 in cs for Request No: 1
[2013-10-04 23:35:47,374]Ptoken(('mrinal-XPS-L501X', 23784)):INFO: Process no: 1 release cs for Request No: 1

5. Compariasion of performances: We have compared the performances by running the process of timestamp and token over certain period of times
    and taking the average of all the performances. Sample output for 3 processes and 6 requests , 2 times and incrementing by 2 each time.
    Here is the result of our analysis:

Time analysis for Ricart Timestamp-Clear
Runtime for pass 0: 10.567081689834595 seconds
Runtime for pass 1: 9.356094121932983 seconds


Time analysis for Ricart Timestamp-Efficient
Runtime for pass 0: 6.6891186237335205 seconds
Runtime for pass 1: 7.238054990768433 seconds


Time analysis for Ricart Token-Clear
Runtime for pass 0: 11.5093834400177 seconds
Runtime for pass 1: 8.138656377792358 seconds


Time analysis for Ricart Token-Efficient
Runtime for pass 0: 2.8909730911254883 seconds
Runtime for pass 1: 4.856569528579712 seconds


 Algorithm Name                                           Average Time
Ricart Timestamp-Clear                       9.961587905883789 seconds
Ricart Timestamp-Efficient                       6.963586807250977 seconds
Ricart Token-Clear                       9.82401990890503 seconds
Ricart Token-Efficient                       3.8737713098526 seconds


