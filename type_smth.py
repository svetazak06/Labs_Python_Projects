import random

print("Choose a template:")
print("1 - Hospital Story")
print("2 - Camping Story")
print("3 - Enchanted Castle Letter")

choice = input("Enter the number of the template: ")

if choice == "1":
    number = input("Type a number: ")
    time = input("Type a measure of time: ")
    transportation = input("Type a mode of transportation: ")
    adjective1 = input("Type an adjective: ")
    adjective2 = input("Type another adjective: ")
    noun1 = input("Type a noun: ")
    color = input("Type a color: ")
    body_part1 = input("Type a part of the body: ")
    verb1 = input("Type a verb: ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type another noun: ")
    body_part2 = input("Type another part of the body: ")
    verb2 = input("Type another verb: ")
    noun4 = input("Type another noun: ")
    adjective3 = input("Type another adjective: ")
    silly_word = input("Type a silly word: ")

    print("\nHere is your story:\n")

    print("It was about", number, time, "ago when I arrived at the hospital in a", transportation + ".",
          "The hospital is a/an", adjective1, "place, there are a lot of", adjective2, noun1, "here.",
          "There are nurses here who have", color, body_part1 + ".",
          "If someone wants to come into my room I told them that they have to", verb1, "first.",
          "I’ve decorated my room with", number2, noun2 + ".",
          "Today I talked to a doctor and they were wearing a", noun3, "on their", body_part2 + ".",
          "I heard that all doctors", verb2, noun4, "every day for breakfast.",
          "The most", adjective3, "thing about being in the hospital is the", silly_word, noun1 + "!")

elif choice == "2":
    name = input("Type a person’s name: ")
    noun = input("Type a noun: ")
    feeling1 = input("Type a feeling adjective: ")
    verb1 = input("Type a verb: ")
    feeling2 = input("Type another feeling adjective: ")
    animal1 = input("Type an animal: ")
    verb2 = input("Type another verb: ")
    color1 = input("Type a color: ")
    verb_ing = input("Type a verb ending in 'ing': ")
    adverb = input("Type an adverb ending in 'ly': ")
    number = input("Type a number: ")
    time = input("Type a measure of time: ")
    color2 = input("Type another color: ")
    animal2 = input("Type another animal: ")
    number2 = input("Type another number: ")
    silly_word = input("Type a silly word: ")
    noun2 = input("Type another noun: ")

    print("\nHere is your story:\n")

    print("This weekend I am going camping with", name + ".",
          "I packed my lantern, sleeping bag, and", noun + ".",
          "I am so", feeling1, "to", verb1, "in a tent.",
          "I am", feeling2, "we might see a(n)", animal1 + ", I hear they’re kind of dangerous.",
          "While we’re camping, we are going to hike, fish, and", verb2 + ".",
          "I have heard that the", color1, "lake is great for", verb_ing + ".",
          "Then we will", adverb, "hike through the forest for", number, time + ".",
          "If I see a", color2, animal2, "while hiking, I am going to bring it home as a pet!",
          "At night we will tell", number2, silly_word, "stories and roast", noun2, "around the campfire!!")

elif choice == "3":
    name = input("Type a person’s name: ")
    adjective1 = input("Type an adjective: ")
    color = input("Type a color: ")
    animal = input("Type an animal: ")
    place = input("Type a place: ")
    adjective2 = input("Type another adjective: ")
    creature1 = input("Type a magical creature (plural): ")
    adjective3 = input("Type another adjective: ")
    creature2 = input("Type another magical creature (plural): ")
    room = input("Type a room in a house: ")
    noun1 = input("Type a noun: ")
    noun2 = input("Type another noun: ")
    noun3_plural = input("Type a plural noun: ")
    adjective4 = input("Type another adjective: ")
    noun4_plural = input("Type another plural noun: ")
    number = input("Type a number: ")
    time = input("Type a measure of time: ")
    verb_ing = input("Type a verb ending in 'ing': ")
    adjective5 = input("Type another adjective: ")
    noun5 = input("Type another noun: ")

    print("\nHere is your story:\n")

    print("Dear", name + ",",
          "I am writing to you from a", adjective1, "castle in an enchanted forest.",
          "I found myself here one day after going for a ride on a", color, animal, "in", place + ".",
          "There are", adjective2, creature1, "and", adjective3, creature2, "here!",
          "In the", room, "there is a pool full of", noun1 + ".",
          "I fall asleep each night on a", noun2, "of", noun3_plural,
          "and dream of", adjective4, noun4_plural + ".",
          "It feels as though I have lived here for", number, time + ".",
          "I hope one day you can visit, although the only way to get here now is",
          verb_ing, "on a", adjective5, noun5 + "!!")

else:
    print("Wrong choice!")
