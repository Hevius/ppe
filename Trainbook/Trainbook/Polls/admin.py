from Trainbook.Polls.models import Poll
from Trainbook.Polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    #def was_published_today(self):
    #    return self.pub_date.date() == datetime.date.today()

    #was_published_today.short_description = u'Publi&#232; aujourd\'hui ?'

admin.site.register(Poll, PollAdmin)