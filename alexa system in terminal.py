def run_alexa():
    print()  # this print for spacing 1 line :)
    print("HI there, my name is Alexa")
    print("And always call me alexa :)")

    import datetime
    import pywhatkit
    import wikipedia

    use_input = input(":) Hi there my name is Alexa and  i am a virtual robot: ")

    if "alexa" in use_input:
        print("listening....")

        help_input = input("How can i help you?: ")
        if "time" in help_input:
            print("Please wait, Working on it....:)")
            correct_time = datetime.datetime.now().strftime("Time is %I:%M %p And %A")
            print(correct_time)

        elif "play" in help_input:
            song = help_input.replace("play" or "alexa", "")
            print("Please wait, Working on it....:)")
            pywhatkit.playonyt("Playing" + song)

        elif "tell me about" or "Tell me about" in help_input:
            replace_wikipedia = help_input.replace("tell me about" or "Tell me about" or "alexa", "")
            print("Please wait, Working on it....:)")
            sc_wiki = wikipedia.summary(replace_wikipedia, 2)
            print(sc_wiki)

        else:
            print(" Sorry, I don't know about this item :(")
    else:
        print("Please call me alexa")

    ask_user = input("are you continue to talking?(y/n): ")

    if ask_user == "y":
        run_alexa()

    else:
        print("Thank you for talking me, see you next time:)")


run_alexa()