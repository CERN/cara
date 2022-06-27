import tornado.web

# ------------------ Translation ----------------------

_ = tornado.locale.get().translate

# ------------------ Default form values ----------------------

# Used to declare when an attribute of a class must have a value provided, and
# there should be no default value used.
_NO_DEFAULT = object()
_DEFAULT_MC_SAMPLE_SIZE = 250_000
# The calculator version is based on a combination of the model version and the
# semantic version of the calculator itself. The version uses the terms
# "{MAJOR}.{MINOR}.{PATCH}" to describe the 3 distinct numbers constituting a version.
# Effectively, if the model increases its MAJOR version then so too should this
# calculator version. If the calculator needs to make breaking changes (e.g. change
# form attributes) then it can also increase its MAJOR version without needing to
# increase the overall CARA version (found at ``cara.__version__``).
__version__ = "4.2"
_DEFAULTS = {
    'activity_type': 'office',
    'air_changes': 0.,
    'air_supply': 0.,
    'calculator_version': _NO_DEFAULT,
    'ceiling_height': 0.,
    'exposed_coffee_break_option': 'coffee_break_0',
    'exposed_coffee_duration': 5,
    'exposed_finish': '17:30',
    'exposed_lunch_finish': '13:30',
    'exposed_lunch_option': True,
    'exposed_lunch_start': '12:30',
    'exposed_start': '08:30',
    'event_month': 'January',
    'floor_area': 0.,
    'hepa_amount': 0.,
    'hepa_option': False,
    'humidity': '',
    'infected_coffee_break_option': 'coffee_break_0',
    'infected_coffee_duration': 5,
    'infected_dont_have_breaks_with_exposed': False,
    'infected_finish': '17:30',
    'infected_lunch_finish': '13:30',
    'infected_lunch_option': True,
    'infected_lunch_start': '12:30',
    'infected_people': _NO_DEFAULT,
    'infected_start': '08:30',
    'inside_temp': 293.,
    'location_latitude': _NO_DEFAULT,
    'location_longitude': _NO_DEFAULT,
    'location_name': _NO_DEFAULT,
    'mask_type': 'Type I',
    'mask_wearing_option': 'mask_off',
    'mechanical_ventilation_type': 'not-applicable',
    'opening_distance': 0.,
    'room_heating_option': False,
    'room_number': _NO_DEFAULT,
    'room_volume': 0.,
    'simulation_name': _NO_DEFAULT,
    'total_people': _NO_DEFAULT,
    'ventilation_type': 'no_ventilation',
    'virus_type': 'SARS_CoV_2',
    'volume_type': _NO_DEFAULT,
    'window_type': 'window_sliding',
    'window_height': 0.,
    'window_width': 0.,
    'windows_duration': 0.,
    'windows_frequency': 0.,
    'windows_number': 0,
    'window_opening_regime': 'windows_open_permanently',
    'short_range_option': 'short_range_no',
    'short_range_interactions': '[]',
}

# ------------------ Activities ----------------------

# ACTIVITY_TYPES = [
#     {'name:': 'office', 'activity': 'Seated', 'expiration': {'Speaking': 1, 'Breathing': 2}}, # Mostly silent in the office, but 1/3rd of time speaking.
#     {'name:': 'smallmeeting', 'activity': 'Seated', 'expiration': {'Speaking': 1, 'Breathing': 2}}, #self.total_people - 1}}, # Conversation of N people is approximately 1/N% of the time speaking.
#     {'name:': 'largemeeting', 'activity': 'Standing', 'expiration': {'Speaking': 1, 'Breathing': 2}}, # each infected person spends 1/3 of time speaking.
#     {'name:': 'training', 'activity': 'Standing', 'expiration': 'Speaking'},
#     {'name:': 'callcentre', 'activity': 'Seated', 'expiration': 'Speaking'},
#     {'name:': 'controlroom-day', 'activity': 'Seated', 'expiration': {'Speaking': 1, 'Breathing': 1}}, # Daytime control room shift, 50% speaking.
#     {'name:': 'controlroom-night', 'activity': 'Seated', 'expiration': {'Speaking': 1, 'Breathing': 9}}, # Nightshift control room, 10% speaking.
#     {'name:': 'library', 'activity': 'Seated', 'expiration': 'Breathing'}, 
#     {'name:': 'workshop', 'activity': 'Moderate activity', 'expiration': {'Speaking': 1, 'Breathing': 1}}, #Model 1/2 of time spent speaking in a workshop.
#     {'name:': 'lab', 'activity': 'Light activity', 'expiration': {'Speaking': 1, 'Breathing': 1}}, #Model 1/2 of time spent speaking in a lab.
#     {'name:': 'gym', 'activity': 'Heavy exercise', 'expiration': 'Breathing'}]
ACTIVITY_TYPES = {'office', 'smallmeeting', 'largemeeting', 'training', 'callcentre', 'controlroom-day', 'controlroom-night', 'library', 'workshop', 'lab', 'gym'}

# ------------------ Validation ----------------------

MECHANICAL_VENTILATION_TYPES = {'mech_type_air_changes', 'mech_type_air_supply', 'not-applicable'}
MASK_TYPES = {'Type I', 'FFP2'}
MASK_WEARING_OPTIONS = {'mask_on', 'mask_off'}
VENTILATION_TYPES = {'natural_ventilation', 'mechanical_ventilation', 'no_ventilation'}
VIRUS_TYPES = {'SARS_CoV_2', 'SARS_CoV_2_ALPHA', 'SARS_CoV_2_BETA','SARS_CoV_2_GAMMA', 'SARS_CoV_2_DELTA', 'SARS_CoV_2_OMICRON'}
VOLUME_TYPES = {'room_volume_explicit', 'room_volume_from_dimensions'}
WINDOWS_OPENING_REGIMES = {'windows_open_permanently', 'windows_open_periodically', 'not-applicable'}
WINDOWS_TYPES = {'window_sliding', 'window_hinged', 'not-applicable'}
COFFEE_OPTIONS_INT = {'coffee_break_0': 0, 'coffee_break_1': 1, 'coffee_break_2': 2, 'coffee_break_4': 4}

MONTH_NAMES = {
    'January' : _('January'), 'February' : _('February'), 'March' : _('March'), 'April' : _('April'), 'May' : _('May'), 'June' :_('June'), 'July' : _('July'),
    'August' : _('August'), 'September' : _('September'), 'October': _('October'), 'November' : _('November'), 'December' : _('December'),
}