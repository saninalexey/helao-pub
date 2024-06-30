config = dict()

config['servers'] = dict(psdDriver=dict(host="127.0.0.1", port=13370),
                         psd=dict(host="127.0.0.1", port=13371),
                         palmsensDriver=dict(host="127.0.0.1", port=13374),
                         palmsens=dict(host="127.0.0.1", port=13375),
                         forceDriver=dict(host="127.0.0.1", port=13352),
                         force=dict(host="127.0.0.1", port=13353),
                         orchestrator=dict(host="127.0.0.1", port=13390),
                         dobotDriver=dict(host="127.0.0.1", port=13382),
                         dobot=dict(host="127.0.0.1", port=13391),
                         analysis=dict(host="127.0.0.1", port=13389),
                         measure=dict(host="127.0.0.1", port=13399),
                         ml=dict(host="127.0.0.1", port=13363))

#config['measure:1'] = dict(url="http://192.168.31.123:6667")
#config['measure:2'] = dict(url="http://192.168.31.114:6669")
config['analysis'] = dict(url="http://127.0.0.1:13368")
config['ml'] = dict(url="http://127.0.0.1:13362")
config['measure'] = dict(url="http://127.0.0.1:13398")

#config['pumpDriver'] = dict(port='COM4', baud=9600, timeout=0.1, pumpAddr={
#                            i: i + 21 for i in range(14)})  # numbering is left to right top to bottom
#config['pumpDriver']['pumpAddr'].update({i: i for i in range(20, 35)})
#config['pumpDriver']['pumpAddr']['all'] = 20

#config['pump'] = dict(url="http://127.0.0.1:13370")

config['palmsensDriver'] = dict(PalmsensSDK_python = r"C:\Users\juliu\Documents\PSPythonSDK",
                                savepath_raw = r"C:\Users\juliu\helao-dev\temp\palmsens_data",
                                log_folder = r"C:\Users\juliu\helao-dev\temp\palmsens_data\log")

config['palmsens'] = dict(url="http://127.0.0.1:13374")

config['autolabDriver'] = dict(basep = r"C:\Program Files\Metrohm Autolab\Autolab SDK 1.11",
                    procp = r"C:\Users\LaborRatte23-2\Documents\echemprocedures",
                    #hwsetupf = r"C:\ProgramData\Metrohm Autolab\12.0\HardwareSetup.AUT88172.xml",
                    hwsetupf = r"C:\ProgramData\Metrohm Autolab\12.0\HardwareSetup.AUT88172.xml",
                    micsetupf = r"C:\Program Files\Metrohm Autolab\Autolab SDK 1.11\Hardware Setup Files\Adk.bin",
                    proceuduresd = {'cp': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\CP.nox',      
                                    'ca': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\CA.nox',
                                    'cv': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\CV.nox',
                                    'lsv': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\LSV.nox',
                                    'eis': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\EIS.nox',
                                    'eis_fast': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\EIS_fast.nox',
                                    'peis_lissajous': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\PEIS_Lissajous.nox',
                                    'ocp': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\ocp_signal.nox',
                                    'on': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\ON.nox',
                                    'off': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\OFF.nox', 
                                    'ocp_rf': r"C:\Users\LaborRatte23-2\Documents\echemprocedures\ocp_rf_v12.nox",
                                    'ms': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\mott_schotky_no_osc.nox',
                                    'cv_ocp':r"C:\Users\LaborRatte23-2\Documents\echemprocedures\CV@OCP.nox",
                                    'gcpl':r"C:\Users\LaborRatte23-2\Documents\echemprocedures\GCPL_n.nox",
                                    'cv_pot':r"C:\Users\LaborRatte23-2\Documents\echemprocedures\CV_Potentiostatic.nox",
                                    'gcpl_fc':r"C:\Users\LaborRatte23-2\Documents\echemprocedures\GCPL_Fc.nox",
                                    'gdpl_fc':r"C:\Users\LaborRatte23-2\Documents\echemprocedures\GDPL_Fc.nox",
                                    'ocp_rs':r"C:\Users\LaborRatte23-2\Documents\echemprocedures\OCP_rs.nox",
                                    'charge': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\CP_charge.nox',
                                    'discharge': r'C:\Users\LaborRatte23-2\Documents\echemprocedures\CP_discharge.nox'})

config['autolab'] = dict(url="http://127.0.0.1:13376")
config['autolab']['procedures'] = {}

config['autolab']['procedures']['ca'] = {'procedure': 'ca',
                                               'setpoints': {'applypotential': {'Setpoint value': 0.735},
                                                             'recordsignal': {'Duration': 1000}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'ca.nox',
                                               'parseinstructions': ['recordsignal']}

config['autolab']['procedures']['cccv'] = {'setpointsjson':{'FHSetSetpointCurrent': {'Setpoint value': 1e-06}}}

config['autolab']['procedures']['ocp'] = {'procedure': 'ocp',
                                                'setpoints': {'FHLevel': {'Duration': 20}},
                                                'plot': 'tCV',
                                                'onoffafter': 'off',
                                                'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                                'filename': 'ocp.nox',
                                                'parseinstructions': ['FHLevel']}

config['autolab']['procedures']['ms'] = {'procedure': 'ms',
                                               # 'setpoints': {'ExecCommandForeach': 'FIAMeasPotentiostatic': {} },
                                               'setpoints': {'FHSetSetpointPotential': {'Setpoint value': 0.01}},
                                               'plot': 'impedance',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'ms.nox',
                                               'parseinstructions': ["FIAMeasurement", "FHLevel"]}


config['autolab']['procedures']['ocp_rf'] = {'procedure': 'ocp_rf',
                                                   'setpoints': {'FHRefDetermination': {'Timeout': 20}},
                                                   'plot': 'tCV',
                                                   'onoffafter': 'off',
                                                   'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                                   'filename': 'ocp_rf.nox',
                                                   'parseinstructions': ['OCP determination']}


config['autolab']['procedures']['cp'] = {'procedure': 'cp',
                                               'setpoints': {'applycurrent': {'Setpoint value': 7*(10**-6)},
                                                             'recordsignal': {'Duration': 600}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'cp.nox',
                                               'parseinstructions': ['recordsignal']}

config['autolab']['procedures']['gcpl'] = {'procedure': 'gcpl',
                                               'setpoints': {
                                                    'FHWait': {'Time': 10},
                                                    'ExecCommandRepeatCount': {'NrOfRepeats': 10},
                                                    'FHSetSetpointCurrent': {'Setpoint value': 1e-07},
                                                    'FHLevelGalvanostatic': {'Interval time in µs': 0.5,
                                                                             'Duration': 18000},
                                                    'FHSetSetpointCurrent': {'Setpoint value': -1e-07},
                                                    'FHLevelGalvanostatic': {'Interval time in µs': 0.5,
                                                                             'Duration': 18000}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev_2\temp",
                                               'filename': 'gcpl.nox',
                                               'parseinstructions': ['FHLevelGalvanostatic']}

config['autolab']['procedures']['gcpl_fc'] = {'procedure': 'gcpl_fc',
                                               'setpoints':
                                                    {'applycurrent': {'Setpoint value': 1e-06},
                                                     'recordsignal': {'Duration': 60,
                                                                     'Interval time in µs': 0.5}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev_2\temp",
                                               'filename': 'gcpl_fc.nox',
                                               'parseinstructions': ['recordsignal']}

config['autolab']['procedures']['ocp_rs'] = {'procedure': 'ocp_rs',
                                               'setpoints':
                                                    {'recordsignal': {'Duration': 60,
                                                                     'Interval time in µs': 0.5}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev_2\temp",
                                               'filename': 'ocp_rs.nox',
                                               'parseinstructions': ['recordsignal']}

config['autolab']['procedures']['cv'] = {'procedure': 'cv',
                                               'setpoints': {
                                                   'FHSetSetpointPotential': {'Setpoint value': 0.4},
                                                   'FHWait': {'Time': 2},
                                                   'CVLinearScanAdc164': {'StartValue': 0.4,
                                                                          'UpperVertex': 1.5,
                                                                          'LowerVertex': 0.399,
                                                                          'NumberOfStopCrossings': 50,
                                                                          'ScanRate': 0.02}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'cv.nox',
                                               'parseinstructions': ['CVLinearScanAdc164']}

config['autolab']['procedures']['lsw'] = {'procedure': 'lsw',
                                               'setpoints': {
                                                   'FHSetSetpointPotential': {'Setpoint value': 0.4},
                                                   'FHWait': {'Time': 2},
                                                   'FHLinearSweep': {'Start value': 0.4,
                                                                          'Step': 1.5,
                                                                          'Stop value': 0.399,
                                                                          'Scanrate': 0.02}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'cv.nox',
                                               'parseinstructions': ['CVLinearScanAdc164']}

config['autolab']['procedures']['cv_pot'] = {'procedure': 'cv_pot',
                                               'setpoints': {
                                                   'FHWait': {'Time': 5},
                                                   'FHCyclicVoltammetry2': {'Upper vertex': 0.75,
                                                                          'Lower vertex': -0.50,
                                                                          'Step': 0.004,
                                                                          'NrOfStopCrossings': 10,
                                                                          'Scanrate': 0.020}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'cv_pot.nox',
                                               'parseinstructions': ['FHCyclicVoltammetry2']}

config['autolab']['procedures']['cv_ocp'] = {'procedure': 'cv_ocp',
                                               'setpoints': {
                                                   'FHRefDetermination': {'Timeout': 30},
                                                   'FHWait': {'Time': 5},
                                                   'FHCyclicVoltammetry2': {'Upper vertex': 0.75,
                                                                          'Lower vertex': -0.50,
                                                                          'Step': 0.004,
                                                                          'NrOfStopCrossings': 10,
                                                                          'Scanrate': 0.020}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'cv.nox',
                                               'parseinstructions': ['FHCyclicVoltammetry2']}

config['autolab']['procedures']['eis'] = {'procedure': 'eis',
                                                'setpoints': {'FHSetSetpointPotential': {'Setpoint value': 0.01}},
                                                'plot': 'impedance',
                                                'onoffafter': 'off',
                                                'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                                'filename': 'eis.nox',
                                                'parseinstructions': ['FIAMeasPotentiostatic']}

config['autolab']['procedures']['eis_fast'] = {'procedure': 'eis_fast',
                                                'setpoints': {'FHSetSetpointPotential': {'Setpoint value': 0.01}},
                                                'plot': 'impedance',
                                                'onoffafter': 'off',
                                                'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                                'filename': 'eis_cp.nox',
                                                'parseinstructions': ['FIAMeasPotentiostatic']}

config['autolab']['procedures']['eis_ocp'] = {'procedure': 'eis_ocp',
                                                'setpoints': {'FHRefDetermination': {'Timeout': 30}},
                                                'plot': 'impedance',
                                                'onoffafter': 'off',
                                                'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                                'filename': 'eis_ocp_test.nox',
                                                'parseinstructions': ['FIAMeasPotentiostatic']}

config['autolab']['procedures']['peis_lissajous'] = {'procedure': 'peis_lissajous',
                                                'setpoints': {'FHSetSetpointPotential': {'Setpoint value': 0.01}},
                                                'plot': 'impedance',
                                                'onoffafter': 'off',
                                                'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                                'filename': 'peis_lissajous.nox',
                                                'parseinstructions': ['FIAMeasPotentiostatic']}                                                

config['autolab']['procedures']['pitt'] = {'procedure': 'pitt',
                                                 'setpoints': {
                                                     'OCP determination': {'Timeout': 60},
                                                     # charge loop range list list(proc.Commands['Charge loop'].CommandParameters['Values'].Value.RangeCollection)
                                                     'Charge pulse': {'Duration': 600},
                                                     'Charge relaxation': {'Duration': 600},
                                                     'Discharge pulse': {'Duration': 600},
                                                     'Discharge relaxation': {'Duration': 600},
                                                     'Export ASCII data': {'Filename': r'C:\Users\LaborRatte_23_3\Documents\My Procedures 1.11\pitt.txt'}},
                                                 'plot': 'impedance',
                                                 'onoffafter': 'off',
                                                 'safepath': r"C:\Users\SDC_1\Documents\Github\helao-dev\temp",
                                                 'filename': 'eis.nox',
                                                 'parseinstructions': ['FIAMeasPotentiostatic']}

config['autolab']['procedures']['gitt'] = {'procedure': 'gitt',
                                                 'setpoints': {
                                                     # 1=10A, 0=1A, -1=100mA, -2=10mA, -3=1mA, -4=100uA, -5=10uA, -6=1uA, -7=100nA, -8=10nA
                                                     'Autolab control': {'WE(1).Current range': -2},
                                                     'OCP determination': {'Timeout': 10},
                                                     'Charge loop': {'Number of repetitions': 78},
                                                     'Set charge current': {'Current (A)': 0.005},
                                                     # cutoff is missing
                                                     'Charge pulse': {'Duration': 600},
                                                     'Charge relaxation': {'Duration': 600},
                                                     'Discharge loop': {'Number of repetitions': 78},
                                                     'Set charge current': {'Current (A)': -0.005},
                                                     # cutoff is missing
                                                     'Discharge pulse': {'Duration': 600},
                                                     'Discharge relaxation': {'Duration': 600},
                                                     'Export ASCII data': {'Filename': r'C:\Users\LaborRatte_23_3\Documents\My Procedures 1.11\pitt.txt'}},
                                                 'plot': 'impedance',
                                                 'onoffafter': 'off',
                                                 'safepath': r"C:\Users\SDC_1\Documents\Github\helao-dev\temp",
                                                 'filename': 'eis.nox',
                                                 'parseinstructions': ['FIAMeasPotentiostatic']}

config['autolab']['procedures']['gitt_eis'] = {'procedure': 'gitt_eis',
                                                     'setpoints': {
                                                         # 1=10A, 0=1A, -1=100mA, -2=10mA, -3=1mA, -4=100uA, -5=10uA, -6=1uA, -7=100nA, -8=10nA
                                                         'Autolab control 1': {'WE(1).Current range': -2},
                                                         'OCP determination 1': {'Timeout': 30},
                                                         'Charge loop': {'Number of repetitions': 78},
                                                         'Charge current': {'Current (A)': 0.005},
                                                         # cutoff is missing
                                                         'Charge pulse': {'Duration': 600},
                                                         'Charge relaxation': {'Duration': 600},
                                                         'OCP determination 2': {'Timeout': 30},
                                                         # FRA measurement settings
                                                         'Discharge loop': {'Number of repetitions': 78},
                                                         'Discharge current': {'Current (A)': -0.005},
                                                         # cutoff is missing
                                                         'Discharge pulse': {'Duration': 600},
                                                         'Discharge relaxation': {'Duration': 600},
                                                         'OCP determination 3': {'Timeout': 30},
                                                         # FRA measurement settings
                                                         'Export ASCII data': {'Filename': r'C:\Users\LaborRatte_23_3\Documents\My Procedures 1.11\pitt.txt'}},
                                                     'plot': 'impedance',
                                                     'onoffafter': 'off',
                                                     'safepath': r"C:\Users\SDC_1\Documents\Github\helao-dev\temp",
                                                     'filename': 'eis.nox',
                                                     'parseinstructions': ['FIAMeasPotentiostatic']}


#config['autolab']['procedures']['charge'] = {'procedure': 'charge',
#                                               'setpoints': {'applycurrent': {'Setpoint value': 10**-6},
#                                                             'recordsignal': {'Duration': 3600}},
#                                               'plot': 'tCV',
#                                               'onoffafter': 'off',
#                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
#                                               'filename': 'cp_charge.nox',
#                                               'parseinstructions': ['recordsignal']}

config['autolab']['procedures']['charge'] = {'procedure': 'charge',
                                                # 1=10A, 0=1A, -1=100mA, -2=10mA, -3=1mA, -4=100uA, -5=10uA, -6=1uA, -7=100nA, -8=10nA
                                               'setpoints': {'Autolab control': {'WE(1).Current range': -5},
                                                             'applycurrent': {'Setpoint value': 10**-6},
                                                             'recordsignal': {'Duration': 3600}},
                                               'plot': 'tCV',
                                               'onoffafter': 'off',
                                               'safepath': r"C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp",
                                               'filename': 'cp_charge.nox',
                                               'parseinstructions': ['recordsignal']}

config['langDriver'] = dict(vx=5, vy=5, vz=5, port='COM3',
                            dll=r"C:\Users\LaborRatte23-2\Documents\git\pyLang\LStepAPI\_C#_VB.net\CClassLStep64",
                            dllconfig=r"C:\Users\LaborRatte23-2\Documents\git\pyLang\config.LSControl",
                            )


# old sample holder
#config['lang'] = dict(url="http://127.0.0.1:13382",
#                      safe_home_pos=[0.0, 0.0, 0.0],
#                        # 0.0, 0.0, 0.0
#                        safe_waste_pos=[42.5, -108.0, 0.0], #46.5, -108, 0
#                        safe_sample_pos=[-5.5, -89.0, 0.0], #-5.5, -89, 0
#                        remove_drop=[42.5, -93.0, 7.5], #46.5, -94.0, 8.0
#                        forceurl="http://127.0.0.1:13379")

# new sample holder (SEM)
config['lang'] = dict(url="http://127.0.0.1:13382",
                      safe_home_pos=[0.0, 0.0, 0.0],
                        safe_waste_pos=[22.5, -108.0, 0.0],
                        safe_sample_pos=[60.0, -84.5, 0.0],
                        # 59.5, -84.5, 0.0 for old wafer Si
                        # 72.0, -10.0, 0.0 # for FTO
                        # 94.0, -19.0, 0.0 # for SEM_yx
                        # 62.0, -83.0, 0.0 # for SEM_xy
                        remove_drop=[22.5, -93.0, 7.5],
                        forceurl="http://127.0.0.1:13353")

config['dobotDriver'] = {
    "api_path": r"C:\Users\juliu\Documents\RobotRecording\include",
    "ip": "192.168.1.6",
    "dashboard_port": 29999,
    "move_port": 30003,
    "error_codes": r"C:\Users\juliu\Documents\RobotRecording\data\error_codes.json",
    "number_of_joints": 4,
    "end_effector": 2,
    "end_effector_pins": {
        "power":5,
        "direction": 10},
    "end_effector_state": 1,
    "joint_acceleration": 3,
    "linear_acceleration": 3,
    "joint_bounds": [[-80, 80], [-125, 125], [95, 245], [-355, 355]] 
}


config["dobot"] = {
    "url": "http://127.0.0.1:13382",
    "safe_home_pose": [371.2, -2.5, 140, 327.5],
    "safe_waste_pose": [355.0, -2.5, 112.0, 327.5],
    "safe_sample_pose": [271.3, -27.8, 115, 327.5],
    "remove_drop_pose": [371.2, -2.5, 108.25, 327.5],
    "forceurl":"http://127.0.0.1:13353"
}

#config['forcesdcDriver'] = dict(port=7,buffer_size=1,
#                             dll_address=r"C:\Users\LaborRatte23-2\Desktop\megsv\megsv_x64\MEGSV.dll")

config['forceDriver'] = dict(com_port=5)
config['force'] = dict(url="http://127.0.0.1:13352")

#config['minipumpDriver'] = dict(port='COM4', baud=1200, timeout=1)
#config['minipump'] = dict(url="http://127.0.0.1:13386") #127.0.0.1", port=13386

config['hamiltonDriver'] = dict(left=dict(syringe=dict(volume=500000,
                                                flowRate=5000,
                                                initFlowRate=5000)),
                                right=dict(syringe=dict(volume=500000,
                                                flowRate=10000,
                                                initFlowRate=10000)),
                                dllpath=r"C:\Program Files (x86)\Hamilton Company\ML600 Programming Helper Tool")
config['hamilton'] = dict(url="http://127.0.0.1:13350",left=dict(valve=dict(prefIn=1,prefOut=3)),right=dict(valve=dict(prefIn=2,prefOut=1)))
#10000000, 200000

config['psdDriver'] = dict(port=6, baud=9600, psd_type = '4', psd_syringe = '1.25m', speed = 10) #PSD.PSDTypes.psd4.value, PSD.SyringeTypes.syringe125mL.value

config['psd'] = dict(url="http://127.0.0.1:13370", valve = {'S1': 2, 'S2': 3, 'S3': 4, 'S4': 5, 'S5': 6, 'S6': 7, 'Out': 1, 'Mix': 8}, volume = 1250, speed = 10) # volume of the pump corresponds to the type, input in µL
config['orchestrator'] = dict(path=r'C:\Users\juliu\data', kadiurl="http://127.0.0.1:13377")

config['launch'] = dict(server=['dobotDriver', 'forceDriver', 'palmsensDriver', 'psdDriver'],
                        action=['dobot', 'force', 'palmsens', 'psd', 'analysis', 'measure', 'ml'],
                        orchestrator=['orchestrator'],
                        visualizer=[],
                        process=['plot_process'])

config['instrument'] = "sdc"

