
from .models import Post, Category,SubCategory
from django import forms
import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name","category"]

class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    category = forms.ModelChoiceField(queryset = models.Category.objects.all())
    subcategory = forms.ModelChoiceField(queryset = models.SubCategory.objects.all())
    prev_ref_post = forms.ModelChoiceField(label="Previous Ref Post",queryset = models.Post.objects.all(),required=False)
    next_ref_post = forms.ModelChoiceField(label="Next Ref Post", queryset=models.Post.objects.all(),required=False)
    class Meta:
        model = Post
        fields = ["category","subcategory","title","image","summary_content","content","draft","publish", "tags","prev_ref_post","next_ref_post"
                  ]

    helper= FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-lg-9'
    helper.layout = Layout( "category"
        ,"subcategory",
        "title","image","summary_content","content","draft"
        ,"publish","tags","prev_ref_post","next_ref_post",
        FormActions(
            Submit('publish_post', 'Publish post', css_class="btn-primary")
        )
    )

class MessageForm(forms.Form):
    text_input = forms.CharField()

    textarea = forms.CharField(
        widget = forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget = forms.RadioSelect,
        initial = 'option_two',
    )

    checkboxes = forms.MultipleChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text = "Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-6'
    helper.layout = Layout(
        Field('text_input', css_class='input-sm'),
        Field('textarea', rows="3", css_class='input-xlarge'),
        'radio_buttons',
        Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        AppendedText('appended_text', '.00'),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    )