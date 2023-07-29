from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import AboutMe, Education, Experience, PortfolioCategory, Portfolio, Service, Testimonials, Blog, Contact
from .serializers import (
    AboutMeSerializer,
    EducationSerializer,
    ExperienceSerializer,
    PortfolioCategorySerializer,
    PortfolioSerializer,
    ServiceSerializer,
    TestimonialsSerializer,
    BlogSerializer,
    ContactSerializer,
)


class AboutMeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class PortfolioCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PortfolioCategory.objects.all()
    serializer_class = PortfolioCategorySerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TestimonialsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
