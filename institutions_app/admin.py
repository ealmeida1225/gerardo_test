from django.contrib import admin

from institutions_app.models import Institution

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', "address", "nif", "creation_date", ]
    list_display_links = ["pk"]
    list_editable = ['name', "address", "nif"]
    search_fields = ["name"]
    list_per_page = 10

    class Meta:
        model = Institution


admin.site.register(Institution, InstitutionAdmin)
