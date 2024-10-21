
for i in range(1,50):
    flag = "false"
    for j in range(2,i):
       if(i%j)==0 :
         flag = "true"
         break;
       else:
         print(i)