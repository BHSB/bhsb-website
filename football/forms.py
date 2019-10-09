from django import forms

class PlayerList(forms.Form):
    player_names = forms.CharField(widget=forms.Textarea(
    attrs={"rows": 16,
            "placeholder": "Type one player per line..."
            }))
