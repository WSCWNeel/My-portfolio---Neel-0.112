# Defining Greetings and Rules of the Alus game 
def intro():
    name = input ("What's your name?")
    print("Hello", name, "Welcome to this Atlas game")
    print("This Atlas Game asks you about places in the Auckland Dsitrict that start with the ending letter of a prompt word from the auckland district that the computer will give you.")

def rule():
    Rule_1 = print("You have to tell suburb names only in Auckland District") 
    Rule_2 = print("You shouldn't repeat the same suburb name again") 
    Rule_3 = print("You should start the name with the ending letter of the previous word")

def getLives():
    while True:
        lives = input("How many lives do you want to do this game?")
        try:
            lives  >= 0 - int(lives) 
            if lives >= 0:
                return lives
            else:
                print("Please pick a number for this question.")
        except:
            print("Please input a number(The reason you are seeing this message is because you didn't input a number for this question the first time around).")
Starts_with_A = ["Albany","Alfriston","Arch Hill","Auckland CBD","Avondale"]
Starts_with_B = ["Balmoral","Bayswater","Bayview","Beach Haven","Belmont","Birkdale","Birkenhead","Blockhouse Bay","Botany Downs","Botany","Browns Bay","Bucklands Beach","Burswood"]
Starts_with_C = ["Campbells Bay","Castor Bay","Chatswood","Clendon Park","Clover Park","Cockle Bay","Conifer Grove"]
Starts_with_D = ["Dannemora","Devonport","Drury"]
Starts_with_E = ["East Tamaki","East Tamaki Heights","Eastern Beach","Eden Terrace","Eden Valley","Ellerslie","Epsom"]
Starts_with_F = ["Fairview Heights","Farm Cove","Favona","Flat Bush","Forrest Hill","Freemans Bay"]
Starts_with_G = ["Gardens","Glen Eden","Glen Innes","Glendene","Glendowie","Glenfield","Golflands","Goodwood Heights","Grafton","Green Bay","Greenhithe","Greenlane","Grey Lynn"]
Starts_with_H = ["Half Moon Bay","Hauraki","Henderson","Herald Island","Herne Bay","Highbrook","Highland Park","Hillcrest""Hillpark","Hillsborough","Hingaia","Hobsonville","Homai","Howick","Huntington Park"]
Starts_with_K = ["Kaurilands","Kelston","Keri Hill","Kingsland","Kohimarama","Konini"]
Starts_with_L = ["Laingholm","Lincoln","Long Bay","Lucas Heights","Lynfield"]
Starts_with_M = ["Mairangi Bay","Mangere","Mangere Bridge","Mangere East","Manukau","Manurewa","Massey","McLaren Park","Meadowbank","Mechanics Bay","Mellons Bay","Middlemore","Milford","Mission Bay","Mission Heights","Morningside","Mount Albert","Mount Eden","Mount Roskill","Mount Wellington","Murrays Bay"]
Starts_with_N = ["Narrow Neck","New Lynn","New Windsor","Newmarket","Newton","Northcote","Northcross","Northpark"]
Starts_with_O = ["One Tree Hill","Onehunga","Opaheke","Orakei","Oranga","Otahuhu","Otara","Oteha","Owairaka"]
Starts_with_P = ["Pahurehure","Pakuranga","Pakuranga Heights","Panmure","Papakura","Papatoetoe","Parnell","Penrose","Pinehill","Point Chevalier","Point England","Ponsonby"]
Starts_with_R = ["Randwick Park","Ranui","Red Hill","Remuera","Rosebank","Rosedale","Rosehill","Rothesay Bay","Royal Heights","Royal Oak"]
Starts_with_S = ["Saint Heliers","Saint Marys Bay","Sandringham","Schnapper Rock","Shamrock Park","Shelly Park","Somerville","Southdown","St Johns","St Lukes","Stanley Point","Stonefields","Sunnyhills","Sunnynook","Sunnyvale","Swanson"]
Starts_with_T = ["Takanini","Takapuna","Tamaki","Te Atatu Peninsula","Te Atatu South","Te Papapa","Three Kings","Titirangi","Torbay Heights","Torbay","Totara Heights","Totara Vale"]
Starts_with_U = ["Unsworth Heights"]
Starts_with_V = ["Viaduct Harbour"]
Starts_with_W = ["Wai o Taiki Bay","Waiake","Waiata Shores","Waikowhai","Waima","Wairau Valley","Waterview","Wattle Downs","Wesley","West Harbour","Western Heights","Western Springs","Westfield","Westgate","Westmere","Weymouth","Whenuapai","Windsor Park","Wiri","Woodlands Park","Wynyard Quarter"]
# Introduction to the user
intro()
rule()
getLives()
Rules_4 = input("Did you understand the rules of this Atlus game?")
if Rules_4 == "yes":
    print("Let's start the game")
else: 
    print(rule())
    Rules_5 = input("Now, Did you understand the rules of this game?")
    if Rules_5 == "no":
        print(rule())
    else:
        Ask_User = input("Do you want to start the game ?")
# The main games starts from here 
if Ask_User == "yes":
    print("Ok, Please start !")
else: 
    print(Starts_with_A[3])  
