import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 6) : 
    name,diet,prep_time,cook_time,flavor_profile,course = datalist

    # print intermediate key-value pairs to standard output
    print(diet,"\t",1)