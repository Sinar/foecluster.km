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
class FocusAreas(object):
    """
    """

    def __call__(self, context):
        # FOE Cluster Focus Areas
        items = [
            VocabItem(u'strengthenmedia', _(u'Strengthening media')),
            VocabItem(u'filmcensorship', _(u'Film censorship')),
            VocabItem(u'roi', _(u'Right to information')),
            VocabItem(u'strenghtenfoe',
                      _(u'Strengthening freedom of expression ')),
            VocabItem(u'internetcensorship',
                      _(u'Internet censorship and digital rights')),
            VocabItem(u'fotcr',
                      _(u'Freedom of thought, conscience, and religion')),
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


FocusAreasFactory = FocusAreas()
