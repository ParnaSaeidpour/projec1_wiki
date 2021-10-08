from django.shortcuts import render

from . import util

import markdown2
from markdown2 import Markdown




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