import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import TemplateSyntaxError
from django.db.models import Q
from django.contrib import messages
from .models import TOS
from .models import Edit
from .models import Element
from .models import ElementText
from .algo import *
from django.contrib.auth.decorators import login_required
from .forms import TOSForm, UserRegisterForm, UserUpdateForm, EditFormSet, EditForm, CompareForm, RankingForm
# Create your views here.

def home(request):
    return render(request, 'HomeScreen/index.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your information has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'HomeScreen/profile.html', context)

def compare(request):
    if request.method == 'POST':
        c_form = CompareForm(request.POST)
        if c_form.is_valid():
            tosDict = c_form.cleaned_data['selected_toses']
		
	    #check to see if multiple TOSs were chosen, message if not
            if(len(tosDict) < 2):
                messages.warning(request, 'Please choose more than one TOS to compare.')
                return redirect('Compare')
            else:
                tosList = list(tosDict)
                tosObjects = TOS.objects.all().filter(name__in=tosList)
                elements = Element.objects.all().order_by('category', 'weight')
                allText = []
                for t in tosList:
                    e = (ElementText.objects.filter(tos = t).values_list('element_id', flat = True))
                    allText.append(e)
                context = {'tosObjects': tosObjects, 'elements': elements, 'allText': allText}
        else:
            c_form = CompareForm()
            context = {'c_form': c_form}
    else:
        c_form = CompareForm()
        context = {'c_form': c_form}
    return render(request, 'HomeScreen/Compare.html', context)
        

def register(request):
    if request.method == 'POST':
        r_form = UserRegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            username = r_form.cleaned_data.get('username')
            messages.success(
                request, "Your account has been created. You may now log in!")
            return redirect('login')
    else:
        r_form = UserRegisterForm()
    return render(request, 'HomeScreen/register.html', {'r_form': r_form})

def search_for_tos(request):
   # if user is searching for a TOS
    if request.GET.get('Search-ToS-Name'):
        search_term = request.GET.get('Search-ToS-Name') if request.GET.get('Search-ToS-Name') != None else ''
        # get results of query from database
        search_results = TOS.objects.filter(Q(name__icontains=search_term), Q(status = 'Approved'))
        if not search_results:
            messages.warning(request, "TOS does not exist.")
    else:
        search_results = None


    TOSs = TOS.objects.filter(Q(status = 'Approved'))
    categories = ['Social Media', 'Streaming', 'News', 'Shopping', 'Finance', 'Misc'] 

    # return query results to the template
    context = {'search_results': search_results, 'TOSs': TOSs, 'categories':categories}
    return render(request, 'HomeScreen/search_for_tos.html', context)

@login_required
def submit(request):
     # if user is submitting a new TOS
   
    if request.method == 'POST':
        form = TOSForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # Bot Section
            sp = spacyClass()

            # Set text for bot and match phrases
            sp.fillText(instance.fullText)
            sp.phraseMatch()
            # add matched sentences to database
            for index, sentence in sp.matchedDict.items():
                # get element
                element = Element.objects.get(pk=index+1)
                # add matched element and sentence to TOS
                instance.elements.add(element, through_defaults={
                    'associatedText': sentence})
            #set rating to 0 for not yet rated, clear for next TOS
            instance.communityRating = 0
            sp.matchedDict.clear()
            # output successful message and redirect to view that TOS in view page
            messages.success(request, 'TOS Submitted!')
            instance.author = request.user
            instance.save()
            return redirect('ViewTOS', instance.name)
    else:
        form = TOSForm()
    return render(request, 'HomeScreen/submit.html', {'form': form})

def ViewTOS(request, tos_name=''):
     # get the TOS from the database
    query = TOS.objects.get(name=tos_name)

    # Get Admin-approved edits
    Accepted_Edits = Edit.objects.filter(status='Accepted', tos=query) 

    #get element found in TOS with their texts
    allText = ElementText.objects.filter(tos=query) 

    # Elements not found in TOS
    t = Element.objects.all()
    tos_id = query.id
    tosElements = t.exclude(tos = tos_id)

    # TOS out of date flag
    tosOOD = query.outOfDate
    # get community Rating
    if query.communityRating != 0:
        commRank = '{0:.1f}'.format(query.communityRating/query.communityCount)
    else:
        commRank = 0

    adminRank= query.weightRating
    
    tosAuthor = query.author
    tosDate = query.date

    #commmunityRanking Form Post 
    if request.method == 'POST':
        r_form = RankingForm(request.POST)
        if r_form.is_valid():
            print('Check')
            numDict = r_form.cleaned_data['ranking']
            value = int(numDict)
            query.communityRating = int(query.communityRating) + value
            query.communityCount = query.communityCount + 1
            query.save()
            messages.success(request, f'Your ranking has been added.')
            return redirect('ViewTOS', tos_name)
    else:
        r_form = RankingForm()

    # return the TOS to the template
    context = {
            'tos_name': tos_name, 
            'tosElements':tosElements, 
            'tos_text': query.fullText, 
            'allText': allText,
            'edits':Accepted_Edits, 
            'outOfDate':tosOOD,
            'com_rank': commRank, 
            'admin_rank':adminRank, 
            'tosAuthor':tosAuthor, 
            'tosDate':tosDate,
            'r_form':r_form
    }
   
    
    # If TOS is out of date
    if 'OutOfDate' in request.GET: 
        TOS.objects.filter(name=tos_name).update(outOfDate = True)
        TOS.objects.filter(name=tos_name).update(date = datetime.datetime.now())
        messages.success(request, ("TOS is now out of date!!"))
        return redirect('ViewTOS', tos_name)
    
    return render(request, 'HomeScreen/ViewTOS.html', context)

@login_required
def Edit_Page(request, tos_name=''):
    # get name of TOS for use in edit page
    query = TOS.objects.get(name=tos_name)
    
    # get TOS Elements and text
    text = ElementText.objects.filter(tos=query)
   
    # Get user-submitted edits
    AllEdits = Edit.objects.filter(tos=query) 

    t = Element.objects.all()
    tos_id = query.id
    tosElements = t.exclude(tos = tos_id)
    
    # Create form for rendering
    form = EditForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            edit = form.save(commit=False)
            edit.author = request.user 
            edit.tos = query
            edit.save()
            return redirect('Detail-Edit', pk=edit.id)
        else:
            return render(request, 'HomeScreen/partials/Edit_Form.html', {
                'form': form
            })
    #get community Rating
    if query.communityRating != 0:
        commRank = '{0:.1f}'.format(query.communityRating/query.communityCount)
    else:
        commRank = 0.0
    # return TOS  and Edit Form data to template
    context = {
            'tos':query, 
            'tos_name':tos_name, 
            'tosElements':tosElements, 
            'tos_text':query.fullText, 
            'allText':text, 
            'form':form,
            'edits':AllEdits,
            'commRank': commRank
            }
    return render(request, 'HomeScreen/Edit.html', context)

def Create_Edit_Form(request):
    context = {
            'form':EditForm()
    }
    return render(request, 'HomeScreen/partials/Edit_Form.html', context)

def Detail_Edit(request, pk):
    edit = Edit.objects.get(pk=pk)
    context = {
            'Edit':edit,
    }
    return render(request, 'HomeScreen/partials/Detail_Edit.html', context)

def searchBarView(request):
    username = request.username

    return render(request, 'HomeScreen/searchbar.html', {'user': username})
