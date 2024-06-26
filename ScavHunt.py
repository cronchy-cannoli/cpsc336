# need to think of questions

# mactain hook :

questions = ['What is "Not the password you are looking for..."?\n',  # macks treasure
             "Who is sending spam?\n",  # spam mack
             "Where it pt2.exe?\n",  # mackware
             "Where does a message get tossed into?\n",  # skull island
             "How much for a hint?\n",  # time is ticking
             "coins, sword, treasure, bottle\n",  # message to the captain
             '"nice try ____\n"',  # open sesame
             "wget 192.168.0.2 flag.txt\n",  # ship in a bottle
             "What is the one word password discovered from the clues?\n",  # digging through gifts
             "What user writes in a Diary?\n",  # captains log
             "How much should I rotate the ship?\n",  # message in a bottle
             "What is a birb picture?\n",  # birb
             "Where is Mackintosh found?\n",  # mactain cack
             "Who will ye be walking the plank with?\n",  # mack coords
             "600 miles where?\n",  # x marks the spot
             "Email me about my music at:\n",  # macktain melodies
             "Who is an expert in celestial and terrestrial navigation techniques?\n",  # ye pirate crew
             "????????{xxxxxxxx_xxxxxxx_xxxxxxx____xxxx%s}\n",  # think ur good?
             "How far is m from x?\n",  # gcc
             "x = 0; chill(x < 5) {x += 1;} x = ??\n",  # macklang
             "Check out my youtube!\n",  # phishing 4 gold
             "supersecret?????????????????\n"]  # macktain hook

key = ["pa55word",
       "mackhack@spammimic.com",
       "c:\\users\\swashbuckler\\pictures\\camera roll",
       "volcano",
       "10 coins",
       "ahoy",
       "bozo",
       "dfed{h@h_l0ok_it$_th3_fl@g}",
       "stegcloak",
       "macksparrow",
       "47 degrees",
       "bitmap",
       "rkstorage",
       "de bugs",
       "east",
       "macktain_ita2_melodies@gmail.com",
       "sea witch anne",
       "wompwomp",
       "28289"
       "5"
       "@captainmacksparrow",
       "plaintextpassword"]


for i in range(len(questions)):
    ans = input(questions[i]).lower()
    if ans == key[i]:
        continue
    elif i == 3 and ans == "a volcano":
        continue
    elif i == 11 and ans == "a bitmap":
        continue
    else:
        print("That's rough buddy.")
        exit()
