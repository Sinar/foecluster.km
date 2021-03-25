# -*- coding: utf-8 -*-

from foecluster.km import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IPartnersMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IPartners(model.Schema):
    """
    """

    directives.widget(nationalities=SelectFieldWidget)
    partners = schema.List(
            title=u'Partners',
            description=u'Partner(s) contributing to this resource',
            required=False,
            value_type=schema.Choice(
                vocabulary='foecluster.partners',
                ),
            )

@implementer(IPartners)
@adapter(IPartnersMarker)
class Partners(object):
    def __init__(self, context):
        self.context = context

    @property
    def partners(self):
        if safe_hasattr(self.context, 'partners'):
            return self.context.partners
        return None

    @partners.setter
    def partners(self, value):
        self.context.partners = value
