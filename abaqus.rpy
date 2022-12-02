# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by haomjc on Wed May 08 09:54:43 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
#: Abaqus Error: 
#: This error may have occurred due to a change to the Abaqus Scripting
#: Interface. Please see the Abaqus Scripting Manual for the details of
#: these changes. Also see the "Example environment files" section of 
#: the Abaqus Site Guide for up-to-date examples of common tasks in the
#: environment file.
#: Execution of "onCaeGraphicsStartup()" in the site directory failed.
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=332.25, 
    height=134.736663818359)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
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
mdb.saveAs(pathName='F:/Temp/Cyc_loid')
#: 模型数据库已保存到 "F:\Temp\Cyc_loid.cae".
mdb.save()
#: 模型数据库已保存到 "F:\Temp\Cyc_loid.cae".
step = mdb.openStep('F:/Temp/cycloid.stp', scaleFromFile=OFF)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=551.461, 
    farPlane=919.824, width=182.392, height=70.4104, viewOffsetX=6.86613, 
    viewOffsetY=0.5725)
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.484, 
    farPlane=906.2, width=189.015, height=72.967, cameraPosition=(462.432, 
    -534.238, -229.513), cameraUpVector=(-0.926244, -0.186004, -0.327833), 
    cameraTarget=(11.226, 2.59586, -7.26707), viewOffsetX=7.11545, 
    viewOffsetY=0.593288)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['cycloid-1-1'].edges
a.ReferencePoint(point=a.instances['cycloid-1-1'].InterestingPoint(
    edge=e1[338], rule=CENTER))
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.082, 
    farPlane=906.991, width=188.882, height=72.9157, cameraPosition=(-476.591, 
    -496.191, 258.204), cameraUpVector=(-0.431209, 0.545735, -0.718493), 
    cameraTarget=(8.06294, -8.61167, -3.6106), viewOffsetX=7.11044, 
    viewOffsetY=0.592871)
session.viewports['Viewport: 1'].view.setValues(nearPlane=597.725, 
    farPlane=878.993, width=197.694, height=76.3175, cameraPosition=(-601.019, 
    -378.353, -181.728), cameraUpVector=(0.0972906, 0.78936, -0.606172), 
    cameraTarget=(9.18069, -7.33281, -5.17527), viewOffsetX=7.44217, 
    viewOffsetY=0.620531)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=596.827, 
    farPlane=879.893, width=197.397, height=76.2028, cameraPosition=(-601.119, 
    -377.967, -182.193), cameraUpVector=(0.0647971, 0.822936, -0.564427), 
    cameraTarget=(9.08038, -6.94642, -5.64057), viewOffsetX=7.43099, 
    viewOffsetY=0.619599)
session.viewports['Viewport: 1'].view.setValues(nearPlane=545.373, 
    farPlane=930.346, width=180.379, height=69.6332, cameraPosition=(244.753, 
    -380.682, -585.525), cameraUpVector=(-0.275262, 0.917772, -0.286227), 
    cameraTarget=(16.0201, 0.66488, 0.500435), viewOffsetX=6.79035, 
    viewOffsetY=0.566182)
session.viewports['Viewport: 1'].view.setValues(nearPlane=536.587, 
    farPlane=939.132, width=240.629, height=92.8919, viewOffsetX=11.015, 
    viewOffsetY=2.72463)
session.viewports['Viewport: 1'].view.setValues(nearPlane=597.122, 
    farPlane=870.25, width=267.776, height=103.372, cameraPosition=(650.148, 
    -142.465, -322.246), cameraUpVector=(-0.486741, 0.701612, -0.520408), 
    cameraTarget=(9.99085, 7.63397, 7.66269), viewOffsetX=12.2576, 
    viewOffsetY=3.03201)
session.viewports['Viewport: 1'].view.setValues(nearPlane=594.58, 
    farPlane=872.794, width=266.637, height=102.932, viewOffsetX=12.2054, 
    viewOffsetY=3.0191)
session.viewports['Viewport: 1'].view.setValues(nearPlane=562.647, 
    farPlane=913.626, width=252.317, height=97.4039, cameraPosition=(-491.05, 
    -298.887, -456.272), cameraUpVector=(0.68917, 0.493081, -0.530958), 
    cameraTarget=(11.864, -14.2761, -1.03014), viewOffsetX=11.5499, 
    viewOffsetY=2.85695)
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
mdb.jobs['Job-cycloid'].writeInput(consistencyChecking=OFF)
#: 作业输入文件已写入到 "Job-cycloid.inp".
session.viewports['Viewport: 1'].view.setValues(nearPlane=539.822, 
    farPlane=936.452, width=510.74, height=197.165, viewOffsetX=69.3157, 
    viewOffsetY=20.0727)
mdb.save()
#: 模型数据库已保存到 "F:\Temp\Cyc_loid.cae".
