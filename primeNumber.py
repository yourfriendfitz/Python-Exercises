#Is it a Prime Number?

num = int(input("See if your number is a Prime Number: "))

if num > 1:
  for i in range(2,num):
    if(num % i) == 0:
      print(f"{num} is not a Prime Number, Sorry")
      break
  else:
    print(f"Woo! {num} is a Prime Number, way to go!")

else: 
  print(f"{num} is not a Prime Number")