def main():
   num_stones=20
   i=0
   valid=[1,2]
   determiner=0
   while num_stones>0:
       print("There are "+str(num_stones)+" stones left.")
       if(i%2==0):
          determiner=1
          pick_stones=int(input("Player 1 would you like to remove 1 or 2 stones?"))
          while pick_stones not in valid:
            pick_stones=int(input("Please enter 1 or 2:"))
       else:
          determiner=2
          pick_stones=int(input("Player 2 would you like to remove 1 or 2 stones?")) 
          while pick_stones not in valid:
            pick_stones=int(input("Please enter 1 or 2:"))   
       num_stones=num_stones-pick_stones
       i+=1
       print()
   if determiner==2:
       print("Player 1 wins!")
   else:
       print("Player 2 wins!")
  
if __name__ == '__main__':
    main()