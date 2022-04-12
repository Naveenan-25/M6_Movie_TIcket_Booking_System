import unittest

from main import *


def test_movie():
  movie = main()
  assert movie.t_movie() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def test_movie1():
   movie = main()
   assert movie.t_movie() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def test_Screen():
    movie = main()
    assert movie.Screen() == [1,2,3]

def test_Screen1():
        movie = main()
        assert movie.Screen() == [1, 2, 3, 4]

def test_food():
     movie = main()
     assert movie.food() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_food1():
     movie = main()
     assert movie.food() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def test_city():
    movie = main()
    assert movie.city() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_city1():
    movie = main()
    assert movie.city() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def test_timing():
    movie = main()
    assert movie.timing() == [1, 2, 3, 4]

def test_timing1():
    movie = main()
    assert movie.timing() == [1, 2, 3, 4, 5]

def test_theatre():
    movie = main()
    assert movie.Theatre() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_theatre1():
    movie = main()
    assert movie.Theatre() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
