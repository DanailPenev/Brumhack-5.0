from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create new challenge
def challenge_change(request, beacon_id):
    try:
        chal = Challenge.objects.filter(beacon=beacon_id).get(active=True)
        new_chal = chal.id+1
        chal.active = False
        while True:
            chal_chal = Challenge.objects.get(pk=new_chal)
            if not chal_chal.active and beacon_id == chal_chal.beacon:
                break
            else:
                new_chal += 1
        chal_chal.active = True
        Challenge.save(chal)
        Challenge.save(chal_chal)
        return JsonResponse({"Success": "Successfully changed challenge"})
    except:
        return JsonResponse({"Error": "We suck boyz"})

#endpoint for adding a new challenge to a given account
def challenge_take(request, accounts_id, beacon_id):
    # check if acountchallenge row exists

    query = AccountsChallenges.objects.filter(beacon=beacon_id)
    chal = Challenge.objects.filter(beacon=beacon_id).get(active=True).id
    newchal = Challenge.objects.filter(beacon=beacon_id).get(active=True)
    if query.filter(account=accounts_id):
        pass
    else:
        newobj = AccountsChallenges()
        acc = Account.objects.get(pk=accounts_id)
        newobj.account = acc
        newobj.challenge_id = newchal.id
        newobj.beacon = beacon_id
        newobj.state = "Taken"
        AccountsChallenges.save(newobj)
        print "hui"
        return JsonResponse({"NewChal": newchal.challengeText})


    print AccountsChallenges.objects.filter(beacon=beacon_id).filter(account=accounts_id).filter(challenge=chal)
    if AccountsChallenges.objects.filter(beacon=beacon_id).filter(account=accounts_id).filter(challenge=chal):
        state = AccountsChallenges.objects.filter(beacon=beacon_id).filter(account=accounts_id).get(challenge=chal).state
        if state == "Completed":
            return JsonResponse({"Error": "You have already completed this beacon's challenge for today"})

        elif state == "Taken":
            return JsonResponse({"Error": "Please submit an answer"})

        elif state == "Cancelled":
            return JsonResponse({"Error": "You have already cancelled that challenge"})

    else:
        query = AccountsChallenges.objects.filter(beacon=beacon_id).exclude(state="Completed").exclude(state="Cancelled")
        try:
            query.filter(account=accounts_id).get(state="Taken")
            return JsonResponse({"Error": "You already have a taken challenge from this beacon."})
        except:
            newobj = AccountsChallenges()
            acc = Account.objects.get(pk=accounts_id)
            newobj.account = acc
            newobj.challenge_id = newchal.id
            newobj.beacon = beacon_id
            newobj.state = "Taken"
            AccountsChallenges.save(newobj)
            return JsonResponse({"NewChal": newchal.challengeText})


# endpoint for giving an answer to a quest - ready
def challenge_answer(request, accounts_id, beacon_id, answer):

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

# endpoint for canceling
def challenge_cancel(request, accounts_id, beacon_id):
    try:
        account_challenge = AccountsChallenges.objects.filter(beacon=beacon_id).filter(account=accounts_id).get(state="Taken")
        account_challenge.state = "Cancelled"
        AccountsChallenges.save(account_challenge)
        return JsonResponse({"Success": "Challenge cancelled successfully"})
    except:
        return JsonResponse({"Error": "Can't find a request."})

# endpoint for registering
def register_account(request, username, password):
    try:
        new_account = Account()
        new_account.username = username
        new_account.password = password
        new_account.points = 0
        Account.save(new_account)
        return JsonResponse({"Success": "Successfully registered."})
    except:
        return JsonResponse({"Error": "Could not register."})

# endpoint for registering
def login_account(request, username, password):
    try:
        user = Account.objects.filter(username=username).get(password=password)

        return JsonResponse({"Success": "Successfully logged in."})
    except:

        return JsonResponse({"Error": "Error when logging in."})