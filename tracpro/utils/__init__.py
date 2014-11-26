from __future__ import unicode_literals


def get_cacheable_attr(obj, attr_name, callable):
    if hasattr(obj, attr_name):
        return getattr(obj, attr_name)

    calculated = callable()
    setattr(obj, attr_name, calculated)
    return calculated
