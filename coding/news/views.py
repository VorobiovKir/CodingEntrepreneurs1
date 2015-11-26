from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import SignUpForm, ContactForm


# Create your views here.
def home(request):

    if request.user.is_authenticated():
        title = request.user
    else:
        title = 'unknown'

    # if request.method == 'POST':
    #     print request.POST

    # add form
    form = SignUpForm(request.POST or None)

    args = {
        'title': title,
        'form': form
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)

        # print request.POST['email']   NOT RECOMMENDED

        # fullname = form.cleaned_data.get('fullname')
        # if not fullname:
        #     fullname = 'New full name'
        # instance.fullname = fullname

        if not instance.fullname:
            instance.fullname = 'Justin'
        instance.save()
        # print instance
        # print instance.fullname
        # print instance.timestamp
        args['title'] = 'thank you'

    return render(request, 'home.html', args)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        fullname = form.cleaned_data.get('fullname')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        # print fullname, email, message
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'jane_ne_@mail.ru']
        contact_message = '%s: %s via %s' % (fullname, message, email)
        some_html_message = '''
         <h1> Hello world </h1>
         '''
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
            html_message=some_html_message
        )

    args = {
        'form': form,
    }
    return render(request, 'form.html', args)