# Loop Control Statements: change a loops execution from its normal
#                          sequence
#break: used to terminate the loop entirely
#continue: skips to the next iteration of the loop
#pass: does nothing, acts as a placeholder

#BREAK
while True:
    name=input("Enter your name: ")
    if name != "":
        break

#CONTINUE

phone_numer="0630-682-4418"

for i in phone_numer:
    if i =="-":
        continue
    print(i, end="")

#PASS

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)