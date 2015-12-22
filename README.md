
#Nirvaris Default Theme

Inspired by PHPs Open Sources, like Wordpress, Drupal, Joomla and Prestashop, where you can build and install Themes, here is a kind of same concept applied to Django websites.

The idea is to have a framework that could be used as a guide line to build diferent styles, using Bootstrap 3, AngularJS and others Browser side things.

The goal is install and uninstall themes to a Django website, changing the look and feel just like that.

We call it the default theme, as we use it as a base to build diferent ones, however, all our apps are built on top of this one, so they will be always comaptible with any app-theme built with the same guide lines.

Everytime we start a new django application, we begin it building the theme. Maybe in the future, it will be so sofisticated as the wordpress ones, where you can setup menus and add some meta data. We will get there. 

It uses the follow dependecies from Nirvaris:

- [Nirvaris Profile](https://github.com/nirvaris/nirvaris-profile)

#Quick start


To install the theme, use pip from git:

```
pip install git+https://github.com/nirvaris/nirvaris-theme-default
```
- Add the app to your INSTALLED_APPS settings

```
    INSTALLED_APPS = (
        ...
        'n_profile'
        'themedefault',
    )
```
- The way to use it is to make every django template like this and add your content in the content block. As it uses Bootstrap and AngularJS, everything is already loaded up. 

```
{% extends "theme-base.html" %}
{% load i18n %}

{% block head_title %}{{ page.title }}{% endblock %}

{% block item-meta-tag %}
{% include 'theme-head-meta-item.html' with item=page %}
{% endblock %}


{% block content %}
<span>This is the default theme</span>
{% endblock %}
```

- Django Forms and messages are styled using theme template tags

```
{% extends "theme-base.html" %}
{% load i18n %}
{% load theme_form_tags %}
{% load theme_messages_tags %}

{% block head_title %}{% trans 'Talk to Us' %}{% endblock %}


{% block content %}

	<div class="row">
		<div class="col-md-3">
		</div>
		<div class="col-md-6">
			<form method="POST" action="#">{% csrf_token %}
				{{ messages|messages_style }}		
				{{ form|form_style }}
				<div class="form-group">
					{# Translators: The submit button on the comments form. #}
					<input class="btn btn-primary btn-lg btn-block" type="submit" value="{% trans 'Send' %}" />
				</div>
			</form>
		</div>
		<div class="col-md-3">
		</div>
	</div>
	
{% endblock %}
```

- The theme also provide a simple image gallery

- If you want to build a new theme, just donwload the sources, rename the app and use this as a template.

We have a plan for making some models where you could add the website name, meta-data, schema for Structure data and few more things that the theme could have at the first place and could be added straight at the admin.