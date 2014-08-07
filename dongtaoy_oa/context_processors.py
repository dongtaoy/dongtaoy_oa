
def common(request):
    from dongtaoy_oa.views import side_bar
    return {"path": request.path,
            "sidebars": side_bar(request)}