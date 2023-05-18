large_avocado = 4225
small_avocado = 4046
jumbo_avocado = 4770

fuji_apple = 4131
red_delicious = 4016
cosmic_crisp = 3507
ambrosia = 6326
cortland = 4106
envy = 3616
gala = 4135
golden_delicious = 4020
granny_smith = 4017
honey_crisp = 3283
jazz = 3293
kiku = 3613
macintosh = 4152
opal_gold = 3618
pink_lady = 4128
sweetie = 3628
kanzi = 3605



main_list = "\n-SEARCH OPTIONS:- \nApples, Avocados, Citrus, Peppers,"

avocado_types = [large_avocado, small_avocado, jumbo_avocado]
avocado_names = "\n-SEARCH OPTIONS:- \nLarge Avocado, Small Avocado, Jumbo Avocado."
apple_types = [fuji_apple, red_delicious, cosmic_crisp, ambrosia, cortland, envy, gala, golden_delicious, granny_smith, honey_crisp, jazz, kiku, macintosh, opal_gold, pink_lady, sweetie, kanzi]
apple_names = "\n-SEARCH OPTIONS:- \nFuji, Red Delicious, Cosmic Crisp, Ambrosia, Cortland, Envy, Gala, \nGolden Delicious, Granny Smith, Honeycrisp, Jazz, Kiku, Macintosh, \nOpal Gold, Pink Lady, Sweetie, Kanzi "

def main():
    while True:
        print(
            "\n-Welcome to the PRODUCE PICKER 3000 App. Press 'q' to Quit.-")
        user = input(">>Enter a type of produce: ")
        if user.lower() == "avocados":
            avocados_search()
            
        
        elif user.lower() == "apples":
            apples_search()
            
        
        if user.lower() == "q":
            print("Goodbye!")
            quit()
            
        if user.lower() == "l":
            print(main_list)
            
        if user.lower() == "h":
            help_section()
            
        else:
            user = input("\nNo product found, press 'enter' to try again...")
            if user == "":
                main()
#-------------------------------------------------------------------------------------------------------
def apples_search():
    while True:
        print("\n-SEARCHING APPLES-")
        user = input(">>Enter the PLU code or the name: ")
        if user.isdigit():
            if user == f"{fuji_apple}":
                apples_fuji()
                
            if user == f"{red_delicious}":
                apples_red_delicious()
                
            elif user == f"{cosmic_crisp}":
                apples_cosmic_crisp()
            
            elif user == f"{ambrosia}":
                apples_ambrosia()
            
            elif user == f"{cortland}":
                apples_cortland()
                
            elif user == f"{envy}":
                apples_envy()
                
            elif user == f"{gala}":
                apples_gala()
        
            elif user == f"{golden_delicious}":
                apples_golden_delicious()
                
            if user == f"{granny_smith}":
                apples_granny_smith()
            
            if user == f"{honey_crisp}":
                apples_honeycrisp()
                
            if user == f"{jazz}":
                apples_jazz()
                
            if user == f"{kiku}":
                apples_kiku()
                
            if user == f"{macintosh}":
                apples_macintosh()
                
            if user == f"{opal_gold}":
                apples_opal_gold()
                
            if user == f"{pink_lady}":
                apples_pink_lady()
                
            if user == f"{sweetie}":
                apples_sweetie()
                
            if user == f"{kanzi}":
                apples_kanzi()
        
        elif user.lower() == "fuji":
            apples_fuji()
        
        if user.lower() == "red delicious":
            apples_red_delicious()
        
        if user.lower() == "cosmic crisp":
            apples_cosmic_crisp()
        
        if user.lower() == "ambrosia":
            apples_ambrosia()
            
        if user.lower() == "envy":
            apples_envy()
            
        if user.lower() == "gala":
            apples_gala()
            
        if user.lower() == "golden delicious":
            apples_golden_delicious()
            
        if user.lower() == "granny smith":
            apples_granny_smith()
            
        if user.lower() == "honeycrisp":
            apples_honeycrisp()
            
        if user.lower() == "jazz":
            apples_jazz()
        
        if user.lower() == "kiku":
            apples_kiku()
            
        if user.lower() == "macintosh":
            apples_macintosh()
            
        if user.lower() == "opal gold":
            apples_opal_gold()
            
        if user.lower() == "pink lady":
            apples_pink_lady()
        
        if user.lower() == "sweetie":
            apples_sweetie()
        
        if user.lower() == "kanzi":
            apples_kanzi()
        
        
        if user.lower() == "b":
            back_button()
            
        if user.lower() == "l":
            print(apple_names)
        
        else:
            user = input("No product found, press 'enter' to try again...")
            if user == "":
                apples_search()

#------------------------------------------------------------------------------------------------------
def avocados_search(): 
    while True:
        print("\n-SEARCHING AVOCADOS-")
        user = input(">>Enter the PLU code or the name: ")
        if user.isdigit():
            if user == f"{large_avocado}":
                avocados_large()
                
            if user == f"{small_avocado}":
                avocados_small()
            
            if user == f"{jumbo_avocado}":
                avocados_jumbo()
                
        if user.lower() == "large":
            avocados_large()
            
        if user.lower() == "small":
            avocados_small()
            
        if user.lower() == "jumbo":
            avocados_jumbo()
            
        if user.lower() == "b":
            back_button()
        
        if user.lower() == "l":
            print(avocado_names)
            
        else:
            user = input("\nNo product found, press 'enter' to try again...")
            if user == "":
                avocados_search()

#APPLE SECTION--------------------------------------------------------------------------------------------------
def apples_fuji():
    print(f"\nFuji Apples PLU {fuji_apple} - Parent Apple: Red Delicious \nGood Sub: Red Delicious, Gala")
    next_search_apples()

def apples_red_delicious():
    print(f"\nRed Delicious PLU {red_delicious} - Parent Apple: None \nGood Sub: Gala, Fuji")
    next_search_apples()
    
def apples_cosmic_crisp():
    print(f"\nCosmic Crisp PLU {cosmic_crisp} - Parent Apple: Honeycrisp & Enterprise \nGood Sub: Honeycrisp, Red Delicious")
    next_search_apples()
    
def apples_ambrosia():
    print(f"\nAmbrosia PLU {ambrosia} - Parent Apple: Golden Delicious & Starking Delicious \nGood Sub: Honeycrisp, Pink Lady")
    next_search_apples()
    
def apples_cortland():
    print(f"\nCortland PLU {cortland} - Parent Apple: None \nGood Sub: Honeycrisp Apple")
    next_search_apples()
    
def apples_envy():
    print(f"\nAmbrosia PLU {envy} - Parent Apple: Braeburn & Royal Gala \nGood Sub: Ambrosia, Pink Lady, Honeycrisp")
    next_search_apples()

def apples_gala():
    print(f"\nGala PLU {gala} - Parent Apple: Golden Delicious & Kidd's Orange Red \n Good Sub: Jazz, Envy, Kanzi")
    next_search_apples()
    
def apples_golden_delicious():
    print(f"\nGolden Delicious PLU {golden_delicious} - Parent Apple: None(Chance Seedling) \nGood Sub: Pink Lady, Fuji")
    next_search_apples()
    
def apples_granny_smith():
    print(f"\nGranny Smith PLU {granny_smith} - Parent Apple:  \nGood Sub: ")
    next_search_apples()
    
def apples_honeycrisp():
    print(f"\nHoneycrisp PLU {honey_crisp} - Parent Apple:  \nGood Sub:")
    next_search_apples()
    
def apples_jazz():
    print(f"\nJazz PLU {jazz} - Parent Apple:  \nGood Sub: ")
    next_search_apples()
    
def apples_kiku():
    print(f"\nKiku PLU {kiku} - Parent Apple:  \nGood Sub: ")
    next_search_apples()
    
def apples_macintosh():
    print(f"\nMacintosh PLU {macintosh} - Parent Apple: \nGood Sub: ")
    next_search_apples()

def apples_opal_gold():
    print(f"\nOpal Gold PLU {opal_gold} - Parent Apple: \nGood Sub: ")
    next_search_apples()
    
def apples_pink_lady():
    print(f"\nPink Lady PLU {pink_lady} - Parent Apple: \nGood Sub: ")
    next_search_apples()

def apples_sweetie():
    print(f"\nSweetie PLU {sweetie} - Parent Apple: \nGood Sub: ")
    next_search_apples()
    
def apples_kanzi():
    print(f"\nKanzi PLU {kanzi} - Parent Apple: \nGood Sub: ")
    next_search_apples()
    
#AVOCADO SECTION--------------------------------------------------------------------------------------------------
def avocados_large():
    print(f"\nLarge Avocados PLU {large_avocado} - Good Sub: Jumbo Avocados or Small Avocados")
    next_search_avocados()
    
def avocados_small():
    print(f"\nSmall Avocados PLU {small_avocado} - Good Sub: Large Avocados")
    next_search_avocados()
    
def avocados_jumbo():
    print(f"\nJumbo Avocados PLU {jumbo_avocado} - Good Sub: Large Avocados")
    next_search_avocados()


#FUNCTIONS--------------------------------------------------------------------------------------------------    
def back_button():
    print("\nGoing back!")
    main()

def next_search_apples():
    user = input("\nPress 'enter' to search again...")
    if user.lower() == "":
        apples_search()
    
def next_search_avocados():
    user = input("\nPress 'enter' to search again...")
    if user.lower() == "":
        avocados_search()
        
def help_section():
    print("\n-HELP-")
    print("Press 'l' for list, 'b' for back, 'q' to quit.")


main()
