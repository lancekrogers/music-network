from django.contrib.auth.decorators import user_passes_test, login_required
from profiles.models import Musician, NonMusician
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

# import login_required user_passes_test
# these functions are made to be passed into user_passes_test


musician_wrapper_func = lambda x: musician_check(x)
non_musician_wrapper_func = lambda x: non_musician_check(x)

def musician_check(x):
    try:
        return Musician.objects.filter(pk=x.pk)
    except ObjectDoesNotExist:
        return redirect('profiles:register_musician')
    except AttributeError:
        return redirect('profiles:register_musician')


def non_musician_check(x):
    try:
        return NonMusician.objects.filter(pk=x.pk)
    except ObjectDoesNotExist:
        return redirect('main:denied')
    except AttributeError:
        return redirect('main:denied')



#def profile_auth(x):



'''
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(redirect_field_name='restaurant_app:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    '''
'''

The above method_decorator setup can be copied and used to require login in
class based views.

        '''