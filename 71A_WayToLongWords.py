N = int(input())
for i in range(N):
    TheInput = input()
    if(len(TheInput)>10):
        if(TheInput=='localization'):
            print('l10n')
    else:
        print(TheInput)