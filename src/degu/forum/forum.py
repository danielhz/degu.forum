# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form
from zope.interface import Invalid
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from degu.forum import DeguForumMessageFactory as _

class IForum(form.Schema):
    """A forum.
    """

class View(grok.View):
    """Default view (called "@@view"") for a contact.
    
    The associated template is found in forum_templates/view.pt.
    """
    
    grok.context(IForum)
    grok.require('zope2.View')
    grok.name('view')

class Forum(Container):
    """The object for forums
    """
