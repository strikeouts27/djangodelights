apps.py notes
changed the default settings in apps.py to Inventory config and inventory on line 6. 

models.py ntes
the ForeignKey will automatically reference the primary key that Django makes for us.
without the def_str__ method it will not label ingredient by name in the django template

admin: 
superuserpassword: ########
models is looking for a generic python package. when you say .models it says look for models in my directory.
in order to load the admin screen add the /admin to the url to see the admin page.

python filename.py help will show available commands if setup correctly.

# ingredients.html #menu.html
class based views hold objects_list
check the model attributes in models.py for the things to iterate over.
self.name in a class. if I am outside of the class than I use object.name.
variable tags are in double quotes {{}}

must import the views in urls.py be certain to use the views names instead of the model names. I must create a view in views.py. 
And than I need to add in these values to the .html page next. All three steps need to be completed.

For CSS I need to use the load static tag. And I need to use the link tag to the html page to the css sytlesheet.

purchases and revenue.html
I need to be able to grab all of the items that were purchased using the .all() method on the all the purchases in the purchases table. 
#purchases 
this grabs every row in the purchases table

# go to the Receipe Requirements table. give me the objects. but only give me the receipe
#where the recipe is me
