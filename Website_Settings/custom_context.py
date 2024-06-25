from Website_Settings.models import Background, Setting


def common_context(request):
    settings = Setting.objects.first()
    return {
        'settings': settings
    }
def image(request):
    backgrounds = Background.objects.last()
    return {
        'backgrounds': backgrounds
    }