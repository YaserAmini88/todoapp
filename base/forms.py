from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                               #set the attributes for html format
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo', 'aria-label':'Todo', 'aria-describeby': 'add-btn'}))
