# Dipika 2 - Reducer using standard input and output
# Easy to test locally in the terminal

import sys

thisKey = ""
thisValue = ""

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    foodtype, region = datalist

    if foodtype != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = foodtype 
      thisValue = region
  
    # apply the aggregation function
   # thisValue += float(count)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)
