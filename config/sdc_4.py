config = dict()

config['servers'] = dict(pumpDriver=dict(host="127.0.0.1", port=13370),
                         pump=dict(host="127.0.0.1", port=13371),
                         autolabDriver=dict(host="127.0.0.1", port=13374),
                         autolab=dict(host="127.0.0.1", port=13375),
                         kadiDriver=dict(host="127.0.0.1", port=13376),
                         kadi=dict(host="127.0.0.1", port=13377),
                         forceDriver=dict(host="127.0.0.1", port=13352),
                         force=dict(host="127.0.0.1", port=13353),
                         orchestrator=dict(host="127.0.0.1", port=13390),
                         langDriver=dict(host="127.0.0.1", port=13382),
                         lang=dict(host="127.0.0.1", port=13391),
                         minipumpDriver=dict(host="127.0.0.1", port=13386),
                         minipump=dict(host="127.0.0.1", port=13385),
                         analysis=dict(host="127.0.0.1", port=13369),
                         measure=dict(host="127.0.0.1", port=13399),
                         ml=dict(host="127.0.0.1", port=13363),
                         microlabDriver=dict(host="127.0.0.1", port=13350),
                         microlab=dict(host="127.0.0.1", port=13351))

config['analysis'] = dict(url= "http://127.0.0.1:13368",
                          cp= {'counter_voltage': 4.7},
                          ocp= {'analysis_points': 10},
                          eis= {'circuit_list': [
                                            "R_0-p(R_1,CPE_1)-CPE_2",
                                            "R_0-p(R_1,CPE_1)-p(R_2,CPE_2)-CPE_3",
                                            "R_0-p(R_1-W_1,CPE_1)",
                                            "R_0-p(R_1,CPE_1)-p(R_2-W_1,CPE_2)",
                                            "R_0-p(R_1,CPE_1)-p(R_2,CPE_2)-p(R_3-W_1,CPE_3)"
                                            ],
                              'guess_list': [
                                            ["R0", "R1", 1e-10, 0.99, 1e-7, 0.8],
                                            ["R0", "R1", 1e-11,0.98, "R2", 4e-7,0.85, 1e-6,0.9],
                                            ["R0", "R1", 1e+5, 1e-6,0.9],
                                            ["R0", "R1", 1e-10,0.98, "R2", 1e+5, 1e-6,0.9],
                                            ["R0", "R1", 1e-10,0.98, "R2", 1e-10,0.98, "R3", 1e+5, 1e-6,0.9]
                                            ],
                              'bounds_list': [
                                            (("R0", "R1", 1e-13, 0.001, 1e-13, 0),("R0", "R1", 1e-5, 0.999, 1e-3, 1)),
                                            (("R0", "R1", 1e-13,0.001, "R2", 1e-13,0.001, 1e-13,0.001),("R0", "R1", 1e-8,1, "R2", 1e-4,1, 1,1)),
                                            (("R0", "R1", 1e-1, 1e-13,0.001),("R0", "R1", 1e+10, 1,1)),
                                            (("R0", "R1", 1e-13,0.001, "R2",1e-1, 1e-13,0.001),("R0", "R1", 1e-6,1, "R2",1e+10, 1,1)),
                                            (("R0", "R1", 1e-13,0.001, "R2", 1e-13,0.001, "R3",1e-1, 1e-13,0.001),("R0", "R1", 1e-6,1, "R2", 1e-6,1, "R3",1e+10, 1,1))
                                            ],
                              'semicircles_max': 3,
                              'metric': 'chi2',
                              'save_path': r'C:\Users\LaborRatte23-2\Documents\GitHub\helao-dev\temp\EIS'}
)

config['ml'] = dict(url="http://127.0.0.1:13362",
                    ternary_labels=("Si", "Ge", "Sn"),
                    ternary_path=r"C:/Users/LaborRatte23-2/Documents/data/substrate_109/AL")

config['measure'] = dict(url="http://127.0.0.1:13398")

config['kadiDriver'] = dict(host=r"https://polis-kadi4mat.iam-cms.kit.edu",
                            PAT=r"")

config['kadi'] = dict(group='2', url="http://127.0.0.1:13376")

config['autolabDriver'] = dict(basep = r"C:\Program Files\Metrohm Autolab\Autolab SDK 1.11",
                    procp = r"C:\Users\LaborRatte23-2\Documents\echemprocedures",
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

config['autolab'] = dict(url="http://127.0.0.1:13374")
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

# coordinates for new sample holder (SEM)
config['lang'] = dict(url="http://127.0.0.1:13382",
                      safe_home_pos=[0.0, 0.0, 0.0],
                        safe_waste_pos=[22.5, -108.0, 0.0],
                        safe_sample_pos=[60.0, -84.5, 0.0],
                        remove_drop=[22.5, -93.0, 7.5],
                        forceurl="http://127.0.0.1:13353")

config['forceDriver'] = dict(com_port=9) # 8 or 9 - both are possible
config['force'] = dict(url="http://127.0.0.1:13352")

config['microlabDriver'] = dict(left=dict(syringe=dict(volume=500000,
                                                flowRate=5000,
                                                initFlowRate=5000)),
                                right=dict(syringe=dict(volume=500000,
                                                flowRate=10000,
                                                initFlowRate=10000)),
                                dllpath=r"C:\Program Files (x86)\Hamilton Company\ML600 Programming Helper Tool")
config['microlab'] = dict(url="http://127.0.0.1:13350",left=dict(valve=dict(prefIn=1,prefOut=3)),right=dict(valve=dict(prefIn=2,prefOut=1)))

config['orchestrator'] = dict(path=r'C:\Users\LaborRatte23-2\Documents\data', kadiurl="http://127.0.0.1:13377")

config['launch'] = dict(server=['autolabDriver', 'kadiDriver', 'langDriver', 'forceDriver', 'microlabDriver'],
                        action=['autolab', 'kadi', 'lang', 'force', 'microlab', 'analysis', 'measure', 'ml'],
                        orchestrator=['orchestrator'],
                        visualizer=['autolab_visualizer'],
                        process=[])

config['instrument'] = "sdc"

config['led'] = dict(port='COM5')
