from django.contrib import admin
from.models import Poll

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display=['id','question','option_one','option_two','option_three','option_one_count','option_two_count','option_three_count']

