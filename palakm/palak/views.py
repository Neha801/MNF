from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from palak.models import Script_info
from palak.models import Character_edit


def homepage(request):   
    return render(request,'palak/pages/homepage.html') 

def screenplays(request):  
    msg = Script_info.objects.all() 
    
    return render(request,'palak/pages/screenplays.html',{"msg":msg}) 

def character(request):   
    return render(request,'palak/pages/character.html') 

def character_edit(request):
    if request.method=="POST":
        print("request",request.FILES)
        character_image =request.FILES['character_image']
        character_name = request.POST.get('character_name', '')
        gender = request.POST.get('gender', '')
        age_group = request.POST.get('age_group', '')
        music = request.POST.get('music', '')
        print("music",music)
        

        Character_edit.objects.create( character_image=character_image,character_name=character_name,gender=gender,age_group=age_group,music=music)  
    return render(request,'palak/pages/character_edit.html') 

def script_info(request):
    if request.method=="POST":
        
        script_title = request.POST.get('script_title', '')
        Author_name  = request.POST.get('Author_name', '')
        genre = request.POST.getlist('genre[]', '')
        language_of_action_line = request.POST.get('language_of_action_line', '')
        language_of_dialogues = request.POST.get('language_of_dialogues', '')
        script_written_in = request.POST.get('script_written_in', '')
        time = request.POST.get('time', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        scriptfile = request.FILES['scriptfile']

        Script_info.objects.create(script_title=script_title, Author_name=Author_name, genre=genre,language_of_action_line=language_of_action_line,
        language_of_dialogues=language_of_dialogues,script_written_in=script_written_in,time =time ,
        country=country,city=city,scriptfile=scriptfile)
        
        
    return render(request, 'palak/pages/script_info.html')

def budget(request):
   
   if request.method == 'POST' and request.FILES['Choose Script']:
        myfile = request.FILES['Choose Script']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        uploaded_file_url=uploaded_file_url.replace('/media/','')
        
        file=request.POST.getlist('mycheckboxname')
        currency=request.POST.get('currency1')
        time=request.POST.get('time1')
        city=request.POST.get('city1')
        language=request.POST.get('language1')
        date=request.POST.get('date1')
        budget=request.POST['text1']
        
        return render(request, 'palak/pages/budget1.html', {"budget":budget,"city":city,"curr":currency,"time":time,"date":date,"language":language,'duration':time,'file':file,'uploaded_file_url': uploaded_file_url})
   
   return render(request,'palak/pages/budget.html')  

def stage1(request):
   
    if request.method == 'POST':
            #if request.POST.get('text7') and request.POST.get('text8') and request.POST.get('text9') and request.POST.get('text10') and request.POST.get('text11') and request.POST.get('text12') and request.POST.get('text13') and request.POST.get('text14') and request.POST.get('text15') :
           post=Budget()
           post.Actors= float(request.POST['text7'])
           post.Other_Actors= float(request.POST['text8'])
           post.Production= request.POST['text9']
           post.Director= request.POST['text10']
           post.Producer= request.POST['text11']
           post.post_production= request.POST['text12']
           post.Legal= request.POST['text13']
           post.Marketing= request.POST['text14']
           post.Miscellaneous= request.POST['text15']
           post.Total_Budget=request.POST['text1']
           post.Project=request.POST['project']
           post.User=request.user
           post.save()
           return render(request, 'palak/pages/stage1.html')  
		
    else :
       total_budget=int(request.GET['text1'])
       currency=request.GET.get('text3')
       project=request.GET.get('project')
       percentage_list=[0.2,0.05,0.3,0.05,0.05,0.05,0.02,0.27,0.01]
       lead_actor= int(0.2*total_budget)
       other_actors=int(0.05*total_budget)
       production=int(0.3*total_budget)
       director=int(0.05*total_budget)
       producer=int(0.05*total_budget)
       post_production=int(0.05*total_budget)
       legal=int(0.02*total_budget)
       marketing=int(0.27*total_budget)
       miscellaneous=int(0.01*total_budget)
       context={'a':lead_actor,'b':other_actors,'c':production,'d':director,'e':producer,'f':post_production,'g':legal,'h':marketing,'i':miscellaneous,'curr':currency,'tb':total_budget,'project':project}
	
    return render(request,'palak/pages/stage1.html',context)

def update_stage1(request):
    total_budget=int(request.GET['text1'])
    currency=request.GET.get('text3')
    currency=request.GET.get('currency')
    time=request.GET.get('time')
    city=request.GET.get('city')
    language=request.GET.get('language')
    date=request.GET.get('date')
    percentage_list=[20/100,5/100,30/100,4/100,4/100,5/100,2/100,24/100,1/100,5/100]
    
    list=[20*total_budget/100,5*total_budget/100,30*total_budget/100,4*total_budget/100,4*total_budget/100,5*total_budget/100,2*total_budget/100,24*total_budget/100,1*total_budget/100,5*total_budget/100]
  
    
	    
    lead_actor1=float(request.GET['text7'])
    other_actors1=float(request.GET['text8'])
    production1=float(request.GET['text9'])
    director1=float(request.GET['text10'])
    producer1=float(request.GET['text11'])
    post_production1=float(request.GET['text12'])
    legal1=float(request.GET['text13'])
    marketing1=float(request.GET['text14'])
    miscellaneous1=float(request.GET['text15'])
    writer1=float(request.GET['writer'])
    list1=[lead_actor1,other_actors1,production1,director1,producer1,post_production1,legal1,marketing1,miscellaneous1,writer1]
    
	
    dif=[]
    sum1=0
    sum_initial=0
    percentage=[]
    for i in range (0,10):
        percentage.append(0)
    
    for i in range (0,10):
        dif.append(list[i]-list1[i])
		
    if sum(list)<sum(list1):
       for i in range (0,10):
           if dif[i]!=0:
              percentage[i]=list1[i]/total_budget
              sum1=sum1+list1[i]/total_budget
              sum_initial=sum_initial+percentage_list[i]
       for i in range (0,10):
           if dif[i]==0:
              percentage[i]=percentage_list[i]*(1-sum1)/(1-sum_initial)
       for i in range (0,10):  
           list[i]=percentage[i]*total_budget	
       differ=sum(list)-total_budget
       lead_actor=round(list[0])
       other_actors=round(list[1])
       production=round(list[2])
       director=round(list[3])
       producer=round(list[4])
       post_production=round(list[5])
       legal=round(list[6])
       marketing=round(list[7])-round(differ)
       miscellaneous=round(list[8])
       writer=round(list[9])
	
    if sum(list)>=sum(list1):
       for i in range(0,10):
           if dif[i]!=0:
              for j in range(0,10):
	                list[j]=list1[j]+((percentage_list[j])/(1-percentage_list[i]))*dif[i]
       for i in range(0,10):
           if list[i]<0:
              list[i]=0
    
	   
       for i in range(0,10):
          if dif[i]!=0:
	          list[i]=list1[i]
       dif.clear()
       differ=sum(list)-total_budget
	   
       lead_actor=round(list[0])
       other_actors=round(list[1])
       production=round(list[2])
       director=round(list[3])
       producer=round(list[4])
       post_production=round(list[5])
       legal=round(list[6])
       marketing=round(list[7])-round(differ)
       miscellaneous=round(list[8])
       writer=round(list[9])
	
	#if dif[0]!=0:
        #lead_actor=int(request.GET['text7'])
        #other_actors=int(0.05*total_budget+(0.2*0.05263+0.05)*dif[0])
        #production=int(0.3*total_budget+(0.2*0.4285+0.3)*dif[0])
        #director=int(0.05*total_budget+(0.2*0.05263+0.05)*dif[0])
        #producer=int(0.05*total_budget+(0.2*0.05263+0.05)*dif[0])
        #post_production=int(0.05*total_budget+(0.2*0.05263+0.05)*dif[0])
        #legal=int(0.02*total_budget+(0.2*0.02040+0.02)*dif[0])
        #marketing=int(0.27*total_budget+(0.27*0.37+0.27)*dif[0])
        #miscellaneous=int(0.01*total_budget+(0.01*0.01010+0.01)*dif[0])
   
	
    
    
    context={"writer":writer,"city":city,"curr":currency,"time":time,"date":date,"language":language,'duration':time,'a':lead_actor,'b':other_actors,'c':production,'d':director,'e':producer,'f':post_production,'g':legal,'h':marketing,'i':miscellaneous,'curr':currency,'tb':total_budget}
	
    return render(request,'palak/pages/stage1.1.html',context)

	
def updated_stage1(request):
    total_budget=int(request.GET['text1'])
    currency=request.GET.get('text3')
    percentage_list=[0.2,0.05,0.3,0.05,0.05,0.05,0.02,0.27,0.01]
    currency=request.GET.get('currency')
    time=request.GET.get('time')
    city=request.GET.get('city')
    language=request.GET.get('language')
    date=request.GET.get('date')
    list3=['text16','text17','text18','text19','text20','text21','text22','text23','text24']
    list2=[]
    for i in range(0,9):
	      list2.append(float(request.GET[list3[i]]))
    
    
    lead_actor1=float(request.GET['text7'])
    other_actors1=float(request.GET['text8'])
    production1=float(request.GET['text9'])
    director1=float(request.GET['text10'])
    producer1=float(request.GET['text11'])
    post_production1=float(request.GET['text12'])
    legal1=float(request.GET['text13'])
    marketing1=float(request.GET['text14'])
    miscellaneous1=float(request.GET['text15'])
    list1=[lead_actor1,other_actors1,production1,director1,producer1,post_production1,legal1,marketing1,miscellaneous1]
    dif=[]
    sum1=0
    sum_initial=0
    percentage=[]
    for i in range (0,9):
        percentage.append(0)
    	
    for i in range (0,9):
        dif.append(list1[i]-list2[i])
    if sum(list1)<sum(list2):
       for i in range (0,9):
          if dif[i]!=0:
             percentage[i]=list2[i]/total_budget
             sum1=sum1+list2[i]/total_budget
             sum_initial=sum_initial+percentage_list[i]
       for i in range (0,9):
          if dif[i]==0 and sum_initial!=0:
           percentage[i]=percentage_list[i]*(1-sum1)/(1-sum_initial)
       for i in range (0,9):  
           list1[i]=percentage[i]*total_budget
       differ=sum(list1)-total_budget	
       lead_actor=round(list1[0])
       other_actors=round(list1[1])
       production=round(list1[2])
       director=round(list1[3])
       producer=round(list1[4])
       post_production=round(list1[5])
       legal=round(list1[6])
       marketing=round(list1[7]-round(differ))
       miscellaneous=round(list1[8])		   
    if sum(list1)>=sum(list2):
       for i in range(0,9):
           if dif[i]!=0:
              for j in range(0,9):
	                list1[j]=list1[j]+((percentage_list[j])/(1-percentage_list[i]))*dif[i]
       for i in range(0,9):
           if list1[i]<0:
              list1[i]=0
    
	
       for i in range(0,9):
          if dif[i]!=0:
	          list1[i]=list2[i]
       dif.clear()
       differ=sum(list1)-total_budget
       lead_actor=round(list1[0])
       other_actors=round(list1[1])
       other_actors=round(list1[1])
       production=round(list1[2])
       director=round(list1[3])
       producer=round(list1[4])
       post_production=round(list1[5])
       legal=round(list1[6])
       marketing=round(list1[7])-round(differ)
       miscellaneous=round(list1[8])
    
    
    
	
	
    context={"city":city,"curr":currency,"time":time,"date":date,"language":language,'duration':time,'a':lead_actor,'b':other_actors,'c':production,'d':director,'e':producer,'f':post_production,'g':legal,'h':marketing,'i':miscellaneous,'curr':currency,'tb':total_budget}
	
    return render(request,'palak/pages/stage1.2.html',context)
	
#No use	
def budget_stage1(request):
    form = BudgetForm(request.POST)
    if request.method == 'POST':
       if form.is_valid():
	        cal=form.save()
	        cal.user = request.user
	        cal.save()
	        return redirect('stage1')	
    
    return render(request,'palak/pages/table.html',{'form':form})

def update_budget(request):
         a=float(request.GET['text7'])
         b=float(request.GET['text8'])
         c=float(request.GET['text9'])
         d=float(request.GET['text10'])
         e=float(request.GET['text11'])
         f=float(request.GET['text12'])
         g=float(request.GET['text13'])
         h=float(request.GET['text14'])
         i=float(request.GET['text15'])
         total_budget=int(request.GET['text1'])
         currency=request.GET.get('currency')
         time=request.GET.get('time')
         city=request.GET.get('city')
         language=request.GET.get('language')
         date=request.GET.get('date')
         writer=request.GET.get('writer')
         return render(request,'palak/pages/update_budget.html',{"writer":writer,"city":city,"curr":currency,"time":time,"date":date,"language":language,'duration':time,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'tb':total_budget })

def updated_budget(request):
         a=float(request.GET['text16'])
         b=float(request.GET['text17'])
         c=float(request.GET['text18'])
         d=float(request.GET['text19'])
         e=float(request.GET['text20'])
         f=float(request.GET['text21'])
         g=float(request.GET['text22'])
         h=float(request.GET['text23'])
         i=float(request.GET['text24'])
         total_budget=int(request.GET['text1'])
         return render(request,'palak/pages/updated_budget.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'tb':total_budget })
def datatable(request):
         return render(request,'palak/pages/datatable.html')

#Not in use		 
def stages2(request):
    actors=stage2_Casting()
    Bud=Budget.objects.filter(User=request.user)
    Project=request.GET.get('project')
    
    Costing_stage1_list=[]
    for j in Bud:
        Costing_stage1_list.append(j.Actors) 
        Costing_stage1_list.append(j.Other_Actors)
        Costing_stage1_list.append(j.Production)
        Costing_stage1_list.append(j.Director)
        Costing_stage1_list.append(j.Producer)
        Costing_stage1_list.append(j.post_production)
        Costing_stage1_list.append(j.Legal)
        Costing_stage1_list.append(j.Marketing)
        Costing_stage1_list.append(j.Miscellaneous)
    context=stage2_production(Costing_stage1_list)
    Actors=['Avichal','Vishwas','Asha']
    Cast=zip(Actors,actors)
    Other=[]
    sum_act=Costing_stage1_list[0]
    for i in range(0,9):
       if i!=0 and i!=2:
           Other.append(Costing_stage1_list[i])
    #Other=[5000,5000,5000,5000,2000,27000,1000]
    a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=[]
    list=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]
    sum_prod=Costing_stage1_list[2]
    for i in  range(0,12):
        list[i]=context[i]
        #sum_prod=sum_prod+context[i]
    for i in  range(0,len(Actors)):
        list[i+12]=actors[i]
       # sum_act=sum_act+actors[i]
    for i in range(0,7):
	    list[i+12+len(Actors)]=Other[i]
    return render(request,'palak/pages/stage2.html',{'project':Project,'sum_prod':sum_prod,'sum_act':sum_act,'Actors':Cast,'actors':actors,'a':round(list[0],2),'b':round(list[1],2),'c':round(list[2],2),'d':round(list[3],2),'e':round(list[4],2),'f':list[5],'g':list[6],'h':list[7],'i':list[8],'j':list[9],'k':list[10],'l':list[11],'m':list[12],'n':list[13],'o':list[14],'p':list[15],'q':list[16],'r':list[17],'s':list[18],'t':list[19],'u':list[20],'v':list[21]})		

def script_input(request):
    project=request.GET.get('project')
    return render(request,'palak/pages/script_input.html',{'project':project})

def update_stage2_budget(request):
    
    a1=float(request.GET['pro1'])
    b1=float(request.GET['pro2'])
    c1=float(request.GET['pro3'])
    d1=float(request.GET['pro4'])
    e1=float(request.GET['pro5'])
    f1=float(request.GET['pro6'])
    g1=float(request.GET['pro7'])
    h1=float(request.GET['pro8'])
    i1=float(request.GET['pro9'])
    j1=float(request.GET['pro10'])
    k1=float(request.GET['pro11'])
    l1=float(request.GET['pro12'])
    pro=a1+b1+c1+d1+e1+f1+g1+h1+i1+j1+k1+l1
    #m1=float(request.GET['act0'])
    #n1=float(request.GET['act1'])
    #o1=float(request.GET['act2'])
    #act=m1+n1+o1
	
    p1=float(request.GET['oth1'])
    q1=float(request.GET['oth2'])
    r1=float(request.GET['oth3'])
    s1=float(request.GET['oth4'])
    t1=float(request.GET['oth5'])
    u1=float(request.GET['oth6'])
    v1=float(request.GET['oth7'])
    w1=float(request.GET['oth8'])
    x1=float(request.GET['oth9'])
    tb=int(request.GET['text1'])
    len_Actors=int(request.GET['len_Actors'])
    len_other_actors=int(request.GET['len_other_actors'])
    range_actors=range(len_Actors)
    range_other_actors=range(len_other_actors)
    lis_cast=[]
    lis_cast_name=[]
    lis_other_cast=[]
    lis_other_cast_name=[]
	
    for i in range(0,len_Actors):
	    lis_cast.append(float(request.GET['act'+str(i)]))
    for i in range(0,len_Actors):
	    lis_cast_name.append((request.GET['act_name'+str(i)]))
    lis_act=zip(lis_cast,lis_cast_name,range_actors)
    for i in range(0,len_other_actors):
	    lis_other_cast.append(float(request.GET['oth_act'+str(i)]))
    for i in range(0,len_other_actors):
	    lis_other_cast_name.append((request.GET['oth_act_name'+str(i)]))
    lis_oth_act=zip(lis_other_cast,lis_other_cast_name,range_other_actors)
    currency=request.GET.get('currency')
    time=request.GET.get('time')
    city=request.GET.get('city')
    language=request.GET.get('language')
    date=request.GET.get('date')
    y1=float(request.GET['writer'])
    scripts=request.GET.get('script')
    
    return render(request,'palak/pages/update_stage2.html',{"scripts":scripts,"len_Actors":len_Actors,"len_other_actors":len_other_actors,"lis_act":lis_act,"lis_oth_act":lis_oth_act,'y':round(y1),"w":round(w1),"x":round(x1),"city":city,"curr":currency,"time":time,"date":date,"language":language,'duration':time,'pro':round(pro),'tb':round(tb),'a':round(a1),'b':round(b1),'c':round(c1),'d':round(d1),'e':round(e1),'f':round(f1),'g':round(g1),'h':round(h1),'i':round(i1),'j':round(j1),'k':round(k1),'l':round(l1),'p':round(p1),'q':round(q1),'r':round(r1),'s':round(s1),'t':round(t1),'u':round(u1),'v':round(v1)})	

def index(request):
    if request.POST:
        # give the absolute path to your `text4midiAllMilisecs.py`
        # and for `tiger.mid`
        # subprocess.call(['python', '/path/to/text4midiALLMilisecs.py', '/path/to/tiger.mid'])
        uploaded_file_url=request.POST.get('script')
        subprocess.call(['python',process_path,uploaded_file_url])
        

    return render(request,'palak/pages/index.html',{"uploaded_file_url":uploaded_file_url})

def checkbox(request):
    mylist=request.GET.getlist('mycheckboxname')
    if 'script' in mylist:
      
        Today_date = dt.today()
        #Bud=Budget.objects.filter(User=request.user)
        Project=request.GET.get('project')
        total_budget=int(request.GET['text1'])
        currency=request.GET.get('currency1')
        time=int(request.GET.get('time1'))

        city=request.GET.get('city1')
        language=request.GET.get('language1')
        date1=(request.GET.get('date1'))
        date1=date1.replace('2020','20')
        d=dt.strptime(date1, '%y-%m-%d' )
        Days_user=str(d-Today_date)
        Daysu=Days_user.split()

        locations=[]
        All_actors=[]
        video=[]
        posts = Stage2.objects.all()
        scripts=request.GET.get('script')
        print(scripts)
        db_script=scripts.split('.')[0]
        subprocess.call(['python',process_path,scripts])	  
      
    #Wrong logic
    #   for stage2 in script: 
    #       locations=stage2.all_locations
    #       All_actors=stage2.all_actors
    #       Duration=round(stage2.video_time_produced)
    #       Total_Days=stage2.total_shoot_days
    #       Total_scenes=stage2.total_scenes
    #       Importance=stage2.character_importance
    #       costume=stage2.costumes
    #       makeup=stage2.makeup
    #       vehicle=stage2.vehicles
    #       stunt=stage2.stunts
    #       livestock=stage2.livestock
    #       VFX=stage2.optical_fx
        script=posts.filter(Script=db_script)[0]
        locations=script.all_locations
        All_actors=script.all_actors
        Duration=round(script.video_time_produced)
        Total_Days=script.total_shoot_days
        Total_scenes=script.total_scenes
        Importance=script.character_importance
        costume=script.costumes
        makeup=script.makeup
        vehicle=script.vehicles
        stunt=script.stunts
        livestock=script.livestock
        VFX=script.optical_fx
      
        Short_Day=Total_Days-int(Daysu[0])+5
        Per_day=int(total_budget/Total_Days)
        Budget_less=100000*Total_Days-total_budget
        
        Other_actors=[]
        Actors_Real=[]
        Imp=list(Importance.values()) 
        Importance=sorted(Importance.items(), key=lambda x: x[1], reverse=True)
        for i in range(0,len(Imp)):
            All_actors[i]=Importance[i][0]
        for i in range(0,len(Imp)):
            Imp[i]=Importance[i][1]
        s=sum(Imp)
        for i in range(0,len(Imp)):
            if (Imp[i]/s)< 0.1:
                Other_actors.append(Imp[i])
            if (Imp[i]/s)> 0.1:
                Actors_Real.append(Imp[i])
        len_Actors=len(Actors_Real)
        len_other_actors=len(Other_actors)
        sum_actors=sum(Actors_Real)
        sum_oth_act=sum(Other_actors)
        for i in range(0,len(Other_actors)):
            Other_actors[i]=(Other_actors[i]/sum_oth_act)
        for i in range(0,len(Actors_Real)):
            Actors_Real[i]=(Actors_Real[i]/sum_actors)
        len_stunt=0
        len_VFX=0
        len_act=len(All_actors)
        len_loc=len(locations)
        #len_stunt=len(stunt)
        len_livestock=len(livestock)
        len_vehicle=len(vehicle)
        len_costume=len(costume)
        len_makeup=len(makeup)
        #len_VFX=len(VFX)	  
        Costing_stage1_list=[]
        variable_heads_count=[len_loc,len_makeup,len_VFX,len_costume,len_livestock,len_vehicle,len_stunt]
        percentage_list=[0.2,0.05,0.3,0.04,0.04,0.05,0.02,0.24,0.01,0.05]
        for i in range(0,10):
            Costing_stage1_list.append(percentage_list[i]*total_budget) 
        context=stage2_production(Costing_stage1_list,variable_heads_count)
        
        actors=stage2_Casting(Costing_stage1_list,All_actors,Actors_Real,Other_actors)[0]
        ot_actors=stage2_Casting(Costing_stage1_list,All_actors,Actors_Real,Other_actors)[1]
        
        actors_cost=[round(num) for num in actors]
        ot_actors_cost=[round(num) for num in ot_actors]
        range_actors=range(len(All_actors))
        Cast_cost=zip(actors_cost,range_actors)   #used for merging count var with actors
        Cast_name=zip(All_actors,range_actors)    #used for merging count var with other_actors
        Cast=zip(All_actors,actors_cost)
        range_other_actors=range(len(ot_actors_cost))
        Other_cast=zip(ot_actors_cost,range_other_actors)
        Other_cast_name=zip(All_actors[len(All_actors)-len(ot_actors):len(All_actors)],range_other_actors)	  
        Cast_ot=zip(All_actors[len(All_actors)-len(ot_actors):len(All_actors)],ot_actors_cost)
        Cast_ot=sorted(Cast_ot, key = lambda t: t[1],reverse=True)
        Cast=sorted(Cast, key = lambda t: t[1],reverse=True)
        Other=[]
        sum_act=Costing_stage1_list[0]
        for i in range(0,10):
            Other.append(Costing_stage1_list[i])
        
        sum_prod=Costing_stage1_list[2]
        
        list1=context+Other
        list1=[round(num) for num in list1]
        template='palak/pages/stage2.html'
        project=request.GET.get('project')
        context={"scripts":scripts,"len_Actors":len_Actors,"len_other_actors":len_other_actors,"Other_cast":Other_cast,"Other_cast_name":Other_cast_name,"Budget_less":Budget_less,"Cast_ot":Cast_ot,"Per_Day":Per_day,"Short_Day":Short_Day,"Days_user":Daysu[0],"loc":len_loc,"Duration":Duration,"Total_days":Total_Days,"Total_scenes":Total_scenes,"len_Act":len_act,"Cast_name":Cast_name,"city":city,"Cast1":Cast_cost,"curr":currency,"time":time,"date1":date1,"language":language,'duration':time,'tb':total_budget,'project':Project,'sum_prod':sum_prod,'sum_act':sum_act,'Cast':Cast,'actors':actors,'a':round(list1[0]),'b':round(list1[1]),'c':round(list1[2]),'d':round(list1[3]),'e':round(list1[4]),'f':round(list1[5]),'g':round(list1[6]),'h':round(list1[7]),'i':round(list1[8]),'j':round(list1[9]),'k':round(list1[10]),'l':round(list1[11]),'m':round(list1[12]),'n':round(list1[13]),'o':round(list1[14]),'p':round(list1[12]),'q':round(list1[13]),'r':round(list1[14]),'s':round(list1[15]),'t':round(list1[16]),'u':round(list1[17]),'v':round(list1[18]),'w':round(list1[19]),'x':round(list1[20]),'y':round(list1[21])}
    else:
      total_budget=int(request.GET['text1'])
      currency=request.GET.get('currency')
      time=request.GET.get('time')
      city=request.GET.get('city')
      language=request.GET.get('language')
      date=request.GET.get('date')
      project=request.GET.get('project')
   	  
      percentage_list=[0.2,0.05,0.3,0.04,0.04,0.05,0.02,0.24,0.01,0.05]
      lead_actor= int(0.2*total_budget)
      other_actors=int(0.05*total_budget)
      production=int(0.3*total_budget)
      director=int(0.04*total_budget)
      producer=int(0.04*total_budget)
      post_production=int(0.05*total_budget)
      legal=int(0.02*total_budget)
      marketing=int(0.24*total_budget)
      miscellaneous=int(0.01*total_budget)
      writer=int(0.05*total_budget)
      context={"city":city,"curr":currency,"time":time,"date":date,"language":language,'duration':time,'a':lead_actor,'b':other_actors,'c':production,'d':director,'e':producer,'f':post_production,'g':legal,'h':marketing,'i':miscellaneous,'curr':currency,'tb':total_budget,'project':project,'writer':writer}
	
    
      template="palak/pages/stage1.html"
    return render(request,template,context)

def update_stage2(request):
    currency=request.GET.get('currency')
    time=request.GET.get('time')
    city=request.GET.get('city')
    language=request.GET.get('language')
    date1=request.GET.get('date')
    scripts=request.GET.get('script')
    fixed_heads_count_prod=[1,1,1,1,1]
    fixed_heads_count=[1,1,1,1,1,1,1,1,1,1]
	
    Costing_stage1_list=[]
    total_budget=int(request.GET['text1'])
    
    Other=[]
    #for i in range(0,10):
     #   Costing_stage1_list.append(percentage_list[i]*total_budget) 
    #context=stage2_production(Costing_stage1_list,variable_heads_count)
    #actors=stage2_Casting(Costing_stage1_list)
    #for i in range(0,10):
      
     #      Other.append(Costing_stage1_list[i])
    #Other=[5000,5000,5000,5000,2000,27000,1000]
    """for i in range(0,len(actors)):
        context.append(actors[i])
    for i in range(0,len(Other)):
        context.append(Other[i])"""
    #context=context+actors+Other
    a=float(request.GET['pro1'])
    b=float(request.GET['pro2'])
    c=float(request.GET['pro3'])
    d=float(request.GET['pro4'])
    e=float(request.GET['pro5'])
    f=float(request.GET['pro6'])
    g=float(request.GET['pro7'])
    h=float(request.GET['pro8'])
    i=float(request.GET['pro9'])
    j=float(request.GET['pro10'])
    k=float(request.GET['pro11'])
    l=float(request.GET['pro12'])
    
    s=float(request.GET['oth4'])
    t=float(request.GET['oth5'])
    u=float(request.GET['oth6'])
    v=float(request.GET['oth7'])
    w=float(request.GET['oth8'])
    x=float(request.GET['oth9'])
    y=float(request.GET['writer'])
    len_Actors=int(request.GET['len_Actors'])
    len_other_actors=int(request.GET['len_other_actors'])
    range_actors=range(len_Actors)
    range_other_actors=range(len_other_actors)
    lis_cast=[]
    lis_cast_name=[]
    lis_other_cast=[]
    lis_other_cast_name=[]
    
    for i in range(0,len_Actors):
	    lis_cast.append(float(request.GET['act'+str(i)]))
    for i in range(0,len_Actors):
	    lis_cast_name.append((request.GET['act_name'+str(i)]))
    lis_act=zip(lis_cast,lis_cast_name,range_actors)
    for i in range(0,len_other_actors):
	    lis_other_cast.append(float(request.GET['oth_act'+str(i)]))
    for i in range(0,len_other_actors):
	    lis_other_cast_name.append((request.GET['oth_act_name'+str(i)]))
    lis_oth_act=zip(lis_other_cast,lis_other_cast_name,range_other_actors)
    
	
	
    
	
    a1=float(request.GET['pro21'])
    b1=float(request.GET['pro22'])
    c1=float(request.GET['pro23'])
    d1=float(request.GET['pro24'])
    e1=float(request.GET['pro25'])
    f1=float(request.GET['pro26'])
    g1=float(request.GET['pro27'])
    h1=float(request.GET['pro28'])
    i1=float(request.GET['pro29'])
    j1=float(request.GET['pro210'])
    k1=float(request.GET['pro211'])
    l1=float(request.GET['pro212'])
   
    s1=float(request.GET['oth4'])
    t1=float(request.GET['oth5'])
    u1=float(request.GET['oth6'])
    v1=float(request.GET['oth7'])
    w1=float(request.GET['oth8'])
    x1=float(request.GET['oth9'])
    y1=float(request.GET['writer']) 
    
    lis_cast1=[]
    lis_other_cast1=[]
    
    for i in range(0,len_Actors):
	    lis_cast1.append(float(request.GET['act1'+str(i)]))
    
    lis_act=zip(lis_cast1,range_actors)
    for i in range(0,len_other_actors):
	    lis_other_cast1.append(float(request.GET['act2'+str(i)]))
    
    lis_oth_act=zip(lis_other_cast1,range_other_actors)
	
    
    posts = Stage2.objects.all()
    scripts=request.GET.get('script')
    db_script=scripts.split('.')[0]
    script=posts.filter(Script=db_script)[0]
    
    
    locations=script.all_locations
    All_actors=script.all_actors
    Duration=round(script.video_time_produced)
    Total_Days=script.total_shoot_days
    Total_scenes=script.total_scenes
    Importance=script.character_importance
    costume=script.costumes
    makeup=script.makeup
    vehicle=script.vehicles
    stunt=script.stunts
    livestock=script.livestock
    VFX=script.optical_fx

    len_act=len(All_actors)
    len_loc=len(locations)
    len_stunt=0
    len_livestock=len(livestock)
    len_vehicle=len(vehicle)
    len_costume=len(costume)
    len_makeup=len(makeup)
    len_VFX=0	
    act_list=[]
    other_act_list=[]
    for i in range(0,len_Actors):
       act_list.append(1)
		
    for i in range(0,len_other_actors):	
       other_act_list.append(1)
	   
    variable_heads_count_prod=[len_loc,len_makeup,len_VFX,len_costume,len_livestock,len_vehicle,len_stunt]      
    variable_heads_count=fixed_heads_count_prod+variable_heads_count_prod+fixed_heads_count+act_list+other_act_list
    percentage_list_production=stage2_production_percent(variable_heads_count_prod)
    Other_actors=[]
    Actors_Real=[]
    Imp=list(Importance.values()) 
    Importance=sorted(Importance.items(), key=lambda x: x[1], reverse=True)
   
    for i in range(0,len(Imp)):
         Imp[i]=Importance[i][1]
    s=sum(Imp)
    for i in range(0,len(Imp)):
        if (Imp[i]/s)< 0.1:
          Other_actors.append(Imp[i])
        if (Imp[i]/s)> 0.1:
          Actors_Real.append(Imp[i])
    len_Actors=len(Actors_Real)
    en_other_actors=len(Other_actors)
    sum_actors=sum(Actors_Real)
    sum_oth_act=sum(Other_actors)
    for i in range(0,len(Other_actors)):
	      Other_actors[i]=(Other_actors[i]*0.05/sum_oth_act)
    for i in range(0,len(Actors_Real)):
	      Actors_Real[i]=(Actors_Real[i]*0.2/sum_actors)
    
    
    
    percentage_list_others=[0.04,0.04,0.05,0.02,0.24,0.01,0.05]
    percentage_list=percentage_list_production+percentage_list_others+Actors_Real+Other_actors
    context=[a,b,c,d,e,f,g,h,i,j,k,l,s,t,u,v,w,x,y]+lis_cast+lis_other_cast
    context1=[a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,s1,t1,u1,v1,w1,x1,y1]+lis_cast1+lis_other_cast1
    total_budget=int(request.GET['text1'])
	
    dif=[]
    sum1=0
    sum_initial=0
    percentage=[]
    for i in range (0,19+len_Actors+len_other_actors):
        percentage.append(0)
    
    for i in range (0,19+len_Actors+len_other_actors):
        dif.append(context[i]-context1[i])
	
    #if sum(context)<sum(context1):
	#Taking the percentage 
    for i in range (0,19+len_Actors+len_other_actors):
           if dif[i]!=0 :                               #the percentage of heads which have been changed by user
              percentage[i]=context1[i]/total_budget    #assigning value to the changed head by directly dividing it with total budget
              sum1=sum1+context1[i]/total_budget        #taking sums of percentage which have been changed
              sum_initial=sum_initial+percentage_list[i] #taking sums of their initial percentage
    for i in range(0,19):
           if variable_heads_count[i]==0:                #similar process for the ones which have no value assigned
              sum1=sum1+context1[i]/total_budget
              sum_initial=sum_initial+percentage_list[i]
    for i in range (0,19+len_Actors+len_other_actors):
           if dif[i]==0 :                                #assigning percentage to ones which have not been changed
              percentage[i]=percentage_list[i]*(1-sum1)/(1-sum_initial)  #formula=>initial_percent*(1-sum of which have already been asigned)/(remaining percentage out of which needed to assign)
    for i in range (0,19+len_Actors+len_other_actors):
           if variable_heads_count[i]!=0:
              context[i]=percentage[i]*total_budget	
           else:
              context[i]=0
    for i in range (0,19+len_Actors+len_other_actors):
           if dif[i]!=0 :
              context[i]=context1[i]
    
    
    #differ=sum(context)-total_budget
    a=round(context[0])
    b=round(context[1])
    c=round(context[2])
    d=round(context[3])
    e=round(context[4])
    f=round(context[5])
    g=round(context[6])
    h=round(context[7])
    i=round(context[8])
    j=round(context[9])
    k=round(context[10])
    l=round(context[11])
   
    
    r=a+b+c+d+e+f+g+h+i+j+k+l
    
   
    
    s=round(context[12])
    t=round(context[13])
    u=round(context[14])
    v=round(context[15])
    w=round(context[16])
    x=round(context[17])
    y=round(context[18])
    for i in range(0,len_Actors):
	    lis_cast[i]=round(context[19+i])
    for i in range(0,len_other_actors):
	    lis_other_cast[i]=round(context[19+len_Actors+i])
		
    Cast=zip(lis_cast,lis_cast_name)
    Cast1=zip(lis_cast,range_actors)
    Cast2=zip(lis_cast_name,range_actors)
    Cast_ot=zip(lis_other_cast,lis_other_cast_name)
    Cast_ot1=zip(lis_other_cast,range_other_actors)
    Cast_ot2=zip(lis_cast_name,range_other_actors)
	
    p=round(sum(lis_cast))
    q=round(sum(lis_other_cast))
    return render(request,'palak/pages/stage2.1.html',{"scripts":scripts,"len_Actors":len_Actors,"len_other_actors":len_other_actors,"Cast1":Cast1,"Cast2":Cast2,"Cast_ot1":Cast_ot1,"Cast_ot2":Cast_ot2,"len_Actors":len_Actors,"len_other_actors":len_other_actors,"Cast_ot":Cast_ot,"loc":len_loc,"Duration":Duration,"Total_days":Total_Days,"Total_scenes":Total_scenes,"len_Act":len_act,"city":city,"curr":currency,"time":time,"language":language,'duration':time,"Cast":Cast,"x":x,"y":y,"w":w,"city":city,"curr":currency,"time":time,"date":date1,"language":language,'duration':time,'tb':total_budget,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v})	
	
	
                
    