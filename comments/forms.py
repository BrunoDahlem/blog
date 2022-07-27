from django.forms import ModelForm
from .models import Comments


class FormComment(ModelForm):

    def clean(self):
        data = self.cleaned_data
        name = data.get('comment_name')
        email = data.get('comment_email')
        comment = data.get('comment_description')

        if not name:
            self.add_error(
                'comment_name',
                'Nome é obrigatório'
            )
        if not email:
            self.add_error(
                'comment_email',
                'E-mail é obrigatório'
            )
        if not comment:
            self.add_error(
                'comment_description',
                'Comentário é obrigatório'
            )

    class Meta:
        model = Comments
        fields = ('comment_name', 'comment_email', 'comment_description')
