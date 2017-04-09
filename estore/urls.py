from django.conf.urls.defaults import *
from estore.content import views
from estore.user_content import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()# for the admin interface

# URL Links relatedd to the admin interface
urlpatterns = patterns('',
    # To enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # To enable the admin interface:
    (r'^admin/', include(admin.site.urls)),
)

# URL link bindings related to the site  Guest user inteface
urlpatterns+=patterns('content.views',
	(r'^(\w+)/main/$','category_page'),	# Link displays the category page
	(r'^(\w+)/search/$','search'),	# Link for the category search 
	(r'^(\w+)/search/(\w+)/$','suggest'),	# Link for recommendation based on a field
	(r'^(\w+)/product/(\w+)/$','product_view'),	# Link for display of product information
	(r'^(\w+)/search/product/(\w+)/$','product_view'),	# Link for display of product information
	(r'^(\w+)/lproduct/(\w+)/$','prdt'),	# Link for displaying recommended product info
	(r'^rate/(\w+)/$','rate'),
	
)

# URL link bindings for the customer interface
urlpatterns+=patterns('user_content.views',
	(r'^$','home'),			# Link for the homepage
	(r'^home/$','home'),		# Link for specific homepage
	(r'login/$','login'),		# Link for the login page
	(r'signup/$','register'),	# Link for the user registration page
	(r'^logout/$','logout_view'),	# Link for logout
	(r'^loggedout/$','success_logout'),	# Link for successful logout
	(r'^(\w+)/addcart/(\w+)/$','addcart'),	# Link for adding products to the cart
	(r'^(\w+)/search/addcart/(\w+)/$','addcart'),	# Link for adding products from a particular section
	(r'viewcart/$','view_cart'),	# Link for displaying user cart
	(r'removecart/(\w+)/$','remove_cart'),	# Link for removing an item from the cart
	(r'checkout/$','checkout'),
	(r'success/$','success_checkout'),
	
)

