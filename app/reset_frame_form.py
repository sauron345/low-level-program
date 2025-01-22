from django import forms


class ResetFrameForm(forms.Form):
    reset_frame_form = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter 13 bytes of reset frame for device B, e.g. 05 00 00 06 78 12 34 56 78 00 00 00 00',
            'rows': 3,
            'cols': 50,
            'style': "resize: none;",
            'oninput': 'auto_spaces_for_line(this)'
        }),
        max_length=50,
        label="",
    )
