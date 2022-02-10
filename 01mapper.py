import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 8) : 
    name,diet,prep_time,cook_time,flavor_profile,course,state,region = datalist

    # print intermediate key-value pairs to standard output
    print(name,"\t",region)