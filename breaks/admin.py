from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from .models import organisations, groups, replacements, dicts, breaks


######################
# ABSTRACT
######################
class BaseOrganisationGroupModelAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('employees',)


class BaseStatusModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


######################
# INLINES
######################
class ReplacementEmployeeInline(admin.TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status', )


######################
# MODELS
######################
@admin.register(organisations.Organisation)
class OrganisationAdmin(BaseOrganisationGroupModelAdmin):
    list_display = ('id', 'name', 'director', )


@admin.register(groups.Group)
class GroupAdmin(BaseOrganisationGroupModelAdmin):
    list_display = ('id', 'name', 'organisation', 'manager', 'min_active', 'replacement_count', )
    autocomplete_fields = ('organisation', )
    list_filter = ('organisation', )
    list_select_related = ('organisation', )

    def get_queryset(self, request):
        return groups.Group.objects.annotate(
            replacement_count=Count('replacements__id')
        )

    def replacement_count(self, obj):
        return obj.replacement_count

    replacement_count.short_description = 'Кол-во смен'


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'group', 'break_start', 'break_end', 'break_max_duration', )
    list_display_links = ('id', 'date', )
    inlines = (ReplacementEmployeeInline, )
    readonly_fields = ('date', )
    autocomplete_fields = ('group', )
    list_select_related = ('group', )
    search_fields = ('date',)


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(BaseStatusModelAdmin):
    pass


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(BaseStatusModelAdmin):
    pass


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement_link', 'employee', 'break_start', 'break_end', 'status', )
    list_filter = ('status', 'replacement', 'break_start', 'break_end', )
    empty_value_display = 'Неизвестно'
    autocomplete_fields = ('replacement', )
    list_select_related = ('replacement', 'employee', )
    radio_fields = {'status': admin.VERTICAL}

    def replacement_link(self, obj):
        link = reverse('admin:breaks_replacement_change', args=[obj.replacement.id])
        return format_html('<a href="{}">{}</a>', link, obj.replacement)

    replacement_link.short_description = 'Ссылка на смену'
