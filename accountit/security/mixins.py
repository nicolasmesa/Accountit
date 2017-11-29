from .utils import company_safe_form


class CompanySafeViewMixin(object):
    """
    Makes any view CompanySafe by adding filter to the query_set for company
    """
    def get_queryset(self):
        query_set = super().get_queryset()

        if not self.request.user.is_authenticated:
            return query_set

        company = self.request.user.company
        return query_set.filter(company=company)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        if not self.request.user.is_authenticated:
            return form

        if form:
            company_safe_form(form, self.request.user.company)

        return form
