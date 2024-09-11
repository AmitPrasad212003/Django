from django.contrib import admin
from betago.models import chaiVarity,ChaiCertificate,Store,ChaiReviews
# Register your models here.
# from django.contrib import admin
# from .models import chaiVarity

# admin.site.register(chaiVarity)

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2

class ChaivarietyAdmin (admin.ModelAdmin):
    list_display = ('name','image','date_added','type')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number','issued_date','valid_untill')

admin.site.register(chaiVarity,ChaivarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)


