from django import forms


class ArithmeticOperatorForm(forms.Form):
    arithmetic_operator_form = forms.CharField(
        max_length=2,
        label="Enter operator arithmetic for block C, allowed:"
              " [ '+' which is default ],"
              " '-', '*', '/', "
              "[ '**' which means exponentiation ]\n",
        widget=forms.TextInput(attrs={
            'style': "text-align: center;",
        })
    )
