#!/usr/bin/env python2
# -*- coding:utf-8 -*-


class JobHook(object):

    def before_job(self):
        raise NotImplementedError("")

    def after_job(self):
        raise NotImplementedError("")

# vim: ts=4 sw=4 sts=4 expandtab
