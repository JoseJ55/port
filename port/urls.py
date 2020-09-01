from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('python/', views.python, name='portfolio-python'),
    path('python/python_example_1/', views.python1, name='python-example-1'),
    path('python/python_example_2/', views.python2, name='python-example-2'),
    path('python/python_example_3/', views.python3, name='python-example-3'),
    path('c_plus_plus/', views.c_plus_plus, name='portfolio-c_plus_plus'),
    path('c_plus_plus/cpp_example_1/', views.c_plus_plus1, name='cpp-example-1'),
    path('c_plus_plus/cpp_example_2/', views.c_plus_plus2, name='cpp-example-2'),
    path('c_plus_plus/cpp_example_3/', views.c_plus_plus3, name='cpp-example-3'),
    path('h_t_m_l/', views.h_t_m_l, name='portfolio-h_t_m_l'),
    path('h_t_m_l/html_example_1', views.h_t_m_l1, name='html-example-1'),
    path('h_t_m_l/html_example_2', views.h_t_m_l2, name='html-example-2'),
    path('h_t_m_l/html_example_3', views.h_t_m_l3, name='html-example-3'),
]
