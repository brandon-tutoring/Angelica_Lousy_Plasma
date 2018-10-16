new_list = []
def lousy_plasma():
    syn_dict = {"happy":"GLAD", "sad":"BLEAK"}
    quest = input("What would you like to translate?") .strip() .lower()
    quest = quest.split()
    print(syn_dict[1])

    for item in quest:
        if item in syn_dict.values() == True:
              new_list.append(syn_dict[item])
        elif item in syn_dict.values() == False:
              new_list.append(item)
    print(new_list) 
lousy_plasma()
