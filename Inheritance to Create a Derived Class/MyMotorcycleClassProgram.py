# This program uses the programmer-defined Motorcycle class.

# Do NOT edit this file. Write your code in Motorcycle.py,
# then open this file and click "Run Code".

from Motorcycle import Motorcycle

motorcycleOne = Motorcycle(90.0, 65.0, True)
motorcycleTwo = Motorcycle(85.0, 60.0, False)

motorcycleOne.accelerate(30.0)
motorcycleTwo.accelerate(20.0)

print("The current speed of motorcycleOne is " + str(motorcycleOne.speed))
print("The current speed of motorcycleTwo is " + str(motorcycleTwo.speed))

if motorcycleOne.sidecar:
   print("This motorcycle has a sidecar")
else:
   print("This motorcycle does not have a sidecar")

if motorcycleTwo.sidecar:
   print("This motorcycle has a sidecar")
else:
   print("This motorcycle does not have a sidecar")
