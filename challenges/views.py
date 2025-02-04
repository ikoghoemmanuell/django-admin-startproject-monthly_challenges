from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for a month!",
    "february": "Walk for at least 20 minutes a day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Learn Django for at least 20 minutes a day!",
    "may": "Learn Django for at least 20 minutes a day!",
    "june": "Learn Django for at least 20 minutes a day!",
    "july": "Learn Django for at least 20 minutes a day!",
    "august": "Learn Django for at least 20 minutes a day!",
    "september": "Learn Django for at least 20 minutes a day!",
    "october": "Learn Django for at least 20 minutes a day!",
    "november": "Learn Django for at least 20 minutes a day!",
    "december": "Learn Django for at least 20 minutes a day!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    return HttpResponse(list_items)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
