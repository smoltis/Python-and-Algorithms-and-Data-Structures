"""
Given a log file with API names, 
start and end timestamps, 
write a program that prints the average 
latency for each API call.

$ cat log
get_foo start 2222222100
get_foo end 2222222150
get_bar start 2222222200
get_foo start 2222222220
get_bar end 2222222230
get_foo end 2222222250
$ cat log | myprog
get_foo: average = 40
get_bar: average = 30

"""

import sys

if __name__ == "__main__":
#    lines = sys.stdin.readlines()
    with open("log.txt") as f:
        lines = f.readlines()
        #store API call as a key and collection [count, duration_sum] as value
        #temporary storage for starting records
        api_calls, api_calls_temp = {}, {}

        for line in lines:
            fields = line.split()
            api_call_name, api_call_type, api_call_ts = fields[0], fields[1], int(fields[2])
            #check start or end
            if api_call_type == "start":
                #add to temporary if key exists, rewrite with the latest 
                api_calls_temp[api_call_name] = api_call_ts
            elif api_call_type == "end":
                if api_call_name in api_calls_temp:
                    #calculate duration
                    api_calls[api_call_name] = [sum(x) for x in zip(api_calls.get(api_call_name, [0,0]) 
                                                                    , [1, api_call_ts - api_calls_temp[api_call_name]])]
                else:
                    print("Error, ending record without starting, for {}, removing from calculation".format(api_call_name))
                #clean up temp dict
                del api_calls_temp[api_call_name]

        #calculate average duration        
        for k,v in api_calls.items():
            print("{0}: average = {1:g}".format(k,v[1]/v[0]))