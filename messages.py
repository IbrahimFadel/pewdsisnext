import random

messages = [
    "Day {}, Lol i thought pewdiepie was next @jakepaul ? The sub gap is: {}",
    "Day {}, {}. Do you know what that number is @jakepaul ? That's how many more subscribers pewdiepie has than you",
    "Day {}, {} people prefer pewdiepie's content to yours @jakepaul",
    "Day {}, @jakepaul the population of a small nation({} to be exact) prefer pewdiepie's content over yours"
]


def generate_message(diff, last_tweeted_message_index, day):
    num = random.randint(0, len(messages))
    message = messages[num].format(day, diff)
    # print(last_tweeted_message_index, num)
    if last_tweeted_message_index == num:
        print("rerunning")
        generate_message(diff, last_tweeted_message_index, day)
    # print(message)

    return message, num
