
from django.db import models

from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class ProjectIndexPage(Page):
    intro = models.TextField(
        blank=True,
        help_text="Short introduction displayed above the project cards.",
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = ["projects.ProjectPage"]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]


class ProjectPage(Page):
    summary = models.TextField(
        help_text="Short description displayed on the project card.",
    )

    featured_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    body = RichTextField(
        blank=True,
    )

    start_date = models.DateField(
        null=True,
        blank=True,
    )

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    parent_page_types = ["projects.ProjectIndexPage"]

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("featured_image"),
        FieldPanel("body"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
    ]

