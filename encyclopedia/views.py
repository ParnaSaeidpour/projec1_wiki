from django.shortcuts import render
from django.http import HttpResponse

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


def Search_Page(request):

    results = []
    query_searched = request.POST['q']
    entries = util.list_entries()

    for entry in entries:
        if(entry.find(query_searched)==0):
            pass
        else:
            results.append(entry)

    return render(request,"encyclopedia/searchpage.html", {
        "results" : results
    })