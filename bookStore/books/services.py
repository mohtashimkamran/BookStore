def set_property(request, obj):
    if not obj.listed_by:
        obj.listed_by = request.user
    
    return obj