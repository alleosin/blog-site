import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.filter(status="published").count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status="published").order_by('-publish')[:count]
    return {"latest_posts": latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    all_posts = Post.objects.filter(status="published")
    return all_posts.annotate(total_comments=Count("comments")).order_by("-total_comments")[:count]

@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter
def by_plural(value, variants):
    variants = variants.split(",")
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif value % 10 >= 2 and value % 10 <= 4 and (value % 100 < 10 or value % 100 > 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]
