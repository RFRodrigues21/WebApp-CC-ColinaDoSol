from django import template

register = template.Library()


@register.filter
def add_css_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})


@register.filter
def hide_field(field):
    return field.as_widget(attrs={'style': 'display: none;'})
@register.filter
def limit_min_value(field, min_value):
    if field.name == 'store_num':
        field.field.widget.attrs['min'] = str(min_value)
    return field