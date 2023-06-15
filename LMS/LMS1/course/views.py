# from django.shortcuts import render,redirect
# from models import Course
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from django.contrib import messages 
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # Create your views here.
# @APIView
# def VIEW_COURSE(APIView):
#     permission_classes = (IsAuthenticated,)
#     course = Course.objects.all()
#     context = {
#         'course':course,
#     }
#     return render('course/course.html',context)


# def EDIT_COURSE(request,id):
#     course=Course.objects.get(id=id)

#     context ={
#         'course':course
#     }
#     return render(request,'manager/edit_course.html',context)


# def UPDATE_COURSE(request):
#     return render(request,'manager/edit_course.html')



# def DELETE_COURSE(request,id):
#     course_id = id
#     course=Course.objects.get(id=id)
#     course.delete()
#     messages.success(request,'Record is successfully deleted')
#     return redirect('view_course')