import ast
import sys

#f = open('run_req_map.txt')
f = open('/home/bbirmingham/repos/orbitalivv/cygnus/sims/SIM_CYG_ENV/MONTE_RUN_FSW_failbump_abort/RUN_00030/log_LOG_MONTE.trk')
dict_file = f.read()
# read() adds a newline character...must remove it
dict_file = dict_file.strip('\n')
dict = ast.literal_eval(dict_file)
f.close

# prints key, then indents and prints value...
#   whatever the value is
for key in dict:
    print key
    print '\t', dict[key]


# if the values are lists, for example...
#for key in sorted(dict):
#    print key
#    for val in sorted(dict[key]):
#        print '\t', val



#print '\nBuilding reverse dictionary\n'
# now make a reverse dictionary
#reverse = {}
#for key in dict:
#    for val in dict[key]:
#        # the setdefault command is only executed if the key does NOT exist
#        reverse.setdefault(val,[])
#        reverse[val].append(key)

# print it out in key-sorted order
#for key in sorted(reverse):
#    print key
#    # and sort the values
#    for val in sorted(reverse[key]):
#        print '\t', val

# now print it to a file
#sys.stdout = open("req_to_run_map.txt", "w")
#for key in sorted(reverse):
#    print key
#    for val in sorted(reverse[key]):
#        print '\t', val
