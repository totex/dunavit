from django.db import models

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey


class HomePage(Page):
    hero_title = models.CharField(max_length=255)
    hero_text = models.TextField()
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    mission_title = models.CharField(
        max_length=255,
        default="More About Our Mission",
    )

    mission_body = RichTextField()

    testimonial_quote = models.TextField()
    testimonial_author = models.CharField(max_length=255)

    newsletter_title = models.CharField(
        max_length=255,
        default="Join the Movement",
    )

    newsletter_text = models.TextField(
        default="Stay informed about our latest conservation efforts.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_text"),
        FieldPanel("hero_image"),
        InlinePanel("impact_items", label="Impact items"),
        FieldPanel("mission_title"),
        FieldPanel("mission_body"),
        InlinePanel("work_items", label="Work items"),
        FieldPanel("testimonial_quote"),
        FieldPanel("testimonial_author"),
        FieldPanel("newsletter_title"),
        FieldPanel("newsletter_text"),
    ]


# These are the impact cards that appear on the home page, e.g. "100+ Projects Completed"
class ImpactItem(Orderable):
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="impact_items",
    )

    icon = models.CharField(
        max_length=100,
        help_text="Material Symbols icon name, e.g. landscape",
    )
    value = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    panels = [
        FieldPanel("icon"),
        FieldPanel("value"),
        FieldPanel("description"),
    ]


class WorkItem(Orderable):
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="work_items",
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]