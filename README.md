# django-thumbs

This has become a branch off of the original thumbs project adding in South
support and a few other nice improvements. If you are looking for the original
django-thumbs project you can find it on [Google Code][1].

[1]: http://code.google.com/p/django-thumbs/ "django-thumbs on Google Code"


## Requirements

Specific versions are untested but it has been known to work with fairly old
versions of all requirements.

  + Django
  + PIL
  + South


## ImageWithThumbsField Usage

Add an ImageWithThumbsField to your model:

    photo = ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,200),)

To retrieve image URL, exactly the same way as with ImageField:

    my_object.photo.url

To retrieve thumbnails URL's just add the size to it:

    my_object.photo.url_125x125
    my_object.photo.url_300x200


## generate_thumb Parameters

  + img = File object
  + thumb_size = desired thumbnail size, ie: (200,120)
  + format = format of the original image ('jpeg', 'gif', 'png', ...)
