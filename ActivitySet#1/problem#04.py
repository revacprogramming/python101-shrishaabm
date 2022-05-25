# Conditional Execution

hrs = float(input("Enter hours? "))
rph=float(input("enter rate per hour"))
if(hrs<40):
  gp=rph*hrs
elif(hrs>40):
  gp=(40*rph)+(hrs-40)*rph*1.5

print("gross pay is",gp)