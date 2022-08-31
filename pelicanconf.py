AUTHOR = 'Laurie Joslin'
SITENAME = 'Laurie Joslin'
SITEURL = ''

PATH = 'content'
IMAGE_PROCESS = {
    "article-image": ["scale_in 300 300 True"],
    "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
}
TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# Blogroll


DEFAULT_PAGINATION = 10
THEME='brutalist'
## path to favicon
FAVICON = 'IMG_8900-modified.png'
## path to logo for nav menu (optional)
LOGO = 'IMG_8900-modified.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'svbhack'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@lauriejoslin_'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [('about me', '/about-this-blog')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
GITHUB = 'https://github.com/lauriejoslin'
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
## Gravatar
## Commenting mine out so you can see how the theme looks without one
## See https://mamcmanus.com to see what it looks like with a Gravatar
# GRAVATAR = 'https://www.gravatar.com/avatar/a5544bcae63c5d56c0b7a3fa0ab5b295?s=256'
## SITEMAP PLUGIN

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True