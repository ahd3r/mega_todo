# mega_todo
Before start this app you must to create a virtualenv with all requirements and in django/contrib/auth/model.py to AbstractUser class add this line:
token_for_confirm=models.CharField(max_length=30, null=True, blank=True)
token_for_reset_password=models.CharField(max_length=30, null=True, blank=True)

Email must be real, that's why make validator and then accept by confirm letter. Password must be difficult, that's why you must to show status, how difficulty is your password. Login and signup must be in one page. 

/* Add an adaptation for every page by bootstrap */

Set sendgrid on site 

/* Add a posibility to delete your account */

/* Add a posibility to edit your task as you want by button and delete each taks by button */

Add an error to page which does not exist 

Add gmail api, for registration 

Add a captcha for registration 

Add a cool skrolbar by library 

Include a Muuri lib for sort a task 

Add superplaceholder too 

On page in which you edit your task, add a value for input and bool as default, what you edit 

Don't and a javascripts code, do it app only on python and other todo-app done by javascript 
