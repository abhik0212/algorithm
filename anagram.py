filename="wordlist1.txt"
dct={}
try:
  with open(filename,'r') as fp:
    for line in fp:
      l=list(line)      
      l.sort()
      k="".join(l)
      if dct.has_key(k):
        dct[k].append(line.strip())
      else:
        dct[k]=[line.strip()]
    fp.close() 
except IOError:
  print "no such file"
"""
#output="".join(dct.values())
for lst in dct.values():
        output="".join(lst)
        #f.write(output)
        #f.write('\n')
        print output
"""
try:
    with open("output1.txt",'w') as f:
      for lst in dct.values():
        output=" ".join(lst)
        f.write(output)
        f.write('\n')
        #print output
      f.close()
except:
  print "can't write output"

