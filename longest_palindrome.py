def longest_palindrome(str1):
    l=len(str1)
    table=[[0 for j in xrange(l)] for i in xrange(l)]
    maxlength=1
    startindex=0
    for i in xrange(l):
      table[i][i]=1
    for i in xrange(l-1):
      if str1[i]==str1[i+1]:
        table[i][i+1]=1
        maxlength=2
        startindex=i
    for size in xrange(3,l+1):
        for i in xrange(l-size+1):
            j=i+size-1
            if str1[i]==str1[j] and table[i+1][j-1]==1:
                table[i][j]=1
                maxlength=size
                startindex=i
    print str1[startindex:startindex+maxlength]

s="forgeeksskeegfor"
longest_palindrome(s)
s="abcd"
longest_palindrome(s)

