from random import randint

name = raw_input('Please input your name:')

f = open('game.txt')
lines = f.readlines()
f.close()

scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

num = randint(1, 100)
times = 0
print 'Guess what I think?'
bingo = False
while bingo == False:
    times += 1   # round+1
    answer = input()
    if answer < num:
        print 'Too small!'
    if answer > num:
        print 'Too large!'
    if answer == num:
        print 'BINGO!'
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1

print '%s, you have played %d rounds, guess right answer at minimum %d rounds, average %d rounds' % (
    name, game_times, min_times, avg_times)

# Update results
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = '' #initialize
for n in scores:
    line = n + '' + ''.join(scores[n]) + '\n'
    result += line

f = open('game.txt','w')
f.write(result)
f.close()