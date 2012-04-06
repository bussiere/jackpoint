from django.contrib import admin
from jackpoint.invitation.models import Invitation,CategorieInvitation,Usage

admin.site.register(Invitation)
admin.site.register(CategorieInvitation)
admin.site.register(Usage)
