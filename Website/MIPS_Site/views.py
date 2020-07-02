from django.shortcuts import render

# Create your views here.

# HOME------------------>
def home(request):
	return render(request,'home.html',{})

#DOCUMENTATIONS------------------>

def ViewDoc(request):
	return render(request,'Documentation_MIPS.html',{})

def ViewDoc1(request):
	return render(request,'Documentation_MIPS1.html',{})

def ViewDoc2(request):
	return render(request,'Documentation_MIPS2.html',{})

def ViewDoc3(request):
	return render(request,'Documentation_MIPS3.html',{})

#PROJECT REPORT------------------>

def ProjectReport(request):
	return render(request,'Project_Report.html',{})

# SCREENSHOTS------------------>

def Working(request):
	return render(request,'Working.html',{})

