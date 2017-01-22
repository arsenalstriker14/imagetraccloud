# class MyAdaptorEditInline(object):

#     @classmethod
#     def can_edit(cls, adaptor_field):
#         user = adaptor_field.request.user
#         obj = adaptor_field.obj
#         can_edit = False
#         if user.is_anonymous():
#             pass
#         elif user.is_superuser:
#             can_edit = True
#         else:
#            can_edit = has_permission(obj, user, 'edit')
#         return can_edit

class MyAdaptorEditInline(object):

    @classmethod
    def can_edit(cls, adaptor_field):
        can_edit = True
        return can_edit