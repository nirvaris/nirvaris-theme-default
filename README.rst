=====
Nirvaris Blog
=====

A simple Django app to add blog post with comments and meta-tags to your website, using tags for listing.

you add posts and tags via django admin interface and they will be avaliable in your website.

you use it like:

<your-url>/blog/<relative_url> -> return the blog post

<your-url>/blog/<tag>/<tag>... -> return the a list of post whithin these tags.


Quick start
-----------

To install the Blog, use pip from git:

pip install git+https://github.com/nirvaris/nirvaris-blog

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'blog',
    )

2. You have to run makemigrations and migrate, as it uses the db to store the posts, oomments and meta-tags. 

3. Copy the templates on the app's template folder to your application template folders
	These templates are used to render the posts. You should use them for your own style
	
4. you hvae to add the app url to your url file:  url(r'^blog/', include('blog.urls')),