from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.

#endpoint for adding a new challenge to a given account
def quest(request, accounts_id, beacon_id):
    # check if acountchallenge row exists

    query = AccountsChallenges.objects.filter(beacon=beacon_id).get(account=accounts_id)
    chal = query.challenge
    state = query.state

    return JsonResponse({str(chal): state})


# endpoint for giving an answer to a quest - ready
def quest_ans(request, accounts_id, beacon_id, answer):

    query = AccountsChallenges.objects.filter(beacon=beacon_id).get(account=accounts_id)
    challenge = query.challenge
    state = query.state

    if state == "Taken":
        currentchallenge = Challenge.objects.get(id=challenge.id)
        if currentchallenge.challengeAnswer == answer:

            # save account
            account = Account.objects.get(id=accounts_id)
            account.points += currentchallenge.reward
            Account.save(account)

            # save state
            query.state = "Completed"
            AccountsChallenges.save(query)

            return JsonResponse({"good["+str(currentchallenge.reward)+"]": account.points})
    elif state == "Completed":
        return JsonResponse({"ErrorCompleted": "You already finished the challenge."})
    else:
        return JsonResponse({"ErrorNotTaken": "You didn't take this challenge and you try to answer it."})

    return JsonResponse({"foo":"bar"})

# endpoint for