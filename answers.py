def get_answer(question, answers):
	return answers[question]



question = input('Enter text: ').lower()
answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

print(get_answer(question, answers))

