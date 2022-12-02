# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by haomjc on Wed May 08 09:54:43 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...

#: the Abaqus Site Guide for up-to-date examples of common tasks in the
#: environment file.
from abaqus import *
from abaqusConstants import *
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup

def stiffness(fileName, ModelName, Youngs_Modulus, Poissions_Ratio, Step_Initial, Step_Minimum, Moment, Shell_Mesh_Size, Cycloid_Mesh_Size, numCpus,numGpus , SaveAs):

    executeOnCaeStartup()
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    Mdb()
    #: 新的模型数据库已创建.
    #: 模型 "Model-1" 已创建.
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    import sys
    sys.path.insert(9, 
        r'd:/SIMULIA/Abaqus/6.14-1/code/python2.7/lib/abaqus_plugins/rsg')
    sys.path.append('C:\\Users\\haomjc\\abaqus_plugins\\_rsgTmpDir')
    mdb.saveAs(pathName='F:/Temp/Cyc_loid1')
    #: 模型数据库已保存到 "F:\Temp\Cyc_loid.cae".
    mdb.save()
    #: 模型数据库已保存到 "F:\Temp\Cyc_loid.cae".
    step = mdb.openStep('F:/Temp/cyc_loid.stp', scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='cycloid-1', geometryFile=step, 
        combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    mdb.models['Model-1'].PartFromGeometryFile(name='cycloid-2', geometryFile=step, 
        bodyNum=2, combine=False, dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['cycloid-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['cycloid-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((210000.0, 0.3), 
        ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['cycloid-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['cycloid-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['cycloid-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['cycloid-2']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['cycloid-2']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['cycloid-1']
    a.Instance(name='cycloid-1-1', part=p, dependent=OFF)
    p = mdb.models['Model-1'].parts['cycloid-2']
    a.Instance(name='cycloid-2-1', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].steps['Step-1'].setValues(initialInc=1e-05, minInc=1e-08)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
        0.1, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    #: 相互作用属性 "IntProp-1" 已创建.
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    mdb.models['Model-1'].ContactStd(name='Int-1', createStepName='Initial')
    mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
        stepName='Initial', useAllstar=ON)
    mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
        stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))
    #: 相互作用 "Int-1" 已创建.
    
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['cycloid-1-1'].edges
    a.ReferencePoint(point=a.instances['cycloid-1-1'].InterestingPoint(
        edge=e1[338], rule=CENTER))
    
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[6], )
    region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['cycloid-2-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
    region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-1')
    mdb.models['Model-1'].Coupling(name='Constraint-1', controlPoint=region1, 
        surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
        localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['cycloid-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#0 #3000000 ]', ), )
    region = a.Set(faces=faces1, name='Set-2')
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
        region=region, localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[6], )
    region = a.Set(referencePoints=refPoints1, name='Set-3')
    mdb.models['Model-1'].Moment(name='Load-1', createStepName='Step-1', 
        region=region, cm1=-400000.0, distributionType=UNIFORM, field='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['cycloid-2-1'], )
    a.seedPartInstance(regions=partInstances, size=4.3, deviationFactor=0.1, 
        minSizeFactor=0.1)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['cycloid-1-1'], )
    a.seedPartInstance(regions=partInstances, size=10.0, deviationFactor=0.1, 
        minSizeFactor=0.1)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['cycloid-1-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
    elemType1 = mesh.ElemType(elemCode=C3D20R)
    elemType2 = mesh.ElemType(elemCode=C3D15)
    elemType3 = mesh.ElemType(elemCode=C3D10)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['cycloid-1-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['cycloid-2-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
    elemType1 = mesh.ElemType(elemCode=C3D20R)
    elemType2 = mesh.ElemType(elemCode=C3D15)
    elemType3 = mesh.ElemType(elemCode=C3D10)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['cycloid-2-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['cycloid-2-1'], )
    a.generateMesh(regions=partInstances)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['cycloid-1-1'], )
    a.generateMesh(regions=partInstances)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
        optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    mdb.Job(name='Job-cycloid', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4, 
        numDomains=4, numGPUs=1)
    mdb.jobs['Job-cyc_loid1'].writeInput(consistencyChecking=OFF)
    #: 作业输入文件已写入到 "Job-cycloid.inp".
    mdb.save()
    #: 模型数据库已保存到 "F:\Temp\Cyc_loid.cae".
