# need to think of questions

# mactain hook :

questions = ['What is "Not the password you are looking for..."?\n',  # macks treasure
             "Who is sending spam?\n",  # spam mack
             "Where it pt2.exe?\n",  # mackware
             "Where does a message get tossed into?\n",  # skull island
             "How much for a hint?\n",  # time is ticking
             "coins, sword, treasure, bottle\n",  # message to the captain
             '"nice try ____"',  # open sesame
             "wget 192.168.0.2 flag.txt",  # ship in a bottle
             "What is the one word password discovered from the clues?",  # digging through gifts
             "What user writes in a Diary?",  # captains log
             "How much should I rotate the ship?",  # message in a bottle
             "What is a birb picture?",  # birb
             "Where is Mackintosh found?",  # mactain cack
             "Who will ye be walking the plank with?",  # mack coords
             "600 miles where?",  # x marks the spot
             "Email me about my music at:",  # macktain melodies
             "Who is an expert in celestial and terrestrial navigation techniques?",  # ye pirate crew
             "????????{xxxxxxxx_xxxxxxx_xxxxxxx____xxxx%s}"  # think ur good?
             "How far is m from x?"  # gcc
             "x = 0; chill(x < 5) {x += 1;} x = ??",  # macklang
             "Check out my youtube!",  # phishing 4 gold
             "supersecret?????????????????"]  # macktain hook

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
       "a bitmap",
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
    else:
        print("That's rough buddy.")
        exit()
