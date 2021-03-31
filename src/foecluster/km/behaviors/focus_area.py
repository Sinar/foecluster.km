# -*- coding: utf-8 -*-

from foecluster.km import _
from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IFocusAreaMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IFocusArea(model.Schema):
    """
    """

    directives.widget(partners=SelectFieldWidget)
    partners = schema.List(
        title=u'Focus Areas',
        description=u'FOE Cluster Focus Areas',
        required=False,
        value_type=schema.Choice(
            vocabulary='foecluster.focusareas',
        ),
    )


@implementer(IFocusArea)
@adapter(IFocusAreaMarker)
class FocusArea(object):
    def __init__(self, context):
        self.context = context

    @property
    def focusareas(self):
        if safe_hasattr(self.context, 'focusareas'):
            return self.context.focusareas
        return None

    @focusareas.setter
    def focusareas(self, value):
        self.context.focusareas = value
