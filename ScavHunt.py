# need to think of questions

# Macks Treasure : what is "Not the password you are looking for..." : pa55word
# Spam Mack : who is trying to scam Mack Sparrow : mackhack@spammimic.com
# Mackware : where is pt2.exe? : C:\Users\Swashbuckler\Pictures\Camera Roll
# Skull Island : Where does a message get tossed? : volcano
# time is ticking : how much to buy a hint? : 10 coins
# message to the captain : coins, sword, treasure, bottle : ahoy

questions = ['What is "Not the password you are looking for..."?\n',
             "Who is sending spam?\n",
             "Where it pt2.exe?\n",
             "Where does a message get tossed into?\n",
             "How much for a hint?\n",
             "coins, sword, treasure, bottle\n"]
key = ["pa55word",
       "mackhack@spammimic.com",
       "c:\\users\\swashbuckler\\pictures\\camera roll",
       "volcano",
       "10 coins",
       "ahoy"]

print(key[2])
for i in range(len(questions)):
    ans = input(questions[i]).lower()
    if ans == key[i]:
        continue
    else:
        print("That's rough buddy.")
        exit()
