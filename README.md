# Small accounting platform to practice Django

## Supports
* CRUD for Items
* CRUD for contacts
* Create / View Invoice
* Registration form (creates a user and a company)
* Create user form

## Notes
* This is just a toy project.
* The Invoice doesn't save contact historic data so if the contact is edited, it will appear that way in the invoice as well.
* Only the item and quantity can be specified per item in an invoice and the rest of the information (tax, price) are
handled in the back end.
* I did hack to be able to add multiple items to an invoice using `jQuery`. As a result, the style of the first item is
replicated whenever a new item is added. (no support for delete items).
* I created a `CompanySafeViewMixin` that can be used with the `Views` and will ensure that each queryset takes the
company into account to prevent a user from seeing data from another user. This is just an experiment and may be broken.
* The home page is pretty useless right now.

## TODO
* Get rid of the username and do auth with just email.
* Make the home page better.
* More CSS!
* Use AJAX.
* A lot more!