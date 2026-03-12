from random import randint

print('Quer me foder me beija! ')
act = input('Beijar  [A]\nZoar  [B]\n')
ch = randint(0, 10)
if act in 'Aa' and ch >= 5:
    print('Você a beijou e os dois começaram a se pegar')
elif act in 'Aa' and ch < 5:
    print('Ela te afastou e te deu uma dura pelo ato!')
elif act in 'Bb':
    print('Vocês começaram a zuar...')