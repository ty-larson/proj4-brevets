import acp_times
import arrow

START_TIME = "2026-01-01T00:00:00+00:00"

def test_start_control():
    # 0km control should open at start and close 1 hour later
    open_t = acp_times.open_time(0, 200, START_TIME)
    close_t = acp_times.close_time(0, 200, START_TIME)
    assert open_t == START_TIME
    assert close_t == arrow.get(START_TIME).shift(hours=1).isoformat()

def test_200_brevet_finish():
    # 200km brevet finish (at 200km) should close at 13:30
    close_t = acp_times.close_time(200, 200, START_TIME)
    assert close_t == arrow.get(START_TIME).shift(hours=13, minutes=30).isoformat()

def test_600_brevet_finish():
    # 600km brevet finish (at 600km) should close at 40:00
    close_t = acp_times.close_time(600, 600, START_TIME)
    assert close_t == arrow.get(START_TIME).shift(hours=40).isoformat()

def test_1000_brevet_open():
    # 1000km control open time (200/34 + 200/32 + 200/30 + 400/28)
    open_t = acp_times.open_time(1000, 1000, START_TIME)
    # Approx 33 hours and 5 minutes
    assert open_t == arrow.get(START_TIME).shift(hours=33, minutes=5).isoformat()

def test_control_exceeds_brevet():
    # If control (205) is past nominal (200), it should use nominal (200) for calculation
    open_200 = acp_times.open_time(200, 200, START_TIME)
    open_205 = acp_times.open_time(205, 200, START_TIME)
    assert open_200 == open_205