from django.contrib import admin

from .models import (
        AboutMe, Experience, PortfolioCategory, Portfolio, Service, 
        Testimonials, Blog, Contact, Konikmalar
    )


class KonikmalarInline(admin.StackedInline):
    model = Konikmalar


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [KonikmalarInline]


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


