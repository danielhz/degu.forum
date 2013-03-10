# -*- coding: utf-8 -*-

from five import grok
from zope import schema
from plone.directives import form
from zope.interface import Invalid
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedBlobImage
from plone.dexterity.content import Container
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.textfield import RichText
from degu.forum import DeguForumMessageFactory as _

class IForumFolder(form.Schema):
    """A forum folder.
    """

class View(grok.View):
    """Default view (called "@@view"") for a contact.
    
    The associated template is found in forumfolder_templates/view.pt.
    """
    
    grok.context(IForumFolder)
    grok.require('zope2.View')
    grok.name('view')

class ForumFolder(Container):
    """The object for forum folders
    """
