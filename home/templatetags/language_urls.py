from django import template
from django.urls import translate_url
from wagtail.models import Locale, Page

register = template.Library()


@register.simple_tag(takes_context=True)
def language_url(context, language_code):
    request = context["request"]
    page = context.get("page")
    locale = Locale.objects.filter(language_code=language_code).first()
    if page is not None and locale is not None and hasattr(page, "get_translation_or_none"):
        translation = page.get_translation_or_none(locale)
        if translation is not None and translation.live:
            return translation.get_url(request)
        # Pages created independently (not via "Translate this page") share no
        # translation key, so match the single same-type page at the same depth
        # under the target language's home page.
        if page.depth > 2:
            target_home = Page.objects.filter(depth=2, locale=locale).first()
            if target_home is not None:
                matches = list(
                    Page.objects.live()
                    .descendant_of(target_home)
                    .filter(depth=page.depth, content_type_id=page.content_type_id)[:2]
                )
                if len(matches) == 1:
                    return matches[0].get_url(request)
    return translate_url(request.get_full_path(), language_code)
