from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from fpbase.decorators import login_required_message_and_redirect as login_required

app_name = "proteins"

urlpatterns = [
    # detail view: /:slug
    url(r"^search/", views.protein_search, name="search"),
    url(r"^blast/", views.blast_view, name="blast"),
    url(
        r"^submit/",
        login_required(
            views.ProteinCreateView.as_view(),
            message="You must be logged in to submit a new protein",
        ),
        name="submit",
    ),
    url(
        r"^protein/(?P<slug>[-\w]+)/update/",
        login_required(
            views.ProteinUpdateView.as_view(),
            message="You must be logged in to update protein information",
        ),
        name="update",
    ),
    url(r"^table/", views.protein_table, name="table"),
    # url(r'^tree/(?P<organism>\d+)/$', views.protein_tree, name='tree'),
    url(
        r"^problems/$",
        TemplateView.as_view(template_name="problems.html"),
        name="problems",
    ),
    url(r"^problems/gaps/$", views.problems_gaps, name="problems-gaps"),
    url(
        r"^problems/inconsistencies/$",
        views.problems_inconsistencies,
        name="problems-inconsistencies",
    ),
    url(
        r"^spectra/submit/$",
        login_required(
            views.SpectrumCreateView.as_view(),
            message="You must be logged in to submit a new spectrum",
        ),
        name="submit-spectra",
    ),
    url(
        r"^spectra/submit/(?P<slug>[-\w]+)/$",
        login_required(
            views.SpectrumCreateView.as_view(),
            message="You must be logged in to submit a new spectrum",
        ),
        name="submit-spectra",
    ),
    url(r"^spectra/(?P<slug>[-\w]+)", views.protein_spectra, name="spectra"),
    url(r"^spectra/$", views.protein_spectra, name="spectra"),
    url(r"^spectra_csv/", views.spectra_csv, name="spectra_csv"),
    url(
        r"^spectra_img/(?P<slug>[-\w]+)(\.(?P<extension>(png)|(svg)|(tif?f)|(pdf)|(jpe?g))?)?$",
        views.spectra_image,
        name="spectra-img",
    ),
    url(
        r"^spectra_url_builder/$",
        TemplateView.as_view(template_name="spectrum_url_form.html"),
        name="spectra-url-builder",
    ),
    url(r"^fret/", views.fret_chart, name="fret"),
    url(r"^compare/$", views.ComparisonView.as_view(), name="compare"),
    url(
        r"^compare/(?P<proteins>[\w,\-]+)/$",
        views.ComparisonView.as_view(),
        name="compare",
    ),
    url(
        r"^lineage/",
        TemplateView.as_view(template_name="lineage.html"),
        name="lineage-list",
    ),
    url(r"^chart/", TemplateView.as_view(template_name="ichart.html"), name="ichart"),
    url(
        r"^collections/(?P<owner>[\w.@+-]+)/?$",
        views.CollectionList.as_view(),
        name="collections",
    ),
    url(r"^collections/", views.CollectionList.as_view(), name="collections"),
    url(
        r"^collection/(?P<pk>\d+)/$",
        views.CollectionDetail.as_view(),
        name="collection-detail",
    ),
    url(
        r"^collection/(?P<pk>\d+)/update/",
        login_required(
            views.CollectionUpdateView.as_view(),
            message="You must be logged in to update collections",
        ),
        name="updatecollection",
    ),
    url(
        r"^collection/(?P<pk>\d+)/delete/",
        login_required(
            views.CollectionDeleteView.as_view(),
            message="You must be logged in to delete collections",
        ),
        name="deletecollection",
    ),
    url(
        r"^collection/create/",
        login_required(
            views.CollectionCreateView.as_view(),
            message="You must be logged in to create a new collection",
        ),
        name="newcollection",
    ),
    url(r"^organisms/$", views.OrganismListView.as_view(), name="organism-list"),
    url(
        r"^organism/(?P<pk>\d+)/$",
        views.OrganismDetailView.as_view(),
        name="organism-detail",
    ),
    url(r"^activity$", views.ActivityView.as_view(), name="activity"),
    url(
        r"^protein/(?P<slug>[-\w]+)/$",
        views.ProteinDetailView.as_view(),
        name="protein-detail",
    ),
    url(
        r"^protein/(?P<slug>[-\w]+)/bleach/$",
        views.protein_bleach_formsets,
        name="protein-bleach-form",
    ),
    url(
        r"^protein/(?P<slug>[-\w]+)/history/$",
        views.protein_history,
        name="protein-history",
    ),
    url(
        r"^bleach_comparison/(?P<pk>[-\w]+)/$",
        views.bleach_comparison,
        name="bleach-comparison",
    ),
    url(r"^bleach_comparison/$", views.bleach_comparison, name="bleach-comparison"),
    url(
        r"^protein/(?P<slug>[-\w]+)/rev/(?P<rev>\d+)$",
        views.ProteinDetailView.as_view(),
        name="protein-detail",
    ),
    url(
        r"^protein/(?P<slug>[-\w]+)/ver/(?P<ver>\d+)$",
        views.ProteinDetailView.as_view(),
        name="protein-detail",
    ),
    url(
        r"^autocomplete-protein/$",
        views.ProteinAutocomplete.as_view(),
        name="protein-autocomplete",
    ),
    url(
        r"^autocomplete-lineage/$",
        views.LineageAutocomplete.as_view(),
        name="lineage-autocomplete",
    ),
    url(
        r"^autocomplete-state/$",
        views.StateAutocomplete.as_view(),
        name="state-autocomplete",
    ),
    url(
        r"^autocomplete-filter/$",
        views.FilterAutocomplete.as_view(),
        name="filter-autocomplete",
    ),
    url(
        r"^microscope/create/",
        login_required(
            views.MicroscopeCreateView.as_view(),
            message="You must be logged in to create a microscope configuration",
        ),
        name="newmicroscope",
    ),
    url(
        r"^microscope/(?P<pk>[-\w]+)/delete/",
        login_required(
            views.MicroscopeDeleteView.as_view(),
            message="You must be logged in to delete microscopes",
        ),
        name="deletemicroscope",
    ),
    url(
        r"^embedscope/(?P<pk>[-\w]+)/$",
        views.MicroscopeEmbedView.as_view(),
        name="microscope-embed",
    ),
    url(
        r"^microscope/(?P<pk>[-\w]+)/report/$",
        views.ScopeReportView.as_view(),
        name="microscope-report",
    ),
    url(
        r"^microscope/(?P<pk>[-\w]+)/$",
        views.MicroscopeDetailView.as_view(),
        name="microscope-detail",
    ),
    url(
        r"^microscope/(?P<pk>[-\w]+)/update/",
        login_required(
            views.MicroscopeUpdateView.as_view(),
            message="You must be logged in to update microscopes",
        ),
        name="updatemicroscope",
    ),
    url(
        r"^microscopes/(?P<owner>[\w.@+-]+)/?$",
        views.MicroscopeList.as_view(),
        name="microscopes",
    ),
    url(r"^microscopes/", views.MicroscopeList.as_view(), name="microscopes"),
    # AJAX
    url(r"^ajax/add_taxonomy/$", views.add_organism, name="add_taxonomy"),
    url(
        r"^ajax/filter_import/(?P<brand>[-\w]+)$",
        views.filter_import,
        name="filter_import",
    ),
    url(
        r"^ajax/add_protein_reference/(?P<slug>[-\w]+)/$",
        views.add_reference,
        name="add_protein_reference",
    ),
    url(
        r"^ajax/add_protein_excerpt/(?P<slug>[-\w]+)/$",
        views.add_protein_excerpt,
        name="add_protein_excerpt",
    ),
    url(
        r"^ajax/admin_approve_protein/(?P<slug>[-\w]+)/$",
        views.approve_protein,
        name="admin_approve_protein",
    ),
    url(
        r"^ajax/admin_revert_version/(?P<ver>\d+)$",
        views.revert_version,
        name="admin_revert_version",
    ),
    url(
        r"^ajax/admin_revert_revision/(?P<rev>\d+)$",
        views.revert_revision,
        name="admin_revert_revision",
    ),
    url(
        r"^ajax/update_transitions/(?P<slug>[-\w]+)/$",
        views.update_transitions,
        name="update_transitions",
    ),
    url(
        r"^ajax/validate_proteinname/$",
        views.validate_proteinname,
        name="validate_proteinname",
    ),
    url(
        r"^ajax/validate_spectrumownername/$",
        views.similar_spectrum_owners,
        name="validate_spectrumownername",
    ),
    url(
        r"^ajax/remove_from_collection/$",
        views.collection_remove,
        name="collection-remove",
    ),
    url(r"^ajax/flag_object/$", views.flag_object, name="flag_object"),
    url(
        r"^ajax/add_to_collection/$", views.add_to_collection, name="add_to_collection"
    ),
    url(r"^ajax/comparison/$", views.update_comparison, name="update-comparison"),
    url(r"^ajax/lineage/(?P<slug>[-\w]+)/$", views.get_lineage, name="get-lineage"),
    url(r"^ajax/lineage/$", views.get_lineage, name="get-lineage"),
    url(
        r"^ajax/org_lineage/(?P<org>[-\w]+)/$",
        views.get_lineage,
        name="get-org-lineage",
    ),
    url(
        r"^microscope/(?P<pk>[-\w]+)/report/json/$",
        views.scope_report_json,
        name="scope_report_json",
    ),
    url(r"^widget/(?P<slug>[-\w]+)/$", views.Widget.as_view(), name="widget-detail"),
]
