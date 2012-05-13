from django.contrib import admin
from invitation.models import Invitation,CategorieInvitation,Usage,InvitationUsed

admin.site.register(Invitation)
admin.site.register(InvitationUsed)
admin.site.register(CategorieInvitation)
admin.site.register(Usage)
