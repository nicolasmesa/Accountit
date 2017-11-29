
def company_safe_form_set(formset, company):
    for form in formset:
        company_safe_form(form, company)


def company_safe_form(form, company):
    fields_dict = form.fields
    fields = fields_dict.values()

    if hasattr(form._meta, 'company_protected_fields'):
        fields = [fields_dict[key] for key in form._meta.company_protected_fields if key in fields_dict]

    for field in fields:
        company_safe_form_field(field, company)


def company_safe_form_field(field, company):
    if hasattr(field, 'queryset'):
        field.queryset = field.queryset.filter(company=company)