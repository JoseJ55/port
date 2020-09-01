from django.shortcuts import render


def home(request):
    return render(request, 'port/home.html')


def c_plus_plus(request):
    return render(request, 'port/c_plus_plus.html')


def c_plus_plus1(request):
    return render(request, 'port/c_plus_plus1.html')


def c_plus_plus2(request):
    return render(request, 'port/c_plus_plus2.html')


def c_plus_plus3(request):
    return render(request, 'port/c_plus_plus3.html')


def python(request):
    return render(request, 'port/python.html')


def python1(request):
    return render(request, 'port/python1.html')


def python2(request):
    return render(request, 'port/python2.html')


def python3(request):
    return render(request, 'port/python3.html')


def h_t_m_l(request):
    return render(request, 'port/h_t_m_l.html')


def h_t_m_l1(request):
    return render(request, 'port/h_t_m_l1.html')


def h_t_m_l2(request):
    return render(request, 'port/h_t_m_l2.html')


def h_t_m_l3(request):
    return render(request, 'port/h_t_m_l3.html')
