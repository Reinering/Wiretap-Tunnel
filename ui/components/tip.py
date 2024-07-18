#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner New
email: nbxlc@hotmail.com
"""


from qfluentwidgets import TeachingTip, InfoBarIcon, TeachingTipTailPosition


class Tip():

    @staticmethod
    def info(parent, target, content, title='', isClosable=True, position=TeachingTipTailPosition.BOTTOM,
             duration=2000):
        return Tip.create(
            target=target,
            title=title,
            content=content,
            icon=InfoBarIcon.INFORMATION,
            isClosable=isClosable,
            position=position,
            duration=duration,
            parent=parent
        )

    @staticmethod
    def warning(parent, target, content, title='', isClosable=True, position=TeachingTipTailPosition.BOTTOM,
                duration=2000):
        return Tip.create(
            target=target,
            title=title,
            content=content,
            icon=InfoBarIcon.WARNING,
            isClosable=isClosable,
            position=position,
            duration=duration,
            parent=parent
        )

    @staticmethod
    def error(parent, target, content, title='', isClosable=True, position=TeachingTipTailPosition.BOTTOM,
              duration=2000):
        return Tip.create(
            target=target,
            title=title,
            content=content,
            icon=InfoBarIcon.ERROR,
            isClosable=isClosable,
            position=position,
            duration=duration,
            parent=parent
        )

    @staticmethod
    def success(parent, target, content, title='', isClosable=True, position=TeachingTipTailPosition.BOTTOM,
                duration=2000):
        return Tip.create(
            target=target,
            title=title,
            content=content,
            icon=InfoBarIcon.SUCCESS,
            isClosable=isClosable,
            position=position,
            duration=duration,
            parent=parent
        )

    @staticmethod
    def fail(parent, target, content, title='', isClosable=True, position=TeachingTipTailPosition.BOTTOM,
             duration=2000):
        return Tip.create(
            target=target,
            title=title,
            content=content,
            icon=InfoBarIcon.ERROR,
            isClosable=isClosable,
            position=position,
            duration=duration,
            parent=parent
        )

    @staticmethod
    def create(parent, target, title, content, icon, isClosable, position, duration):
        return TeachingTip.create(
            target=target,
            icon=icon,
            title=title,
            content=content,
            isClosable=isClosable,
            tailPosition=position,
            duration=duration,
            parent=parent
        )