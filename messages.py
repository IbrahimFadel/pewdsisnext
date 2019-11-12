import random

messages = [
    "Day {}, Lol i thought pewdiepie was next @jakepaul ? The sub gap is: {}",
    "Day {}, {}. Do you know what that number is @jakepaul ? That's how many more subscribers pewdiepie has than you",
    "Day {}, {} people prefer pewdiepie's content to yours @jakepaul",
    "Day {}, @jakepaul the population of medium sized nation ({} to be exact) prefer pewdiepie's content over yours",
    "Day {}, out of the 7.8 billion human beings who inhabit this hellhole of an earth, {} prefer Pewdiepie's content to yours, @jakepaul.",
    "Day {}, don't worry @jakepaul, I'm sure you'll catch up. You only have {} more subs to go.",
    "Day {}, I like men. One of those men is Pewdiepie, but not @jakepaul. {} people also agree with me on this.",
    "Day {}, if I could save a certain number of people from this planet, I would save the {} people who prevent @jakepaul from overtaking Pewdiepie.",
    "Day {}, Pewds is next, @jakepaul? Oh really? {} people would beg to differ."
]


def generate_message(diff, last_tweeted_message_index, day):
    num = random.randint(0, len(messages) - 1)
    message = messages[num].format(day, diff)
    if last_tweeted_message_index == num:
        print("rerunning")
        generate_message(diff, last_tweeted_message_index, day)

    return message, num
