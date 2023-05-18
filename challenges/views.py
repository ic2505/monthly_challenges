from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no vegetables for the entire month!",
    "may": "Eat no meat for the entire month!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Eat no vegetables for the entire month!",
    "september": "Eat no meat for the entire month!",
    "october": "Walk for at least 20 minutes every day!",
    "november": "Learn Django for at least 20 minutes every day!",
    "december": "Eat no vegetables for the entire month!",
}


def monthly_challenge_by_number(request, month):

    if month > 12:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    redirect_month = list(monthly_challenges.keys())[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
