from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
CHALLENGES = {
    "january": "Workout Daily for 1.5 hr 🏋🏻",
    "february": "Drink 2L water daily 💧.",
    "march": "Code daily for 2 hours 👨🏻‍💻",
    "april": "Swimming 30 minutes daily 🏊🏻‍♂️",
    "may": "Learn Javascript for 2 hours daily 🖥️",
    "june": "No Meat eating ❌",
    "july": "Start doing meditation for 20 minutes daily 🧘",
    "august": "Walk in nature for 20 minutes 🌴",
    "september": "Run 1km daily 🏃🏻",
    "october": "30 Days no social media 📵",
    "november": "Travel to new city 🏙️",
    "december": "wake up early 🌅",
}


def monthly_challenge_by_number(request, month):
    '''
    Takes month as a number
    '''

    month_list = list(CHALLENGES.keys())
    if month > len(month_list):
        return HttpResponseNotFound("Not Found 🆘")
    month_selected = month_list[month - 1]
    redirected_url = reverse("monthly-challenge", args=[month_selected])
    return HttpResponseRedirect(redirected_url)


def monthly_challenge(request, month):
    '''
    return each month challenge
    '''

    if month in CHALLENGES:
        context = {
            "month": month,
            "challengetext": CHALLENGES[month]
        }
        return render(request,
                      "challenges/monthly-challenge.html",
                      context=context
                      )
    return HttpResponseNotFound("Not Found 🆘")


def show_all_challenges(request):
    '''
    This will show the list of all months
    '''
    str = ''
    for month in CHALLENGES:
        month_path = reverse("monthly-challenge", args=[month])
        str += f'<li><a href="{month_path}">{month}</a></li>'
    response_data = f'<ul>{str}</ul>'
    return HttpResponse(response_data)
