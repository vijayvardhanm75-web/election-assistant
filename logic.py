def election_assistant():
    print("👋 Hi! I’m your Election Assistant.")
    print("I’ll help you understand the voting process easily.\n")

    print("Tell me about you:")
    print("1. I’m a first-time voter")
    print("2. I’ve voted before")
    print("3. I just want to learn")

    choice = input("\nEnter 1, 2, or 3: ")

    if choice == "1":
        print("\nGreat! Let’s get you ready to vote 😊")
        print("Here’s what you need to do:")
        print("➡ First, register yourself as a voter")
        print("➡ Check if you meet eligibility criteria")
        print("➡ Find your nearest polling station")
        print("➡ On election day, go and cast your vote")
        print("\n💡 Tip: Don’t forget to carry a valid ID!")

    elif choice == "2":
        print("\nWelcome back! You already know the basics 👍")
        print("Just make sure:")
        print("➡ Your voter ID details are correct")
        print("➡ You know your polling booth location")
        print("➡ You go early to avoid long queues")
        print("\n💡 Tip: Try to vote during non-peak hours")

    else:
        print("\nNice! Let’s explore how elections work 🧠")
        print("➡ Citizens vote to choose their representatives")
        print("➡ Elections happen in phases: registration → voting → results")
        print("➡ Every vote counts in building the government")
        print("\n💡 Tip: Stay updated with official election news")

    print("\nHope this helped! Feel free to come back anytime 🙌")

election_assistant()
