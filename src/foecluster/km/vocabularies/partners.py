# -*- coding: utf-8 -*-

# from plone import api
from foecluster.km import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class Partners(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'ai', _(u'Amnesty International Malaysia')),
            VocabItem(u'article19', _(u'Article 19')),
            VocabItem(u'c4', _(u''' Centre to Combat Corruption and
            Cronyism(C4)''')),
            VocabItem(u'cij', _(u'Centre for Independent Journalism')),
            VocabItem(u'fff', _(u'Freedom Film Network')),
            VocabItem(u'justice_sisters', _(u'Justice for Sisters')),
            VocabItem(u'kryss', _(u'KRYSS Network')),
            VocabItem(u'mcchr', _(u'''
            Malaysian Centre for Constitutionalism and Human Rights
            (MCCHR)''')),
            VocabItem(u'geramm', _(u'Gerakan Media Merdeka')),
            VocabItem(u'sinarproject', _(u'Sinar Project')),
            VocabItem(u'sis', _(u'Sisters in Islam)')),
            VocabItem(u'suaram', _(u'Suara Rakyat Malaysia (SUARAM)')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


PartnersFactory = Partners()
