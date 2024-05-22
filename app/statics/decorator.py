import functools
from flask import redirect,url_for
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args,**kwargs):
        if view is None:
            return redirect(url_for('auth.login'))
        return view(*args,**kwargs)
    return wrapped_view