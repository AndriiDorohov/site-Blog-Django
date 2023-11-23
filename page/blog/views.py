# Django modules
from django.contrib import messages
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import DetailView

# Models & Forms from my project
from .models import Article, Comment, Profile, SubscribedUsers
from .decorators import user_is_superuser
from .forms import (
    ArticleForm,
    CommentForm,
    RegistrationForm,
    LoginForm,
    ArticleSearchForm,
    NewsletterForm,
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
)


global_context = {
    "author_name": _("Andrii Dorokhov"),
}


def home_page(request):
    articles = Article.objects.all().order_by("-pubdate")
    context = global_context | {"articles": articles}
    page_number = request.GET.get("page", 1)
    items_per_page = 9
    paginated = Paginator(articles, items_per_page)
    try:
        page = paginated.page(page_number)
    except PageNotAnInteger:
        page = paginated.page(1)
    except EmptyPage:
        page = paginated.page(paginated.num_pages)

    specific_article = Article.objects.first()

    show_pagination = paginated.num_pages == 1
    return render(
        request,
        "home_page.html",
        {
            "page": page,
            "specific_article": specific_article,
            **context,
            "show_pagination": show_pagination,
        },
    )


def about_page(request):
    context = global_context
    return render(request, "about_page.html", context)


def single_post_page(request):
    context = global_context
    return render(request, "single_post_page.html", context)


def pages_page(request):
    context = global_context
    return render(request, "pages_page.html", context)


def contact_page(request):
    context = global_context
    return render(request, "contact_page.html", context)


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()
    article_is_liked = request.user in article.likes.all()
    number_of_likes = article.number_of_likes()
    context = global_context | {
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
        "number_of_likes": number_of_likes,
        "article_is_liked": article_is_liked,
    }
    return render(request, "article_page.html", context)


def category_page(request, category):
    articles = Article.objects.filter(category=category)
    context = global_context | {"articles": articles, "category": category}
    return render(request, "category_page.html", context)

def author_page(request, author_name):
    articles = Article.objects.filter(author_name=author_name).order_by("-pubdate")
    context = global_context | {"articles": articles, "author": author_name}
    page_number = request.GET.get("page", 1)
    items_per_page = 6
    paginated = Paginator(articles, items_per_page)
    try:
        page = paginated.page(page_number)
    except PageNotAnInteger:
        page = paginated.page(1)
    except EmptyPage:
        page = paginated.page(paginated.num_pages)

    specific_article = Article.objects.first()

    show_pagination = paginated.num_pages == 1
    return render(
        request,
        "author_page.html",
        {
            "page": page,
            "specific_article": specific_article,
            **context,
            "show_pagination": show_pagination,
        },
    )

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.author_name = request.user.username
            article.save()
            # article.likes.set([request.user.id])
            messages.success(request, _("Article has been created successfully."))

            return redirect("home_page")
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ArticleForm()

    context = global_context | {"form": form}
    return render(request, "create_article.html", context)


def add_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            Comment.objects.create(article=article, user=request.user, text=text)

    return redirect("article_page", slug=article.slug)


def article_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    return HttpResponseRedirect(reverse("article_page", args=[article.slug]))

def registration(request):
    global_context = {'show_link': False, "page_title": 'User registration form', "page_description": 'Here you can register on the website by entering your name, email address, and password. If the name or email address is already registered, you will be notified. Afterwards, you can create and fill out your profile.'}
    context = {}
    context.update(global_context)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This mailbox is already registered.")
            else:
                user = form.save(commit=False)
                user.save()
                Profile.objects.create(user=user, email=email)
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect("home_page")
    else:
        form = RegistrationForm()
    return render(request, "./partials/registration.html", {"form": form, **context})


def user_login(request):
    global_context = {'show_link': False, "page_title": 'User registration form', "page_description": 'Here you can enter your username and the password you provided during registration.'}
    context = {}
    context.update(global_context)
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
    else:
        form = LoginForm()
    return render(request, "./partials/login.html", {"form": form, **context})


def article_search(request):
    search_form = ArticleSearchForm(request.GET)
    query = request.GET.get("query", "")

    articles = Article.objects.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(full_text__icontains=query))
    context = {
        "search_form": search_form,
        "articles": articles,
    }

    return render(request, "search_results.html", context)

class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        article = get_object_or_404(Article, slug=self.kwargs["slug"])
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        data["total_likes"] = article.total_likes()
        data["article_is_liked"] = liked
        return data

@login_required
def profile(request):
    global_context = {"show_link": False, "page_title": 'User profile edit', "page_description": "This is your profile page. Here you can edit your profile information."}
    user = request.user
    article_count = Article.objects.filter(author=user).count()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if profile:
                p_form.save()
            else:
                new_profile = p_form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'user': user,
        'article_count': article_count,
        'u_form': u_form,
        'p_form': p_form,
    }
    context.update(global_context)

    return render(request, 'partials/profile_edit.html', context)

@login_required
def profile_view(request):
    global_context = {"show_link": True, "page_title": 'User profile', "page_description": "This is your profile page. You can see the progress you've made with your work and manage your projects or assigned tasks"}
    user = request.user
    article_count = Article.objects.filter(author=user).count()

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        messages.info(request, 'You cannot update profile data here.')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'user': user,
        'article_count': article_count,
        'u_form': u_form,
        'p_form': p_form
    }
    context.update(global_context)


    return render(request, 'partials/profile_view.html', context)

@user_is_superuser
def newsletter(request):
    if request.method == "POST":
        subscribers = SubscribedUsers.objects.all()

        subject = request.POST.get("subject")
        email_message = request.POST.get("message")

        for subscriber in subscribers:
            send_mail(
                subject,
                email_message,
                "your@email.com",
                [subscriber.email],
                fail_silently=False,
            )

        messages.success(request, f"Email sent to all subscribers")
        return redirect("/")

    return render(request, "newsletter.html")

def subscribe(request):
    if request.method == "POST":
        return handle_subscription(request)
    return redirect("/")

def handle_subscription(request):
    name = request.POST.get("name", None)
    email = request.POST.get("email", None)

    if not name or not email:
        return handle_invalid_subscription(request)

    if User.objects.filter(email=email).exists():
        return handle_existing_user(request, email)

    subscribe_user = SubscribedUsers.objects.filter(email=email).first()
    if subscribe_user:
        return handle_existing_subscriber(request, email)

    return create_new_subscription(request, name, email)

def handle_invalid_subscription(request):
    messages.error(
        request,
        "You must type a valid name and email to subscribe to the Newsletter",
    )
    return redirect("/")

def handle_existing_user(request, email):
    messages.error(
        request,
        f"Found a registered user with the associated {email} email. You must log in to subscribe or unsubscribe.",
    )
    return redirect(request.META.get("HTTP_REFERER", "/"))

def handle_existing_subscriber(request, email):
    messages.error(request, f"{email} email address is already subscribed.")
    return redirect(request.META.get("HTTP_REFERER", "/"))

def create_new_subscription(request, name, email):
    email_validator = EmailValidator()

    try:
        email_validator(email)
    except ValidationError as e:
        messages.error(request, e.messages[0])
        return redirect("/")

    subscribe_model_instance = SubscribedUsers()
    subscribe_model_instance.name = name
    subscribe_model_instance.email = email
    subscribe_model_instance.save()
    messages.success(
        request, f"{email} email was successfully subscribed to our newsletter!"
    )
    return redirect(request.META.get("HTTP_REFERER", "/"))
