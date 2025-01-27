from django import forms


class FramesSenderForm(forms.Form):
    frames = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter 13 bytes in line for frame, e.g. 05 00 00 06 78 12 34 56 78 00 00 00 00',
            'rows': 3,
            'cols': 50,
            'style': "resize: none;",
            'oninput': 'auto_spaces_for_frames(this)'
        }),
        label=""
    )
