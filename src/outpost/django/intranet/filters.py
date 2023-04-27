from django.utils.translation import gettext_lazy as _
from django_filters import (
    BooleanFilter,
    CharFilter,
)
from django_filters.rest_framework import (
    filters,
    filterset,
)

from . import models
from .conf import settings


class FunctionFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `name`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `regex`, `iregex`
    """

    category = filters.ChoiceFilter(
        label=_("Category"), choices=models.Function.CATEGORY_CHOICES
    )
    persons = filters.ModelMultipleChoiceFilter(
        label=_("Person"), queryset=models.Person.objects.all()
    )

    class Meta:
        model = models.Function
        fields = {
            "name": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "regex",
                "iregex",
            ),
            "leader": ("exact",),
        }


class OrganizationFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `name`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `regex`, `iregex`
      - `short`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `address`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `email`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `phone`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `url`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
    """

    category = filters.ChoiceFilter(
        label=_("Category"), choices=models.Organization.CATEGORY_CHOICES
    )
    parent = filters.ModelChoiceFilter(
        label=_("Parent"), queryset=models.Organization.objects.all()
    )

    class Meta:
        model = models.Organization
        fields = {
            "name": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "regex",
                "iregex",
            ),
            "short": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "address": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "email": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "phone": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "url": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
        }


class PersonFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `first_name`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `last_name`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `title`: `iexact`, `contains`, `icontains`, `isnull`, `regex`, `iregex`
      - `consultation`: `contains`, `icontains`, `isnull`, `regex`, `iregex`
      - `appendix`: `contains`, `icontains`, `isnull`, `regex`, `iregex`
    """

    sex = filters.ChoiceFilter(label=_("Sex"), choices=models.Person.GENDER_CHOICES)
    functions = filters.ModelMultipleChoiceFilter(
        label=_("Function"), queryset=models.Function.objects.all()
    )

    class Meta:
        model = models.Person
        fields = {
            "first_name": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "last_name": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "title": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "isnull",
                "regex",
                "iregex",
            ),
            "consultation": ("contains", "icontains", "isnull", "regex", "iregex"),
            "appendix": ("contains", "icontains", "isnull", "regex", "iregex"),
        }


class StudentFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `first_name`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `last_name`: `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `isnull`, `regex`, `iregex`
      - `title`: `iexact`, `contains`, `icontains`, `isnull`, `regex`, `iregex`
    """

    class Meta:
        model = models.Student
        fields = {
            "first_name": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "last_name": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
                "isnull",
                "regex",
                "iregex",
            ),
            "title": (
                "exact",
                "iexact",
                "contains",
                "icontains",
                "isnull",
                "regex",
                "iregex",
            ),
        }


class PersonOrganizationFunctionFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>
    """

    class Meta:
        model = models.PersonOrganizationFunction
        fields = ("person", "organization", "function")


class DistributionListFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>
    """

    class Meta:
        model = models.DistributionList
        fields = ("name", "persons")


class CourseGroupTermFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `start`: `exact`, `gt`, `gte`, `lt`, `lte`, `date`
      - `end`: `exact`, `gt`, `gte`, `lt`, `lte`, `date`
    """

    room_title = CharFilter(field_name="room__title")
    room_title__contains = CharFilter(field_name="room__title", lookup_expr="contains")
    room_title__icontains = CharFilter(
        field_name="room__title", lookup_expr="icontains"
    )
    room_title__startswith = CharFilter(
        field_name="room__title", lookup_expr="startswith"
    )
    room_title__istartswith = CharFilter(
        field_name="room__title", lookup_expr="istartswith"
    )
    room_title__endswith = CharFilter(field_name="room__title", lookup_expr="endswith")
    room_title__iendswith = CharFilter(
        field_name="room__title", lookup_expr="iendswith"
    )
    room_number = CharFilter(field_name="room__name_full")
    room_number__contains = CharFilter(
        field_name="room__name_full", lookup_expr="contains"
    )
    room_number__icontains = CharFilter(
        field_name="room__name_full", lookup_expr="icontains"
    )
    room_number__startswith = CharFilter(
        field_name="room__name_full", lookup_expr="startswith"
    )
    room_number__istartswith = CharFilter(
        field_name="room__name_full", lookup_expr="istartswith"
    )
    room_number__endswith = CharFilter(
        field_name="room__name_full", lookup_expr="endswith"
    )
    room_number__iendswith = CharFilter(
        field_name="room__name_full", lookup_expr="iendswith"
    )
    virtual = BooleanFilter(method="filter_virtual")

    class Meta:
        model = models.CourseGroupTerm
        fields = {
            "person": ("exact",),
            "term": ("exact",),
            "room": ("exact",),
            "start": ("exact", "gt", "lt", "gte", "lte", "date"),
            "end": ("exact", "gt", "lt", "gte", "lte", "date"),
            "title": (
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
            ),
            "room__title": (
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
            ),
            "room__name_short": (
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
            ),
            "room__name_full": (
                "contains",
                "icontains",
                "startswith",
                "istartswith",
                "endswith",
                "iendswith",
            ),
        }

    def filter_virtual(self, queryset, name, value):
        kwargs = {"room_id__in": settings.CAMPUSONLINE_VIRTUAL_ROOMS}
        if value:
            return queryset.filter(**kwargs)
        else:
            return queryset.exclude(**kwargs)


class EventFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `building__short`: `exact`, `startswith`, `contains`
      - `room__category__name`: `exact`
      - `room__floor__name`: `exact`
      - `room__building__name`: `exact`, `startswith`
      - `room__building__short`: `exact`
      - `room__building__address`: `exact`, `startswith`, `contains`
      - `room__title`: `exact`, `startswith`, `contains`
      - `room__name_full`: `exact`, `startswith`, `contains`
      - `course__category`: `exact`
      - `category`: `exact`
      - `date`: `gt`, `gte`, `lt`, `lte`
      - `start`: `gt`, `gte`, `lt`, `lte`
      - `end`: `gt`, `gte`, `lt`, `lte`
      - `show_end`: `gt`, `gte`, `lt`, `lte`
    """

    class Meta:
        model = models.Event
        fields = {
            "building__short": ("exact", "startswith", "contains"),
            "room__category__name": ("exact",),
            "room__floor__name": ("exact",),
            "room__building__name": ("exact", "startswith"),
            "room__building__short": ("exact",),
            "room__building__address": ("exact", "contains", "startswith"),
            "room__title": ("exact", "contains", "startswith"),
            "room__name_full": ("exact", "contains", "startswith"),
            "course__category": ("exact",),
            "category": ("exact",),
            "date": ("exact", "gt", "gte", "lt", "lte"),
            "start": ("exact", "gt", "gte", "lt", "lte"),
            "end": ("exact", "gt", "gte", "lt", "lte"),
            "show_end": ("exact", "gt", "gte", "lt", "lte"),
        }


class BulletinFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `academic_year`: `contains`, `regex`
      - `published`: `gte`, `gt`, `lte`, `lt`
    """

    class Meta:
        model = models.Bulletin
        fields = {
            "issue": ("exact",),
            "academic_year": ("exact", "contains", "regex"),
            "published": ("exact", "gt", "lt", "gte", "lte", "date"),
        }


class BulletinPageFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `bulletin`: `gte`, `gt`, `lte`, `lt`
      - `index`: `gte`, `gt`, `lte`, `lt`
    """

    class Meta:
        model = models.BulletinPage
        fields = {
            "bulletin": ("exact", "gt", "lt", "gte", "lte"),
            "index": ("exact", "gt", "lt", "gte", "lte"),
        }


class FinalThesisFilter(filterset.FilterSet):
    """
    ## Filters

    To filter for exact value matches:

        ?<fieldname>=<value>

    For advanced filtering use lookups:

        ?<fieldname>__<lookup>=<value>

    Possible lookups:

      - `year`: `contains`, `regex`
      - `modified`: `gte`, `gt`, `lte`, `lt`, `date`
    """

    class Meta:
        model = models.FinalThesis
        fields = {
            "author": ("exact",),
            "tutor": ("exact",),
            "organization": ("exact",),
            "year": ("exact", "contains", "regex"),
            "modified": ("exact", "gt", "lt", "gte", "lte", "date"),
        }