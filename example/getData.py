import pandas as pd
import os


def getData():
    cwd = os.getcwd()
    inputDataPath = os.path.join(cwd, "InputData")
    data = {}

    # Onshore data
    capacityMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Wind', 'maxCapacityOnshore_GW_el.xlsx'),
                                index_col=0, squeeze=True)
    operationRateMax = pd.read_excel(
        os.path.join(inputDataPath, 'SpatialData', 'Wind', 'maxOperationRateOnshore_el.xlsx'))

    data.update({'Wind (onshore), capacityMax': capacityMax})
    data.update({'Wind (onshore), operationRateMax': operationRateMax})

    # Offshore data
    capacityMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Wind', 'maxCapacityOffshore_GW_el.xlsx'),
                                index_col=0, squeeze=True)
    operationRateMax = pd.read_excel(
        os.path.join(inputDataPath, 'SpatialData', 'Wind', 'maxOperationRateOffshore_el.xlsx'))

    data.update({'Wind (offshore), capacityMax': capacityMax})
    data.update({'Wind (offshore), operationRateMax': operationRateMax})

    # PV data
    capacityMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'PV', 'maxCapacityPV_GW_el.xlsx'),
                                index_col=0, squeeze=True)
    operationRateMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'PV', 'maxOperationRatePV_el.xlsx'))

    data.update({'PV, capacityMax': capacityMax})
    data.update({'PV, operationRateMax': operationRateMax})

    # Run of river data
    capacityFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'HydroPower', 'fixCapacityROR_GW_el.xlsx'),
                                index_col=0, squeeze=True)
    operationRateFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'HydroPower',
                                                  'fixOperationRateROR_GW_el.xlsx'))

    data.update({'Existing run-of-river plants, capacityFix': capacityFix})
    data.update({'Existing run-of-river plants, operationRateFix': operationRateFix})

    # Biogas data
    operationRateMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Biogas',
                                                  'biogasPotential_GWh_biogas.xlsx'))

    data.update({'Biogas, operationRateMax': operationRateMax})

    # Natural gas plant data
    capacityMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'NaturalGasPlants',
                                             'existingCombinedCycleGasTurbinePlantsCapacity_GW_el.xlsx'),
                                index_col=0, squeeze=True)

    data.update({'Existing CCGT plants (methane), capacityMax': capacityMax})

    # Hydrogen salt cavern data
    capacityMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'GeologicalStorage',
                                             'existingSaltCavernsCapacity_GWh_methane.xlsx'),
                                index_col=0, squeeze=True) * 3 / 10

    data.update({'Salt caverns (hydrogen), capacityMax': capacityMax})

    # Methane salt cavern data
    capacityMax = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'GeologicalStorage',
                                             'existingSaltCavernsCapacity_GWh_methane.xlsx'),
                                index_col=0, squeeze=True)

    data.update({'Salt caverns (methane), capacityMax': capacityMax})

    # Pumped hydro storage data
    capacityFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'HydroPower',
                                             'fixCapacityPHS_storage_GWh_energyPHS.xlsx'),
                                index_col=0, squeeze=True)

    data.update({'Pumped hydro storage, capacityFix': capacityFix})

    # AC cables data
    capacityFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'ElectricGrid',
                                             'ACcableExistingCapacity_GW_el.xlsx'),
                                index_col=0, header=0)

    data.update({'AC cables, capacityFix': capacityFix})

    # DC cables data
    capacityFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'ElectricGrid',
                                             'DCcableExistingCapacity_GW_el.xlsx'),
                                index_col=0, header=0)
    distances = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'ElectricGrid',
                                           'DCcableLength_km.xlsx'),
                              index_col=0, header=0)
    losses = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'ElectricGrid',
                                        'DCcableLosses.xlsx'),
                           index_col=0, header=0)

    data.update({'DC cables, capacityFix': capacityFix})
    data.update({'DC cables, distances': distances})
    data.update({'DC cables, losses': losses})

    # Pipelines data
    eligibility = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Pipelines',
                                             'pipelineIncidence.xlsx'), index_col=0, header=0)
    distances = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Pipelines', 'pipelineIncidence.xlsx'),
                              index_col=0, header=0)

    data.update({'Pipelines, eligibility': eligibility})
    data.update({'Pipelines, distances': distances})

    # Electricity demand data
    operationRateFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Demands',
                                                  'electricityDemand_GWh_el.xlsx'))

    data.update({'Electricity demand, operationRateFix': operationRateFix})

    # Hydrogen demand data
    operationRateFix = pd.read_excel(os.path.join(inputDataPath, 'SpatialData', 'Demands',
                                                  'hydrogenDemand_GWh_hydrogen.xlsx'))

    data.update({'Hydrogen demand, operationRateFix': operationRateFix})

    return data
