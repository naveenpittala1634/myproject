from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Oba.db_module.db_operations import MysqlDB
from Oba.service.graph_services import order_by_state, top_5_branches, order_by_item_type
from Oba.service.time_selector_widget import RetrieveBasedOnHours

from django.shortcuts import render


def welcome(request):
    r = RetrieveBasedOnHours()
    db_data = r.time_based_data(10000)
    return HttpResponse(db_data)


def welcome1(request):
    return HttpResponse(order_by_state())


def home(request):
    return render(request, "C://Users//naveen//IdeaProjects//myproject//myapp//templates//myapp//home.html")


def data_analysis_view(request):
    return render(request, 'C://Users//naveen//IdeaProjects//myproject//myapp//templates//myapp//DataAnalysis.html')


def feed_in_and_fetch(request):
    return render(request, 'C://Users//naveen//IdeaProjects//myproject//myapp//templates//myapp//FeedAndFetch.html')


def process_form(request):
    if request.method == 'GET':
        query_params = dict(request.GET)
        options = query_params["options[]"]
        if options[0] == "Order by State":
            return HttpResponse(order_by_state())
        elif options[0] == "Order by Item Type":
            return HttpResponse(order_by_item_type())
        elif options[0] == "Top 5 Branches":
            return HttpResponse(top_5_branches())
    return HttpResponse("Fetch Successful!")


def get_data_from_db(request):
    mysqldb = MysqlDB()
    if request.method == 'GET':
        query_params = dict(request.GET)
        options = query_params["userInput"]
        id = options[0]
        my_data = mysqldb.fetch_data_based_on_id(id)
        if my_data:
            print(my_data)
            return render(request,
                          "C://Users//naveen//IdeaProjects//myproject//myapp//templates//myapp//table_data.html",
                          {"my_data": my_data})
        else:
            return HttpResponse(f"No data with customer id {id}")

    return HttpResponse("Fetch Successful!")


def store_data(request):
    mysqldb = MysqlDB()
    if request.method == 'POST':
        query_params = dict(request.POST)
        options = query_params["userInput1"]
        id = options[0]
        mysqldb.insert_into_db(id)
        id = options[0].split(",")[4]
        my_data = mysqldb.fetch_data_based_on_id(id)
        if my_data:
            print(my_data)
            return render(request,
                          "C://Users//naveen//IdeaProjects//myproject//myapp//templates//myapp//table_data.html",
                          {"my_data": my_data})
