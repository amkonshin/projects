#import h2o
import pandas as pd


def map_for_dict_Gender(Gender):
    dict_Gender = {'Male': 0, 'Female': 1}
    res = dict_Gender.get(Gender)
    return res


def map_for_dict_MariStat(MariStat):
    dict_MariStat = {'Other': 0, 'Alone': 1}
    res = dict_MariStat.get(MariStat)
    return res


def f_VehUsage_Professional(VehUsage):
    if VehUsage == 'Professional':
        VehUsage_Professional = 1
    else:
        VehUsage_Professional = 0
    return VehUsage_Professional


def f_VehUsage_Private_trip_to_office(VehUsage):
    if VehUsage == 'Private+trip to office':
        VehUsage_Private_trip_to_office = 1
    else:
        VehUsage_Private_trip_to_office = 0
    return VehUsage_Private_trip_to_office


def f_VehUsage_Private(VehUsage):
    if VehUsage == 'Private':
        VehUsage_Private = 1
    else:
        VehUsage_Private = 0
    return VehUsage_Private


def f_VehUsage_Professional_run(VehUsage):
    if VehUsage == 'Professional run':
        VehUsage_Professional_run = 1
    else:
        VehUsage_Professional_run = 0
    return VehUsage_Professional_run

def transform_exp(exp):
    if exp < 0:
        exp_f = None
    elif exp > 52:
        exp_f = 52
    return exp_f
def driver_min_age_m(age,gender):
    return age if gender==0 else 18
def driver_min_age_f(age,gender):
    return age if gender==1 else 18

def return_NewDF():
    columns = [
        'driver_minexp',
        'Gender',
        'MariStat',
        'HasKmLimit',
        'BonusMalus',
        'OutUseNb',
        'RiskArea',
        'driver_minage_m',
        'driver_minage_f',
        'driver_minage_m_2',
        'driver_minage_f_2',
        'VehUsg_Private',
        'VehUsg_Private+trip to office',
        'VehUsg_Professional',
        'VehUsg_Professional run',
        'CSP1',
        'CSP2',
        'CSP3',
        'CSP6',
        'CSP7'
    ]
    return pd.DataFrame(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        columns=columns)

def process_input(json_input):
    LicAge = transform_exp(json_input["LicAge"])
    Gender = map_for_dict_Gender(json_input["Gender"])
    MariStat = map_for_dict_MariStat(json_input["MariStat"])

    HasKmLimit = json_input["HasKmLimit"]
    BonusMalus = json_input["BonusMalus"]
    OutUseNb = json_input["OutUseNb"]
    RiskArea = json_input["RiskArea"]
    DrivAge = json_input["DrivAge"]
    d_minage_m=driver_min_age_m(json_input["DrivAge"],json_input["Gender"])
    d_minage_f = driver_min_age_f(json_input["DrivAge"],json_input["Gender"])
    VehUsg_Private = f_VehUsage_Private(json_input["VehUsage"])
    VehUsg_Private_trip_to_office = f_VehUsage_Private_trip_to_office(json_input["VehUsage"])
    VehUsg_Professional = f_VehUsage_Professional(json_input["VehUsage"])
    VehUsg_Professional_run = f_VehUsage_Professional_run(json_input["VehUsage"])

    CSP1 = 0
    CSP2 = 0
    CSP3 = 0
    CSP6 = 0
    CSP7 = 0


    hf = return_NewDF()

    hf[0, 'driver_minexp'] = LicAge
    hf[0, 'Gender'] = Gender
    hf[0, 'MariStat'] = MariStat
    hf[0, 'HasKmLimit'] = HasKmLimit
    hf[0, 'BonusMalus'] = BonusMalus
    hf[0, 'OutUseNb'] = OutUseNb
    hf[0, 'RiskArea'] = RiskArea
    hf[0, 'driver_minage_m'] = d_minage_m
    hf[0, 'driver_minage_f'] = d_minage_f
    hf[0, 'driver_minage_m_2'] = d_minage_m**2
    hf[0, 'driver_minage_f_2'] = d_minage_f**2
    hf[0, 'VehUsg_Private'] = VehUsg_Private
    hf[0, 'VehUsg_Private+trip to office'] = VehUsg_Private_trip_to_office
    hf[0, 'VehUsg_Professional'] = VehUsg_Professional
    hf[0, 'VehUsg_Professional run'] = VehUsg_Professional_run
    hf[0, 'CSP1'] = CSP1
    hf[0, 'CSP2'] = CSP2
    hf[0, 'CSP3'] = CSP3
    hf[0, 'CSP6'] = CSP6
    hf[0, 'CSP7'] = CSP7

    return hf
