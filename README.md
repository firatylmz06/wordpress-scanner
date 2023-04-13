Here is an example of its usage:

```
from wordpress_scanner import WordpressScanner


scanner = WordpressScanner(domain)

users = scanner.get_users() 
theme_name = scanner.get_theme_name() 
plugins_name = scanner.get_plugins_name()

print(users)
print(theme_name)
print(plugins_name)

```

This library is a useful tool that can extract the theme name, plugin names, and user name of a WordPress site. It is designed to work with Flask and offers a simple and fast interface for WordPress sites. With the theme name and user name information of a site, you can easily find out which theme and plugins are being used by the site owner. This information can be particularly helpful when analyzing or examining a site.

Using the library is quite easy. After importing the library, all you need to do is enter the WordPress site URL.

The library has been designed to make WordPress site management easier and more efficient for users. I hope this library will help users improve their WordPress site management tasks.


### Changelog


__v1.1[2023-04-13]__
* It worked.

__v0.9[2023-04-12]__
* Pull and fix all plugin names