from updowngame import Up_Down

sb = Up_Down()

def new_game(d):
	sb.newGame(d)
	return {'code': 'success'}

def guess(d):
	try:
		guess = d.get('guess', [''])[0]
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	answer = sb.guess(guess)
	trials = sb.getGuessCount()

	return {'code': 'success', 'guess': guess, 'answer':answer, 'trials': trials}
