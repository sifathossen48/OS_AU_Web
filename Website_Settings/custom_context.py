from Website_Settings.models import Setting


def common_context(request):
    settings = Setting.objects.first()
    return {
        'settings': settings
    }