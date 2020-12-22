from django.shortcuts import redirect

def anonymous_required(redirect_url):
    def _wrapped(view_func, *args, **kwargs):
      def check_anonymous(request, *args, **kwargs):
        view = view_func(request, *args, **kwargs)
        if request.user.is_authenticated:
          return redirect(redirect_url)
        return view
      return check_anonymous
    return _wrapped

def superuser_required(redirect_url):
    def _wrapped(view_func, *args, **kwargs):
      def check_superuser(request, *args, **kwargs):
        view = view_func(request, *args, **kwargs)
        if not request.user.is_superuser:
          return redirect(redirect_url)
        return view
      return check_superuser
    return _wrapped

def staff_required(redirect_url):
    def _wrapped(view_func, *args, **kwargs):
      def check_staff(request, *args, **kwargs):
        view = view_func(request, *args, **kwargs)
        if not request.user.is_staff:
          return redirect(redirect_url)
        return view
      return check_staff
    return _wrapped