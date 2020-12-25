from django import forms
from crispy_forms import bootstrap, layout
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.layout import Layout

from public.models import Publisher,Book,BookCategory

class PublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'

        self.helper.layout = Layout(
        Div(
            Div('Publication Name', css_class="col-sm-2"),
            bootstrap.FormActions(
                layout.Submit('submit', 'Add', css_class='btn btn-primary')),
            css_class='row',
        )
    )
    class Meta:
        model = Publisher
        fields = ('publisher',)

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'

        self.helper.layout = Layout(
        Div(
            Div('Category Name', css_class="col-sm-2"),
            bootstrap.FormActions(
                layout.Submit('submit', 'Add', css_class='btn btn-primary')),
            css_class='row',
        )
    )
    class Meta:
        model = BookCategory
        fields = ('category',)

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'

        self.helper.layout = Layout(
        Div(
            Div('Publication Name', css_class="col-sm-2"),
        ),
        Div(
            Div('Book Name', css_class="col-sm-2"),
        ),
        Div(
            Div('Categoru', css_class="col-sm-2"),
        ),
        Div(
            Div('Jalaram Price', css_class="col-sm-2"),
        ),
        Div(
            Div('Publication Name', css_class="col-sm-2"),
        )
    )   
    class Meta:
        model = Book
        fields = ('book_name','publisher', 'category','jalaram_price','print_price','quantity')