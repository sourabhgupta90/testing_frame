from django.shortcuts import render
from colanderWithType.schema import testColanderSchema, testUpdateColanderSchema
import json
from testing_frame.test_app.report_lab_pdf import pdf


def get_json_data(name):
    file = open(name)
    return json.loads(file.read())


def render_main_page(request):
    links = get_json_data('data/bookmark_links.json')
    sidebar = get_json_data('data/sidebar_links.json')
    return render(request, "main_page.html", {"sidebar_link":sidebar,'links': links})


def sidebar_page(request, offset):
    html = "<html><body>It is now %s.</body></html>" % "23"
    return HttpResponse(html)


def webworker(request):
    return render(request, "webWorker.html")


def colander_test(request):
    testColanderSchema()
    testUpdateColanderSchema()
    return render(request, "schema.html")


def handle_bar_test(request):
    print render(request, "handlebar.html")
    return render(request, "handlebar.html")


def css_test(request):
    return render(request, "css_test.html")


def yui_test(request):
    return render(request, "dashboard.html")


def yui_app(request):
    return render(request, "appTest.html")


def user_timings(request):
    return render(request, "user_timings.html")


def test_report_lab(request):
    pdf_obj = pdf.PdfRenderer()
    pdf_obj.render_pdf()
    return HttpResponse(pdf_obj.get_pdf(request), mimetype='application/pdf')


def angular_dashboard(request):
    return render(request, "angular_dashboard.html")


def test_routing(request):
    print "here"
    return render(request, "angular_dashboard.html")


def get_angular_partial(request, offset):
    return render(request, "angular_dashboard.html")


from django.http import HttpResponse
from django.utils import simplejson
import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#         print offset 
#     except ValueError:
#         raise Http404()

    dt = '' #datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def test_chosen(request):
    html = "<html><body></body></html>"
    return HttpResponse(html)


def fire_ajax(request):
    #print request.GET['title']
    return_dict = {'message': 'bla bla bla','code':324}
    json = simplejson.dumps(return_dict)
    return HttpResponse(json, mimetype="application/x-javascript")


def datasource_template(request):
    return render(request, "datasource.html", {"sidebar_link":"23",'links': "24"})


def datasource_data(request):
    return_dict = {'message': 'bla bla bla','code':324}
    jsondata = simplejson.dumps(return_dict)
    print "here"
    return HttpResponse(jsondata, mimetype="application/json")