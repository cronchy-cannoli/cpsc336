while 1 == 1:
    choice = input("Check a Flag? (y/n): ")
    match choice:
        case 'y':
            flag = input("Enter flag to check: ")
            match flag:
                case "dfend{G@mbl1ng_i$_gr3@t}":
                    print("Time is Ticking")
                case "dfend{AAAA-capt-davy-mack}":
                    print("Macks Treasure")
                case "dfend{X_MARKS_THE_SP0T}":
                    print("Message to the Captain")
                case "dfend{y0U_h4vE_pLe4s3d_tHe_paRr0t_goD}":
                    print("Skull Island")
                case _:
                    print("Nuh Uh")
        case 'n':
            print("Exiting...")
            break
        case _:
            print("Please enter y or n")

