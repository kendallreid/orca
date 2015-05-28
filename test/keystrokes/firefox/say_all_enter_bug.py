#!/usr/bin/python

"""Test of sayAll."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Add"))
sequence.append(utils.AssertPresentationAction(
    "1. KP_Add to do a SayAll",
    ["SPEECH OUTPUT: 'Home'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Back to the Gnome Bugzilla home page'",
     "SPEECH OUTPUT: 'Bugzilla'",
     "SPEECH OUTPUT: 'New bug'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '·'",
     "SPEECH OUTPUT: 'Browse'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '·'",
     "SPEECH OUTPUT: 'Search'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '·'",
     "SPEECH OUTPUT: 'Reports'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '·'",
     "SPEECH OUTPUT: 'Account'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '·'",
     "SPEECH OUTPUT: 'Admin'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '·'",
     "SPEECH OUTPUT: 'Help'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Logged In joanmarie.diggs@gmail.com'",
     "SPEECH OUTPUT: '|'",
     "SPEECH OUTPUT: 'Log Out'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Enter Bug: orca \u2013 This page lets you enter a new bug into Bugzilla.'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'Before reporting a bug, please read the'",
     "SPEECH OUTPUT: 'bug writing guidelines'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ', please look at the list of'",
     "SPEECH OUTPUT: 'most frequently reported bugs'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ', and please'",
     "SPEECH OUTPUT: 'search'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'or'",
     "SPEECH OUTPUT: 'browse'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'for the bug.'",
     "SPEECH OUTPUT: 'Reporter:'",
     "SPEECH OUTPUT: 'joanmarie.diggs@gmail.com'",
     "SPEECH OUTPUT: 'Product:'",
     "SPEECH OUTPUT: 'orca'",
     "SPEECH OUTPUT: 'Version:'",
     "SPEECH OUTPUT: '2.21.x '",
     "SPEECH OUTPUT: 'List with 9 items'",
     "SPEECH OUTPUT: 'Component'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ':'",
     "SPEECH OUTPUT: 'braille '",
     "SPEECH OUTPUT: 'List with 5 items'",
     "SPEECH OUTPUT: 'GNOME version'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ':'",
     "SPEECH OUTPUT: 'Unspecified'",
     "SPEECH OUTPUT: 'combo box'",
     "SPEECH OUTPUT: 'OS'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ':'",
     "SPEECH OUTPUT: 'Linux'",
     "SPEECH OUTPUT: 'combo box'",
     "SPEECH OUTPUT: 'Severity'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ':'",
     "SPEECH OUTPUT: 'normal'",
     "SPEECH OUTPUT: 'combo box'",
     "SPEECH OUTPUT: 'Summary:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Description:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Optional Fields'",
     "SPEECH OUTPUT: 'Cc:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Keywords'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ':'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Depends on:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Blocks:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'Commit'",
     "SPEECH OUTPUT: 'push button'",
     "SPEECH OUTPUT: 'Remember values as bookmarkable template'",
     "SPEECH OUTPUT: 'push button'",
     "SPEECH OUTPUT: 'We've made a guess at your operating system.'",
     "SPEECH OUTPUT: 'Please check it and, if we got it wrong, email bugmaster@gnome.org.'",
     "SPEECH OUTPUT: 'Saved Searches:'",
     "SPEECH OUTPUT: 'All Orca'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '|'",
     "SPEECH OUTPUT: 'Firefox'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '|'",
     "SPEECH OUTPUT: 'open orca'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '|'",
     "SPEECH OUTPUT: 'Open RFEs'",
     "SPEECH OUTPUT: 'link'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
