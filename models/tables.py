# -*- coding: utf-8 -*-
#db = DAL("sqlite://storage.sqlite")
from datetime import datetime


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

CATEGORY = ['bikes','computers','cars','electronics', 'equipment','household',
               'clothing', 'sporting']

db.define_table('bboard',
                Field('title'),
                Field('name'),
                Field('phone'),
                Field('email'),
                Field('user_id', db.auth_user),
                Field('date_posted', 'datetime'),
                Field('category'),
                Field('bbmessage', 'text'),
                Field('Sold', 'boolean'),
                Field('Price', 'double'),
                Field('image_file', 'upload')
                )

db.bboard.bbmessage.label = 'Description'
db.bboard.name.default = get_first_name()
db.bboard.date_posted.default = datetime.utcnow()
db.bboard.name.writable = False
db.bboard.Sold.default = False
db.bboard.user_id.default = auth.user_id
db.bboard.user_id.writable = db.bboard.user_id.readable = False
db.bboard.date_posted.writable = False
db.bboard.Price.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')
db.bboard.category.requires = IS_IN_SET(CATEGORY)
