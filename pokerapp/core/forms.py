from django import forms

class ComprobadorPoker(forms.Form):

    opciones = {'1':'2'}

    carta1 = forms.IntegerField(label="", required=True, max_value=12, min_value=1,widget=forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Numero de la Carta 1'}))
    palo1 = forms.ChoiceField(label="", required=True, choices=(("Pica","Pica"),("Corazon","Corazon"),("Trebol","Trebol"),("Diamante","Diamante")), widget=forms.Select(attrs={'class':'form-control mt-3', "placeholder":"Palo 1"}))
    carta2 = forms.IntegerField(label='', required=True, max_value=12, min_value=1,widget=forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Numero de la Carta 2'}))
    palo2 = forms.ChoiceField(label="", required=True, choices=(("Pica","Pica"),("Corazon","Corazon"),("Trebol","Trebol"),("Diamante","Diamante")),widget=forms.Select(attrs={'class':'form-control mt-3', "placeholder":"Palo 2"}))
    carta3 = forms.IntegerField(label='', required=True, max_value=12, min_value=1,widget=forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Numero de la Carta 3'}))
    palo3 = forms.ChoiceField(label="", required=True,  choices=(("Pica","Pica"),("Corazon","Corazon"),("Trebol","Trebol"),("Diamante","Diamante")),widget=forms.Select(attrs={'class':'form-control mt-3', "placeholder":"Palo 3"}))
    carta4 = forms.IntegerField(label='', required=True, max_value=12, min_value=1,widget=forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Numero de la Carta 4'}))
    palo4 = forms.ChoiceField(label="",  required=True, choices=(("Pica","Pica"),("Corazon","Corazon"),("Trebol","Trebol"),("Diamante","Diamante")),widget=forms.Select(attrs={'class':'form-control mt-3', "placeholder":"Palo 4"}))
    carta5 = forms.IntegerField(label='', required=True, max_value=12, min_value=1,widget=forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Numero de la Carta 5'}))
    palo5 = forms.ChoiceField(label="",  required=True, choices=(("Pica","Pica"),("Corazon","Corazon"),("Trebol","Trebol"),("Diamante","Diamante")),widget=forms.Select(attrs={'class':'form-control mt-3', "placeholder":"Palo 5"}))


class NumeroJugadores(forms.Form):
    numero_jugadores = forms.IntegerField(label="Numero de Jugadores", required=True, max_value=10, min_value=1, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numero de Jugadores'}))



