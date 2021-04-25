from django.contrib import admin

from .models import PaymentMethod, PaymentType

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'payment_type', 'down_payment', 'bank_loan', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'payment_type', 'down_payment', 'bank_loan', 'down_payment_description')
    list_per_page = 25

admin.site.register(PaymentMethod, PaymentMethodAdmin)

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_per_page = 25

admin.site.register(PaymentType, PaymentTypeAdmin)
