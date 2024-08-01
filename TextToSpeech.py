import pyttsx3
engine=pyttsx3.init()

# FUNCTION abstraction for voice and speed
def sound(voice):
    #CODE FOR VOICE
    if voice=="female":
        voices=engine.getProperty("voices")
        return engine.setProperty("voice",voices[1].id)
    else :
        voices=engine.getProperty("voices")
        return engine.setProperty("voice",voices[0].id)


    #CODE FOR SPEED
def fast(speed):
    if speed==134:
        newVoiceRate=134
        return engine.setProperty('rate',newVoiceRate)
    elif speed==135:
        newVoiceRate=135
        engine.setProperty('rate',newVoiceRate)
    elif speed==136:
        newVoiceRate=136
        engine.setProperty('rate',newVoiceRate)
    elif speed==137 :
        newVoiceRate=137
        engine.setProperty('rate',newVoiceRate)


type=int(input("select your story type:\n1.fairytale\n2.scientific facts\n3.moral\n4.epicpoems\n"))
match type:
    #option 1 fairytale stories
    case 1:
        choice=int(input("enter your choice:\n1.beauty and beast\n2.hansel and gretel\n3.upload your own story:\n"))

        print("please type voice needed")
        voice=input("enter voice you want male or female   ")
        
        speed=int(input("enter speed you want:\n1.134\n2.135\n3.136\n4.137\n NOTE:current  speed is 137 ,type 137 to continue\n"))
        
        #FUNCTION CALLS FOR VOICE AND SPEED
        sound(voice)
        fast(speed)
        
        match choice:
            case 1:    #BEAUTY AND BEST
                text="Beauty and the Beast is a story about a young prince that was cast under a spell. His spell could only be broken with true love. Through many ups and downs, he found love with Beauty, and she, in time, returned his love. They marry and the prince's spell is broken, and they live happily ever after."
                engine.say(text)
            case 2:    #HANSEL AND GRETEL
                text="Hansel and Gretel is about the siblings, Hansel and Gretel, who are abandoned in a forest and fall into the hands of a witch who lives in a gingerbread, cake, and candy house. The evil witch plans to fatten the children before eating them, but Gretel outwits her and kills her."
                engine.say(text)
            case 3:    #upload your code
                text=input("write your story here please  ")
                engine.say(text)

                # EXPLAINING USER ABOUT UPLOADING THEIR OWN CODE
                p=("user instruction,upload your own story is for writing your own story and hearing it")
                engine.say(p)
                newVoiceRate=134
                engine.setProperty('rate',newVoiceRate)
                
                


    case 2: #OPTION 2 SCIENTIFIC FACTS
        choice=int(input("enter your choice:\n1.set-1\n2.set-2\n3.set-3\n"))

        print("please type voice needed")
        voice=input("enter voice you want male or female   ")
        
        speed=int(input("enter speed you want:\n1.134\n2.135\n3.136\n4.137\n NOTE:current  speed is 137 ,type 137 to continue\n"))

        sound(voice)
        fast(speed)

        match choice:
            case 1:     #SET-1
                text="Our planet has more trees compared to stars in the solar system.\nWater can boil & freeze at the same time.\nLights take almost eight minutes to proceed from the sun to earth.\nGrasshoppers have ears in their bellies."
                engine.say(text)
            case 2:     #SET-2
                text="A cockroach has the ability to live for up to one week without its head.\nLizards use their tongue to smell.\nA cloud can as heavy as a million pounds.\nWe can't burp in space.\nMen suffer from colour blindness more than women.\n " 
                engine.say(text)
            case 3:     #SET-3
                text="It is impossible for most people to lick their own elbow. (try it!)'\nA crocodile cannot stick its tongue out.\nA shrimp's heart is in its head.\nIt is physically impossible for pigs to look up into the sky.\nAn ostrich's eye is bigger than its brain.\n"
                engine.say(text)


    case 3: # OPTION 3 MORAL STORIES
        choice=int(input("enter your choice:\n1.rabbit and tortoise\n2.grasshopper and ant\n3.own story \n"))

        print("please type voice needed")
        voice=input("enter voice you want male or female   ")
        
        speed=int(input("enter speed you want:\n 1.134  2.135  3.136  4.137\n NOTE:current  speed is 137 ,type 137 to continue \n"))

        sound(voice)
        fast(speed)
        
        match choice:
            case 1:    #RABBIT AND TORTOISE 
                text="Once upon a time, there was a tortoise who was friends with a rabbit.Out of the blue one day, the rabbit challenged the tortoise to a race. During the race, he looked at the tortoises slow pace and was assured of his easy victory. So, he decided to take a quick nap before he finished the race. When he finally woke up after a long nap, he found that the tortoise had already reached the finish line. Much to his shock and disappointment,he had lost the race while he was busy catching up on his sleep. "
                engine.say(text)
            
            case 2:   #GRASSHOPPER AND ANT
                text="This is a short story for the little ones about a grasshopper that spends its summer singing while the ant works hard to stack food for the upcoming winter. When the winter season arrives, the grasshopper finds itself dying of hunger and begs the ant for food."
                engine.say(text)
            
            case 3:   #CREATE YOUR OWN STORY
                newVoiceRate=134
                engine.setProperty('rate',newVoiceRate)
                
                # EXPLAINING USER ABOUT UPLOADING THEIR OWN CODE
                p=("user instruction,upload your own story is for writing your own story and hearing it")
                engine.say(p)
                
                text=input("write your story   ")
                engine.say(text)
    
    case 4:  # epic poems
        choice=int(input("enter your choice:\n1.The Odyssey by Homer\n2.The Divine Comedy by Dante\n3.Paradise Lost by John Milton \n"))

        print("please type voice needed")
        voice=input("enter voice you want male or female   ")
        
        print("slower voice is recommended (134) for good feel and understanding")
        speed=int(input("enter speed you want:\n 1.134  2.135  3.136  4.137\n NOTE:current  speed is 137 ,type 137 to continue \n"))
        

        sound(voice)
        fast(speed)

        if choice == 1:    #The Odyssey by Homer
            text="The Odyssey is about Odysseus and his return home to Ithaca. See this famous epic in action.Tell me, O muse, of that ingenious hero who travelled far and wide after he had sacked the famous town of Troy. Many cities did he visit, and many were the nations with whose manners and customs he was acquainted; moreover he suffered much by sea while trying to save his own life and bring his men safely home; but do what he might he could not save his men, for they perished through their own sheer folly in eating the cattle of the Sun-god Hyperion; so the god prevented them from ever reaching home. Tell me, too, about all these things, O daughter of Jove, from whatsoever source you may know them."
            engine.say(text)

        elif choice==2:   # The Divine Comedy by Dante
            text="Dante Alighieri wrote a famous epic work that takes you on a journey through hell, purgatory and paradise. Explore an excerpt of The Divine Comedy.In the middle of the journey of our life, I came to myself, in a dark wood, where the direct way was lost. It is a hard thing to speak of, how wild, harsh and impenetrable that wood was, so that thinking of it recreates the fear. It is scarcely less bitter than death: but, in order to tell of the good that I found there, I must tell of the other things I saw there"
            engine.say(text)

        elif choice==3:   #Paradise Lost by John Milton
            text="John Miltons epic poem is written in blank verse and includes two stories about Satan and Adam and Eve. See an excerpt of Miltons epic poem.Of Mans First Disobedience, and the Fruit Of that Forbidden Tree, whose mortal tast Brought Death into the World, and all our woe, With loss of Eden, till one greater Man Restore us, and regain the blissful Seat. "
            engine.say(text)

greet=("Have a good day!")
engine.say(greet)
print("HAVE A GREAT DAY\nUPDATES WILL BE AVAILABLE SOON")



engine.runAndWait()
