def saved(data):
    if data.GET.get('save', '').strip():
        return True
    else:
        return False
