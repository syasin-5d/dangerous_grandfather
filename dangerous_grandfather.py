import random

def hogehoge_challenge(challenge_string):
    challenge = list(challenge_string)
    for j in range(0,10):
        print("{0}回目 : ".format(j+1),end='')
        for i in range(0,len(challenge)):
            print(random.choice(challenge),end='')
        print("")
            
def main():
    print("challengeする文字列を入力しよう!")
    while(True):
        challenge_string = input()
        if(challenge_string == ""):
            break
        hogehoge_challenge(challenge_string)
        
        
if __name__ == '__main__':
    main()
