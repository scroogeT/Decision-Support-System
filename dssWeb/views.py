from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from .forms import vrpSolveForm
#from HTMLParser import HTMLParser
from django import forms
import googlemaps
#from .vrpConstrained import *
gmaps = googlemaps.Client(key='AIzaSyDAjpn0_OR1ASmzc4f1y4tJrQE3673_vu8')
# Create your views here.

def login(request):
    return render(request, 'dssWeb/login.html')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'dssWeb/home.html')

"""
#html parser stackoverflow.com/questions/753052
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(self, d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
"""

@login_required(login_url='/login/')
@permission_required('consignment.can_change_consignment')
def vrpSolve(request):

    form_class = vrpSolveForm
    form = form_class(request.POST)
    #base = request.POST['base']
    vehicles = truck.objects.filter(Q(isAllocated=False))
    cons = consignment.objects.filter(Q(isAssigned=False))
    imps = importedOrders.objects.filter(isAssigned=False)
    # allocate base to a static distribution point & demand(weight) to 0
    destinations = [[-17.853883, 30.999545]]
    demands = [0]
        #update destinations & demands(weight) array with all the selected values' cordinates
    for imp in imps:
        lat = imp.lat
        long = imp.long
        demand = imp.weight
        demands.append(demand)
        destinations.append([lat,long])
    print(destinations, demands)

   # directMe = gmaps.directions(origin='-17.853883, 30.999545', destination='-17.853883, 30.999545', waypoints ='kuwadzana,ZW| norton, ZW|chitungwiza,ZW')
    #directMe = gmaps.directions(origin='Harare, zw', destination='Chitungwiza, zw')

    #send destinations & demands to VRPsolver

    #test VRPsolver
    tripNum = 0
    for vehicle in vehicles:
        capacity = 7
        tripNum+=1
        for imp in imps:
            while capacity-imp.weight>=0:
                capacity = capacity - imp.weight
                imp.isAssigned = True
                imp.tripNumber = vehicle.id
                imp.deliveryStatus = deliveryState.objects.get(pk=3)
                vehicle.isAllocated = True
                # save changes
                imp.save()
                vehicle.save()
                print(vehicle, capacity)

            #imps = importedOrders.objects.filter(isAssigned=False)
            print(imps)
        print('outer')




                #cons = request.POST['cons']
    trucks = request.POST['trucks']
    loadTime = request.POST['loadTime']

    print('scheduling truck {}, to consignment {} with Load/Unload time of: {} '.format(trucks,cons,loadTime))

    decoder = dict()

    return routeAllocations(request)

@login_required(login_url='/login/')
@permission_required('consignment.can_add_consignment',login_url='/login/')
def routeAllocations(request):
    #find unassigned vehicles
    vehicles = truck.objects.filter(Q(isAllocated=False))
    #print(vehicles)
    #find unassigned consignments
    cons = consignment.objects.filter(Q(isAssigned=False))
    imports = importedOrders.objects.filter(Q(isAssigned=False))
    #print(cons)
    #find distributionPoint
    bases = distributionPoint.objects.all()
    #print(bases)
    return render(request, 'dssWeb/route_allocations.html',{'vehicles':vehicles, 'bases':bases, 'imports': imports})

@login_required(login_url='/login/')
def dailyRoutes(request):

    #my_distance = gmaps.distance_matrix('harare', 'pretoria')
    #directMe = gmaps.directions(origin ='harare,ZW', destination ='mutare,ZW')
    #print(my_distance)
    #print(directMe)
    #find routes that are closer to each other
    #cluster these making sure the ConsignmentTonnage <= tonnage of the trucks available
    #
    #calculate routes based on the googlemaps distance & directions API
    #######################################################################################
    cons = importedOrders.objects.filter(Q(isAssigned=True))
    print(cons)

    return render(request, 'dssWeb/daily_routes.html',{'cons': cons})

@login_required(login_url='/login/')
def profitability(request):
    #calculate the revenues collected from trips and their costs based on distance travelled
    shippments = importedOrders.objects.filter(Q(isDelivered=True)&Q(isReceived=True))
    revenue = 0.0
    load = 0
    capacity = 0
    trips = shippments.__len__()
    for shippment in shippments:
        revenue=+shippment.charge
        load =+shippment.weight
    if shippments:
        capacity = ((7*trips - load)/load)*100
        print(6/7)

    #and other costs like driver allowance etc
    return render(request, 'dssWeb/profitability_analysis.html',{'revenue':revenue,'load':load, 'trips':trips, 'capacity':capacity})

@login_required(login_url='/login/')
def feesTable(request):
    return render(request, 'dssWeb/fees_table.html')
