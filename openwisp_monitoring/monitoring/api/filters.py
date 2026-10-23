from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from swapper import load_model
from django_filters.rest_framework import DjangoFilterBackend

Chart = load_model("monitoring", "Chart")


class DashboardQueryFilterSet(filters.FilterSet):
    organization_slug = filters.CharFilter(
        label=_("Organization slug"),
    )
    location_id = filters.CharFilter(label=_("Location ID"))
    floorplan_id = filters.CharFilter(label=_("Floor plan ID"))
    time = filters.CharFilter(label=_("Timeframe"))
    start = filters.CharFilter(label=_("Start"))
    end = filters.CharFilter(label=_("End"))

    class Meta:
        model = Chart
        fields = []


class DashboardQueryFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset
