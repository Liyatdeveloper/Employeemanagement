from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import*
from django.conf import settings
from django.conf.urls.static import static
import os
from django.views.decorators.cache import cache_control



# Create your views here.

def index(request):
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		pswd=request.POST['pswd']
		website=request.POST['website']
		var=Tbl_Company.objects.all().filter(email=email)
		if var:
			txt="""<script>alert('Already exist...');window.location='/register/';</script>"""
			return HttpResponse(txt)
		else:
			Tbl_Company(name=name,email=email,pswd=pswd,website=website).save()
			return render(request,'company_register.html')
	else:
		return render(request,'company_register.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def emp_register(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		phone=request.POST['phone']
		email=request.POST['email']
		pswd=request.POST['pswd']
		company=request.POST['company']
		cmpy_id=Tbl_Company.objects.get(id=company)
		chk=Tbl_Employee.objects.all().filter(email=email)
		if chk:
			txt="""<script>alert('Already exist...');window.location='/emp_register/';</script>"""
			return HttpResponse(txt)
		else:
			Tbl_Employee(fname=fname,lname=lname,phone=phone,email=email,pswd=pswd,company=cmpy_id).save()
			return render(request,'emp_register.html')
	else:
		var=Tbl_Company.objects.all()
		return render(request,'emp_register.html',{'var':var})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
	if request.method=="POST":
		email=request.POST['email']
		pswd=request.POST['pswd']
		admin=Tbl_Admin.objects.all().filter(email=email,pswd=pswd)
		cmpny=Tbl_Company.objects.all().filter(email=email,pswd=pswd)
		emp=Tbl_Employee.objects.all().filter(email=email,pswd=pswd)
		if admin:
			for x in admin:
				request.session['id']=x.id
			return render(request,'Admin/admin_home.html')
		elif cmpny:
			for x in cmpny:
				request.session['id']=x.id
			return render(request,'Company/cmpny_home.html')
		elif emp:
			for x in emp:
				request.session['id']=x.id
			return render(request,'Employee/emp_home.html')
		else:
			txt="""<script>alert('Invalid credentials...');window.location='/login/';</script>"""
			return HttpResponse(txt)
	else:
		return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
	if request.session.has_key('id'):
		del request.session['id']
		logout(request)
	return HttpResponseRedirect('/')





# Admin
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_home(request):
	if request.session.has_key('id'):
		return render(request,'Admin/admin_home.html')
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_view_cmpny(request):
	if request.session.has_key('id'):
		var=Tbl_Company.objects.all()
		return render(request,'Admin/admin_view_cmpny.html',{'var':var})
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_view_emp(request):
	if request.session.has_key('id'):
		var=Tbl_Employee.objects.all()
		return render(request,'Admin/admin_view_emp.html',{'var':var})
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_delete_cmpny(request):
	if request.session.has_key('id'):
		cmp_id=request.GET['id']
		Tbl_Company.objects.all().filter(id=cmp_id).delete()
		return HttpResponseRedirect('/admin_view_cmpny/')
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_delete_emp(request):
	if request.session.has_key('id'):
		emp_id=request.GET['id']
		Tbl_Employee.objects.all().filter(id=emp_id).delete()
		return HttpResponseRedirect('/admin_view_emp/')
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_edit_cmpny(request):
	if request.session.has_key('id'):
		if request.method=="POST":
			name=request.POST['name']
			email=request.POST['email']
			pswd=request.POST['pswd']
			website=request.POST['website']
			idd=request.POST['cmp_id']
			Tbl_Company.objects.all().filter(id=idd).update(name=name,email=email,pswd=pswd,website=website)
			return HttpResponseRedirect('/admin_view_cmpny/')
		else:
			cmp_id=request.GET['id']
			var=Tbl_Company.objects.all().filter(id=cmp_id)
			return render(request,'Admin/admin_edit_cmpny.html',{'var':var,'cmp_id':cmp_id})
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_edit_emp(request):
	if request.session.has_key('id'):
		if request.method=="POST":
			fname=request.POST['fname']
			lname=request.POST['lname']
			phone=request.POST['phone']
			email=request.POST['email']
			pswd=request.POST['pswd']
			company=request.POST['company']
			cmpy_id=Tbl_Company.objects.get(id=company)
			idd=request.POST['emp_id']
			Tbl_Employee.objects.all().filter(id=idd).update(fname=fname,lname=lname,phone=phone,email=email,pswd=pswd,company=cmpy_id)
			return HttpResponseRedirect('/admin_view_emp/')
		else:
			emp_id=request.GET['id']
			var=Tbl_Employee.objects.all().filter(id=emp_id)
			cmpny=Tbl_Company.objects.all()
			return render(request,'Admin/admin_edit_emp.html',{'var':var,'emp_id':emp_id,'cmpny':cmpny})
	else:
		return HttpResponseRedirect('/login/')



# Company
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cmpny_home(request):
	if request.session.has_key('id'):
		return render(request,'Company/cmpny_home.html')
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cmpny_profile(request):
	if request.session.has_key('id'):
		myid=request.session['id']
		var=Tbl_Company.objects.all().filter(id=myid)
		return render(request,'Company/cmpny_profile.html',{'var':var})
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cmpny_employee(request):
	if request.session.has_key('id'):
		myid=request.session['id']
		var=Tbl_Employee.objects.all().filter(company=myid)
		return render(request,'Company/cmpny_employee.html',{'var':var})
	else:
		return HttpResponseRedirect('/login/')



# Employee
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def emp_home(request):
	if request.session.has_key('id'):
		return render(request,'Employee/emp_home.html')
	else:
		return HttpResponseRedirect('/login/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def emp_profile(request):
	if request.session.has_key('id'):
		myid=request.session['id']
		var=Tbl_Employee.objects.all().filter(id=myid)
		return render(request,'Employee/emp_profile.html',{'var':var})
	else:
		return HttpResponseRedirect('/login/')