from django import template

register = template.Library()


@register.filter
def join_tags(tags):
    return ", ".join(tag.name for tag in tags)
