from django.shortcuts import render
from django.http import HttpResponse

from . import util

import markdown2
from markdown2 import Markdown
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def Entry_Page(request, page):
    try:

        entry = util.get_entry(page)
        markdowner = Markdown()
        contents = markdowner.convert(entry)

        return render(request, "encyclopedia/EntryPage.html", {
            "title": page,
            "content": contents
        })
    except TypeError:
        return render(request, "encyclopedia/errorpage.html")