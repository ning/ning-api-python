Overview
========

[ning-api-python](https://github.com/ning/ning-api-python) is a Python client
library for accessing the [Ning API](http://developer.ning.com/).

The Ning API is a RESTful API that allows developers to access the content on
their Ning Networks.


Example Usage
=============


Create Token
------------

Request the access token for the given member using the Ning API

    import oauth2 as oauth
    import ningapi

    consumer = oauth.Consumer(
          key="0d716e57-5ada-4b29-a33c-2f4af1b26837",
          secret="f0963fa5-1259-434f-86fc-8a17d14b16ca"
          )

    host = "external.ningapis.com"
    network = "apiexample"

    ning_api = ningapi.Client(host, network, consumer)


    email = "test@example.com"
    password = "I<3Ning"

    token = ning_api.login(email, password)

    print "Access Key: %s" % token.key
    print "Access Secret: %s" % token.secret


List Photos
-----------

Query the Ning API for the five most recent photos, returning the photo's
title and the URL of the image

    import oauth2 as oauth
    import ningapi

    consumer = oauth.Consumer(
          key="0d716e57-5ada-4b29-a33c-2f4af1b26837",
          secret="f0963fa5-1259-434f-86fc-8a17d14b16ca"
          )
    token = oauth.Token(
          key="07aa5613-6783-4735-b8f1-4c69642ad438",
          secret="e2c528ec-8b81-402c-8f88-8bf17ba8751f"
          )

    host = "external.ningapis.com"
    network = "apiexample"

    ning_api = ningapi.Client(host, network, consumer, token)


    fields = ["title", "image.url"]
    attrs = {
      "fields": ",".join(fields),
      "count": 5
    }

    content = ning_api.get("Photo/recent", attrs)
    for photo in content["entry"]:
      photo_id = photo["id"]
      photo_resource = content["resources"][photo_id]

      print "%s\n\t%s" % (photo["title"], photo_resource["url"])


Create Photo
------------

Upload a photo using the Ning API

    import oauth2 as oauth
    import ningapi

    consumer = oauth.Consumer(
          key="0d716e57-5ada-4b29-a33c-2f4af1b26837",
          secret="f0963fa5-1259-434f-86fc-8a17d14b16ca"
          )
    token = oauth.Token(
          key="07aa5613-6783-4735-b8f1-4c69642ad438",
          secret="e2c528ec-8b81-402c-8f88-8bf17ba8751f"
          )

    host = "external.ningapis.com"
    network = "apiexample"

    ning_api = ningapi.Client(host, network, consumer, token)


    photo_title = "Photo Title"
    photo_desc = "Photo Description"
    photo_path = "/Users/devin/Pictures/nasa/NASA-23.jpg"
    photo_content_type = "image/jpeg"

    photo_fields = {
          "title": photo_title,
          "description": photo_desc,
          "file": photo_path,
          "content_type": photo_content_type
          }

    content = ning_api.post("Photo", photo_fields)

    if content["success"]:
      print "Photo uploaded: %s" % content["id"]


Update a Photo
--------------

Update a photo using the Ning API

    import oauth2 as oauth
    import ningapi

    consumer = oauth.Consumer(
            key="0d716e57-5ada-4b29-a33c-2f4af1b26837",
            secret="f0963fa5-1259-434f-86fc-8a17d14b16ca"
            )
    token = oauth.Token(
            key="07aa5613-6783-4735-b8f1-4c69642ad438",
            secret="e2c528ec-8b81-402c-8f88-8bf17ba8751f"
            )

    host = "external.ningapis.com"
    network = "apiexample"

    ning_api = ningapi.Client(host, network, consumer, token)


    photo_title = "Updated Photo Title"
    photo_desc = "Updated Photo Description"

    photo_fields = {
            "title": photo_title,
            "description": photo_desc,
            "id": "3011345:Photo:3930"
            }

    content = ning_api.put("Photo", photo_fields)

    if content["success"]:
        print "Photo updated"


Delete a Photo
--------------

Delete a photo using the Ning API

    import oauth2 as oauth
    import ningapi

    consumer = oauth.Consumer(
          key="0d716e57-5ada-4b29-a33c-2f4af1b26837",
          secret="f0963fa5-1259-434f-86fc-8a17d14b16ca"
          )
    token = oauth.Token(
          key="07aa5613-6783-4735-b8f1-4c69642ad438",
          secret="e2c528ec-8b81-402c-8f88-8bf17ba8751f"
          )

    host = "external.ningapis.com"
    network = "apiexample"

    ning_api = ningapi.Client(host, network, consumer, token)



    photo_fields = {
          "id": "3011345:Photo:3928"
          }

    content = ning_api.delete("Photo", photo_fields)

    if content["success"]:
      print "Photo deleted"
