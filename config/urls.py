from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views import defaults as default_views
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap
from rest_framework.documentation import include_docs_urls
from fpbase.sitemaps import (
    ProteinSitemap,
    OrganismsSitemap,
    StaticSitemap,
    AuthorsSitemap,
    MicroscopeSitemap,
    ProteinCollectionSitemap,
    ReferencesSitemap,
)

import fpbase.views
from references.views import ReferenceListView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


sitemaps = {
    "static": StaticSitemap(),
    "authors": AuthorsSitemap(),
    "references": ReferencesSitemap(),
    "proteins": ProteinSitemap(),
    "organisms": OrganismsSitemap(),
    "microscopes": MicroscopeSitemap(),
    "collections": ProteinCollectionSitemap(),
}

urlpatterns = [
    url(r"^$", fpbase.views.HomeView.as_view(), name="home"),
    url(
        r"^about/$",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # url(r'^faq/$', TemplateView.as_view(template_name='pages/faq.html'), name='faq'),
    url(
        r"^help/$",
        RedirectView.as_view(url="https://help.fpbase.org", query_string=True),
        name="help",
    ),
    url(r"^cite/$", TemplateView.as_view(template_name="pages/cite.html"), name="cite"),
    url(
        r"^terms/$",
        TemplateView.as_view(template_name="pages/terms.html"),
        name="terms",
    ),
    url(
        r"^privacy/$",
        TemplateView.as_view(template_name="pages/terms.html"),
        name="privacy",
    ),
    url(
        r"^contributing/$",
        TemplateView.as_view(template_name="pages/contributing.html"),
        name="contributing",
    ),
    url(
        r"^schema/$",
        RedirectView.as_view(url="https://help.fpbase.org/schema/schema"),
        name="schema",
    ),
    url(
        r"^bleaching/$",
        TemplateView.as_view(template_name="pages/bleaching.html"),
        name="bleaching",
    ),
    # url(r'^mutations/$', TemplateView.as_view(template_name='pages/mutations.html'), name='mutations'),
    url(
        r"^robots\.txt$",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots",
    ),
    url(
        r"^sitemap\.xml$",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    url(
        r"^googleaecf5301782589e7\.html$",
        TemplateView.as_view(template_name="googleaecf5301782589e7.html"),
        name="verification",
    ),
    url(r"^contact/$", fpbase.views.ContactView.as_view(), name="contact"),
    url(
        r"^thanks/$",
        TemplateView.as_view(template_name="pages/thanks.html"),
        name="thanks",
    ),
    url(r"^beta/$", TemplateView.as_view(template_name="pages/beta.html"), name="beta"),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
    # User management
    url(r"^users/", include("fpbase.users.urls", namespace="users")),
    url(r"^accounts/", include("allauth.urls")),
    url(r"^api/", include("proteins.api.urls", namespace="api")),
    # url(r'^api/$', TemplateView.as_view(template_name='pages/api.html'), name='api'),
    # Your stuff: custom urls includes go here
    # api-auth for DRF
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^api-docs/", include_docs_urls(title="FPbase API docs")),
    # custom apps
    url(r"^", include("proteins.urls")),  # NOTE: without $
    url(r"^reference/", include("references.urls")),  # NOTE: without $
    url(
        r"^references/$",
        cache_page(60 * 30)(ReferenceListView.as_view()),
        name="reference-list",
    ),
    url(r"^fav/", include("favit.urls")),
    url(r"^avatar/", include("avatar.urls")),
    url(r"^test500/", fpbase.views.test500),
    url(r"^graphql/$", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r"^graphql/batch/$", csrf_exempt(GraphQLView.as_view(batch=True))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = "fpbase.views.server_error"

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.

    urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", fpbase.views.server_error),
        url(r"^test/$", fpbase.views.testview),
        url(
            r"^autocomplete/$",
            TemplateView.as_view(template_name="pages/test_autocomplete.html"),
        ),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
