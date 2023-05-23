from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    return render(request, "challenges/index.html", {
            "months": months,
        })


def monthly_challenge_by_number(request, month):

    if month > 12:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    redirect_month = list(monthly_challenges.keys())[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name" : month,
            "text": challenge_text,
        })
    except:
        raise Http404()
