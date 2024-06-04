questions = ["What be my sys time? (HR:MIN:SEC)\n",
             "What be the PID of the game I was playin?\n",
             "When did I first open me music app? (HR:MIN:SEC)\n",
             "What be the build number for netutils.dll\n",
             "What be the full file path of thy writing I had open?(use forward slashes)\n",
             "How many entries be in me diary?\n"]
key = ["19:53:54",
       "3164",
       "19:39:20",
       "3636",
       "C:/Users/MackSparrow/Documents/writings/Diary.txt.txt",
       "12"]

flag = "dfend{Up0n_tH3_H1gH_$e@s}"
print("Arrrrrg maytee, me computer got some sea water in her and crashed during my important writing.")
print("Answer these questions for me and I'll give ye what ye want.")

for i in range(len(questions)):
    ans = input(questions[i])
    if ans == key[i]:
        continue
    else:
        print("ye be wrong")
        exit()
print(flag)
exit()
