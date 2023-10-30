from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from orgchart.models import Department


def department_tree(request):
    departments = Department.objects.all()

    department_tree = {}

    top_level_departments = []

    for department in departments:
        if not department.parent_department:
            top_level_departments.append(department)
            department_tree[department] = []

    for department in departments:
        if department.parent_department:
            if department.parent_department in department_tree:
                department_tree[department.parent_department].append(department)

    page = request.GET.get("page")
    paginator = Paginator(top_level_departments, 10)  # 10 items per page

    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        departments = paginator.page(1)
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)

    return render(
        request,
        "tree.html",
        {"departments": departments, "department_tree": department_tree},
    )
