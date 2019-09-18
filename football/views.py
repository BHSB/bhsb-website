from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PlayerList
from .football_teams import Team_Selector

# Create your views here.
def home_view(request):
    return render(request, "base.html", {})

def football_view(request):
    my_form = PlayerList()
    team_selector = Team_Selector()
    football_list = []
    blue_team = []
    yellow_team = []
    order = ""
    if request.method == "POST":
        my_form = PlayerList(request.POST)
        if my_form.is_valid():
            football_list = my_form.cleaned_data['player_names'].split('\r\n')
            teams, order = team_selector.pick_teams(football_list)
            blue_team = teams[1][1]
            yellow_team = teams[2][1]
        else:
            print(my_form.errors)
    context = {
        "form": my_form,
        "order": order,
        "blue_team": blue_team,
        "yellow_team": yellow_team
    }
    return render(request, "football/football.html", context)
