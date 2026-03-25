from delorean import DeLorean

def test_delorean_starts_in_present():
    # Try placing #? on the line below to explore the object in Value Graphs
    car = DeLorean(2.85)  #?
    assert car.in_future is False
    assert car.engine == {"type": "2.85 L"}

def test_delorean_time_travels():
    car = DeLorean(2.85)
    # Try using the Time Travel Debugger on this test
    car.accelerate_to(89)
    assert car.in_future is True

def test_delorean_stays_in_present():
    car = DeLorean(2.85)
    car.accelerate_to(55)
    assert car.in_future is False

def test_delorean_stopped_is_not_future():
    car = DeLorean(2.85)
    # Try clicking Debug code lens and stepping back from the assertion
    car.accelerate_to(0)
    assert car.in_future is False
