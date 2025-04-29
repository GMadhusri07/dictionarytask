#  1. Print the list of prime numbers and non prime numbers separately in given list.
num=[1,2,3,4,5,6,7,8,10,9,12,14,122,34,56,73,79,91]
primelist=[]
non_primelist=[]

for number in num:
  factors=0
  for j in range(1,number+1,1):
    if number%j==0:
      factors+=1
  if factors==2:
     primelist.append(number)
  else:
    non_primelist.append(number)
print("The primelist contains:", primelist)
print("The non-primelist contains:", non_primelist)

# ----------------------------------------------------------------------------------------------------------------------

# 2. Count the skills through the dictionary
student1={"name": "Madhusri","role":"FS developer","skills":["FE","BE","cloud","ML", "AI"]}
no_of_skills=len(student1["skills"])
print("No of skills: ", no_of_skills)