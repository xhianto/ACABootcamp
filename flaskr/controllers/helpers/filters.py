from ...app import app
from datetime import date

@app.template_filter('calc_age')
def filter_calc_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))