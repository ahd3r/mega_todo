# mega_todo
Before start this app you must to create a virtualenv and in django/contrib/auth/model.py to AbstractUser class add this line:
token_for_confirm=models.CharField(max_length=30, null=True, blank=True)
token_for_reset_password=models.CharField(max_length=30, null=True, blank=True)
