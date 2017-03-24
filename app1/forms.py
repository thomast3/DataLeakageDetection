from django import forms

class ChangepwdForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ChangepwdForm, self).__init__(*args, **kwargs)
		self.fields['current'].widget.attrs = {
			'class' : 'form-control',
			'placeholder' : 'Current Password'
		}
		self.fields['new'].widget.attrs = {
			'class' : 'form-control',
			'placeholder' : 'New Password'
		}
		self.fields['reenter'].widget.attrs = {
			'class' : 'form-control',
			'placeholder' : 'Re-enter Password'
		}

	current = forms.CharField(max_length=50, widget=forms.PasswordInput)
	new = forms.CharField(max_length=50, widget=forms.PasswordInput)	
	reenter = forms.CharField(max_length=50, widget=forms.PasswordInput)