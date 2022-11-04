from django.shortcuts import render
from django.utils.translation import gettext_lazy as _, get_language, activate, gettext


def translate(lang):
    current_lang = get_language()
    try:
        activate(lang)
        text = gettext('hello')
    finally:
        activate(current_lang)
    return text


def home(request):
    trans = translate(lang='ja')
    return render(request, 'index.html', {'trans': trans})
