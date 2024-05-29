from os import system, name
from art import logo

print(logo)
print("Welcome to the secret auction program.")

dic_ppl = {}
keep_play = True


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def auction():
    player = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dic_ppl[player] = bid


def winner():
    max_auc = 0
    ppl_winner = ''
    for key in dic_ppl:
        if dic_ppl[key] > max_auc:
            max_auc = dic_ppl[key]
            ppl_winner = key
    print(f"The winner is {ppl_winner} with a bid of ${dic_ppl[ppl_winner]}.")


while keep_play:
    auction()
    response = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if response == 'yes':
        clear()
    else:
        keep_play = False

winner()
