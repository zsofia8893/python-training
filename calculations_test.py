# Egy teszteset az egy függvény
# Egy teszteset mindig csak egy dolgot tesztel
# Teszteset neve konvenció szerint a 'test' szóval kezdődik

from calculations import absolute


def test_absolute_with_positive():
    #BDD = Behaviour Driven Develpoment
    #3 részből áll: given - when - then
    #given
    input = 5
    #when
    result = absolute(input)
    #then   a result megegyezik-e az elvárt értékkel
    expected = 5
    assert result == expected

    #Így lehet lefutattani; python -m pytest -v

def test_absolute_with_negative():
    assert absolute(-5) == 5

def test_absolute_with_zero():
    assert absolute (0) == 0