from django.shortcuts import render, redirect
from .models import player, Questions

# Create your views here.
def home(rq):
    if rq.method == 'POST':
        ans = rq.POST['answer'].lower()
        cur_player = player.objects.get(user = rq.user)
        cur_question = Questions.objects.get(id = cur_player.current_question_no)
        #if answer is correct
        if ans == cur_question.answer.lower():
            cur_player.score += 1
            cur_player.current_question_no += 1
            cur_player.save()
        # if answer is wrong
        else:
            next_question = Questions.objects.get(id = cur_player.current_question_no)
            param = {'player' : player.objects.all().order_by('-score'), 'question' : next_question, 'msg' : "wrong answer"}
            return render(rq, 'quizapp/home.html', param)

        #after attending all questions
        if cur_player.current_question_no > len(Questions.objects.all()):
            return redirect('/quizapp/final_page')

        next_question = Questions.objects.get(id = cur_player.current_question_no)
        param = {'player' : player.objects.all().order_by('-score'), 'question' : next_question}
        return render(rq, 'quizapp/home.html', param)
        

    if player.objects.filter(user = rq.user).exists() == False:
        new_player = player(user = rq.user)
        new_player.save()

    
    cur_player = player.objects.get(user = rq.user)

    if cur_player.current_question_no > len(Questions.objects.all()):
            return redirect('/quizapp/final_page')

    cur_question = Questions.objects.get(id = cur_player.current_question_no)
    print(cur_question)

    param = {'player' : player.objects.all(), 'question' : cur_question}
    return render(rq, 'quizapp/home.html', param)

def final_page(rq):
    param = {'player' : player.objects.all().order_by('-score')}
    return render(rq, 'quizapp/final_page.html', param)

def leaderboard(rq):
    param = {'player' : player.objects.all().order_by('-score')}
    return render(rq, 'quizapp/leaderboard.html', param)