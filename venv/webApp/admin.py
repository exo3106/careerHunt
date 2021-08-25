from django.contrib import admin
from .models import UniversityCatalogue, ProgrammeRequirement,NewsAndUpdates
from import_export.admin import ImportExportModelAdmin
from import_export import resources

@admin.register(UniversityCatalogue,ProgrammeRequirement,NewsAndUpdates)

class UniCatalogueAdmin(ImportExportModelAdmin):
    pass

