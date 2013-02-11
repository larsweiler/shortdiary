from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
import string
import random

class Invite(models.Model):
	generate_code = lambda: ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(20))

	generated_by = models.ForeignKey(User, verbose_name = _('generated by'))
	code = models.CharField(unique = True, default = generate_code, editable = False, max_length = 50, verbose_name = _('code'))
	created_at = models.DateTimeField(auto_now_add = True)

	__unicode__ = lambda self: self.code

	class Meta:
		verbose_name = _('invite')
		verbose_name_plural = _('invites')

class InviteRequest(models.Model):
	email = models.EmailField(unique = True, max_length = 20, verbose_name = _('email'))
	created_at = models.DateTimeField(auto_now_add = True)

	__unicode__ = lambda self: self.email

	class Meta:
		verbose_name = _('invite request')
		verbose_name_plural = _('invite requests')
