def main():
   step=0
   loop=0
   print("Enter a sequence of non-decreasing numbers.")
   while loop==0:
       num = float(input("Enter num:"))
       if step==0:
           i = num
           step+=1
       else:
            if (num >= i):
                i = num
                step+=1
            else:
                 break
   print ("Thanks for playing!")
   print ("Sequence length: "+str(step)) 
         
if __name__ == "__main__":
    main()