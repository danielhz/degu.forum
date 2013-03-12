# degu.forum

## Introduction

degu.forum provides content types for forums based on Dexterity and in
plone.app.discussion. It is provides tree content types:

- *Forum Folder* contains tematic forums.
- *Forum* represent a forum about a topic.
- *Forum thread* is the start point for a discussion.

## Installing it

Adds this line to your buildout (degu.forum).

Go to ZMI and set a workflow to `Discussion Item (Comment)`. The
workflow `one_state_workflow` could be a good option.
