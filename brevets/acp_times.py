"""
Open and close time calculations for ACP-sanctioned brevets.
"""
import arrow

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Calculates the opening time for a control point.
    """
    start_time = arrow.get(brevet_start_time)
    calc_dist = min(control_dist_km, brevet_dist_km)
    
    hours = 0
    if calc_dist <= 200:
        hours = calc_dist / 34
    elif calc_dist <= 400:
        hours = (200 / 34) + ((calc_dist - 200) / 32)
    elif calc_dist <= 600:
        hours = (200 / 34) + (200 / 32) + ((calc_dist - 400) / 30)
    else:
        hours = (200 / 34) + (200 / 32) + (200 / 30) + ((calc_dist - 600) / 28)
        
    return start_time.shift(minutes=round(hours * 60)).isoformat()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Calculates the closing time for a control point.
    """
    start_time = arrow.get(brevet_start_time)
    calc_dist = min(control_dist_km, brevet_dist_km)
    
    if calc_dist == 0:
        return start_time.shift(hours=1).isoformat()
        
    hours = 0
    if calc_dist <= 600:
        hours = calc_dist / 15
    else:
        hours = (600 / 15) + ((calc_dist - 600) / 11.428)
    
    if control_dist_km >= brevet_dist_km:
        finish_times = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}
        hours = finish_times.get(brevet_dist_km, hours)

    return start_time.shift(minutes=round(hours * 60)).isoformat()