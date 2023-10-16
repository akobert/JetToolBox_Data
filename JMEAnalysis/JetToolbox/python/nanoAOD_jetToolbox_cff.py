import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *
### NanoAOD v5 (for 2016,2017,2018), for different recipe please modify accordingly
from Configuration.Eras.Modifier_run2_nanoAOD_94X2016_cff import run2_nanoAOD_94X2016
from Configuration.Eras.Modifier_run2_nanoAOD_94XMiniAODv2_cff import run2_nanoAOD_94XMiniAODv2
from Configuration.Eras.Modifier_run2_nanoAOD_102Xv1_cff import run2_nanoAOD_102Xv1
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
from JMEAnalysis.JetToolbox.jetToolbox_cff import _addProcessAndTask

from  PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors #Added 3/20/23
from  PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cfi import updatedPatJets #Added 3/20/23

# ---------------------------------------------------------
# This is the part the user should modify
def setupCustomizedJetToolbox(process):
    
    runOnMC = False	#This directory is for Data reprocessing


    #### AK4 PUPPI jets

    ak4btagdiscriminators = [
            	'pfDeepCSVJetTags:probb',
            	'pfDeepCSVJetTags:probbb',
            	'pfDeepCSVJetTags:probc',
            	'pfDeepCSVJetTags:probudsg',
#            	'pfDeepFlavourJetTags:probb',
#            	'pfDeepFlavourJetTags:probbb',
#            	'pfDeepFlavourJetTags:problepb',
#            	'pfDeepFlavourJetTags:probc',
#            	'pfDeepFlavourJetTags:probuds',
#            	'pfDeepFlavourJetTags:probg',
#		'pfMassDecorrelatedParticleNetJetTags:probXbb', #3/1/23 Added ParticleNet Discriminators
#		'pfMassDecorrelatedParticleNetJetTags:probXcc',
#		'pfMassDecorrelatedParticleNetJetTags:probXqq',
#		'pfMassDecorrelatedParticleNetJetTags:probQCDc',
#		'pfMassDecorrelatedParticleNetJetTags:probQCDcc',
#		'pfMassDecorrelatedParticleNetJetTags:probQCDb',
#		'pfMassDecorrelatedParticleNetJetTags:probQCDbb',
#		'pfMassDecorrelatedParticleNetJetTags:probQCDothers'
    ]
    ak4btaginfos = [ 'pfDeepCSVTagInfos' ] #'pfDeepFlavourTagInfos'

    jetToolbox(process, 'ak4', 'dummyseq', 'noOutput',
               dataTier='nanoAOD',
               PUMethod='Puppi', JETCorrPayload='AK4PFPuppi',
               #addQGTagger=True,
               runOnMC=False,
               Cut='pt > 15.0 && abs(eta) < 2.4',
               bTagDiscriminators=ak4btagdiscriminators,
               bTagInfos=ak4btaginfos,
               verbosity=4
               )

    #Exclusive to Data version
    if hasattr(process, "patJetsPuppi"):
        process.patJetsPuppi.addGenPartonMatch = cms.bool(False)
        process.patJetsPuppi.addGenJetMatch = cms.bool(False)
        process.patJetsPuppi.JetPartonMapSource = cms.InputTag("")
        process.patJetsPuppi.JetFlavourInfoSource = cms.InputTag("")

    #### AK8 PUPPI jets
    ak8btagdiscriminators = [
                        'pfBoostedDoubleSecondaryVertexAK8BJetTags',
#                        'pfMassIndependentDeepDoubleBvLJetTags:probQCD',
#                        'pfMassIndependentDeepDoubleBvLJetTags:probHbb',
#                        'pfMassIndependentDeepDoubleCvLJetTags:probQCD',
#                        'pfMassIndependentDeepDoubleCvLJetTags:probHcc',
#                        'pfMassIndependentDeepDoubleCvBJetTags:probHbb',
#                        'pfMassIndependentDeepDoubleCvBJetTags:probHcc',
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:bbvsLight",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ccvsLight",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHccvsQCD",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:WvsQCD",
#                        "pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:ZHbbvsQCD"
#			'pfMassDecorrelatedParticleNetJetTags:probXbb', #2/22/23 Added ParticleNet Discriminators
#			'pfMassDecorrelatedParticleNetJetTags:probXcc',
#			'pfMassDecorrelatedParticleNetJetTags:probXqq',
#			'pfMassDecorrelatedParticleNetJetTags:probQCDc',
#			'pfMassDecorrelatedParticleNetJetTags:probQCDcc',
#			'pfMassDecorrelatedParticleNetJetTags:probQCDb',
#			'pfMassDecorrelatedParticleNetJetTags:probQCDbb',
#			'pfMassDecorrelatedParticleNetJetTags:probQCDothers'
            ]

    jetToolbox(process, 'ak8', 'adummyseq', 'noOutput',
               dataTier='nanoAOD',
               PUMethod='Puppi', JETCorrPayload='AK8PFPuppi',
	       subJETCorrPayload='AK4PFPuppi',
               runOnMC=runOnMC,
               Cut='pt > 100.0',
               bTagDiscriminators=ak8btagdiscriminators,
               verbosity=4,
	       addSoftDrop=True,
               addSoftDropSubjets=True,
               addPruning=True,
               addNsub=True,
               addEnergyCorrFunc=True,
	       addEnergyCorrFuncSubjets=True,	# Added 7/13
#	       runParticleNetMD=True	#Added 3/7/23
               )
#    particlenet_stuff = '''

#    process.SelectJetCorrFactorsAK8 = patJetCorrFactors.clone(src='selectedPatJetsAK8PFPuppiSoftDrop',
#        levels = cms.vstring('L1FastJet',
#            'L2Relative',
#            'L3Absolute',
#        'L2L3Residual'),
#        payload = cms.string('AK8PFPuppi'),
#        primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
#    )
    process.SelectJetCorrFactorsAK8 = patJetCorrFactors.clone(src='packedPatJetsAK8PFPuppiSoftDrop',
        levels = cms.vstring('L1FastJet',
            'L2Relative',
            'L3Absolute',
        'L2L3Residual'),
        payload = cms.string('AK8PFPuppi'),
        primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    )


#    process.updatedSelectJetsAK8 = updatedPatJets.clone(
#        addBTagInfo=False,
#        jetSource='selectedPatJetsAK8PFPuppiSoftDrop',
#	jetCorrFactorsSource=cms.VInputTag(cms.InputTag("SelectJetCorrFactorsAK8")),
#    )
    process.updatedSelectJetsAK8 = updatedPatJets.clone(
        addBTagInfo=False,
        jetSource='packedPatJetsAK8PFPuppiSoftDrop',
	jetCorrFactorsSource=cms.VInputTag(cms.InputTag("SelectJetCorrFactorsAK8")),
    )
   

#    print("asdf")
    print(process.patAlgosToolsTask)
 
    from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection   
    from RecoBTag.ONNXRuntime.pfParticleNet_cff import pfMassDecorrelatedParticleNetJetTags
    flav_names = ["probQCDothers", "probQCDb", "probQCDbb", "probQCDc", "probQCDcc", "probXqq", "probXbb", "probXcc"]
    pfMassDecorrelatedParticleNetJetTagsProbs = ['pfMassDecorrelatedParticleNetJetTags:' + n for n in flav_names]
    ak8btagdiscriminators += pfMassDecorrelatedParticleNetJetTagsProbs

    print("DEBUG: ParticleNetMD Tagging")

    JETCorrLevels = ['L2Relative', 'L3Absolute', 'L2L3Residual']

    updateJetCollection(
    	process,
    	jetSource=cms.InputTag('updatedSelectJetsAK8'),
    	rParam=0.8,
    	jetCorrections=('AK8PFPuppi', cms.vstring(JETCorrLevels), 'None'),
    	btagDiscriminators=ak8btagdiscriminators,
        postfix='AK8'
    )
   
    _addProcessAndTask(process, 'SelectJetCorrFactorsAK8', process.SelectJetCorrFactorsAK8)
    _addProcessAndTask(process, 'updatedSelectJetsAK8', process.updatedSelectJetsAK8) 
    
    print(process.patAlgosToolsTask)
 
    from RecoBTag.ONNXRuntime.pfParticleNet_cff import pfMassDecorrelatedParticleNetJetTags
    process.pfParticleNetTagInfosAK8.jet_radius = 0.8
    process.pfMassDecorrelatedParticleNetJetTagsAK8ParticleNet = pfMassDecorrelatedParticleNetJetTags.clone(
        src = 'pfParticleNetTagInfos',
#        preprocess_json = '/home/akobert/CMSSW_10_6_29/src/ParticleNetMD/preprocess.json',
#        model_path = '/home/akobert/CMSSW_10_6_29/src/ParticleNetMD/ParticleNetMD.onnx',
        preprocess_json = 'PhysicsTools/data/ParticleNet-MD/ak8/preprocess.json',
        model_path = 'PhysicsTools/data/ParticleNet-MD/ak8/ParticleNet-MD.onnx',
    )
    print("DEBUG: Checkpoint 1")
   
    srcJets = cms.InputTag('selectedUpdatedPatJetsAK8') 

    process.ak8WithUserData = cms.EDProducer("PATJetUserDataEmbedder",
        src=srcJets,
        userFloats=cms.PSet(),
        userInts=cms.PSet(),
    )

    process.finalSelectedJetsAK8 = cms.EDFilter("PATJetRefSelector",
        src = cms.InputTag("ak8WithUserData"),
        cut = cms.string("")
    )
    print("DEBUG: Checkpoint 2")
    
    process.selectedPatJetsAK8PFPuppiJTBTable = cms.EDProducer("SimpleCandidateFlatTableProducer", src=cms.InputTag('finalSelectedJetsAK8'), name=cms.string("selectedPatJetsAK8PFPuppi"), cut=cms.string(""), doc=cms.string("Selected AK8 PUPPI Jets with ParticleNet Taggers"), singleton=cms.bool(False), extension=cms.bool(False), variables=cms.PSet(P4Vars,
#	msoftdrop = Var("groomedMass()", float, doc="Corrected soft drop mass with PUPPI", precision=10),
	msoftdrop = Var("userFloat('ak8PFJetsPuppiSoftDropMass')", float, doc='Softdrop mass', precision=10),
        area=Var("jetArea()", float, doc="jet catchment area, for JECs", precision=10),
        nMuons = Var("?hasOverlaps('muons')?overlaps('muons').size():0", int, doc="number of muons in the jet"),
        muonIdx1 = Var("?overlaps('muons').size()>0?overlaps('muons')[0].key():-1", int, doc="index of first matching muon"),
        muonIdx2 = Var("?overlaps('muons').size()>1?overlaps('muons')[1].key():-1", int, doc="index of second matching muon"),
        electronIdx1 = Var("?overlaps('electrons').size()>0?overlaps('electrons')[0].key():-1", int, doc="index of first matching electron"),
        electronIdx2 = Var("?overlaps('electrons').size()>1?overlaps('electrons')[1].key():-1", int, doc="index of second matching electron"),
         nElectrons = Var("?hasOverlaps('electrons')?overlaps('electrons').size():0", int, doc="number of electrons in the jet"),
        jetId = Var("userInt('looseId')+userInt('tightId')*2+4*userInt('tightIdLepVeto')",int,doc="Jet ID flags bit1 is loose, bit2 is tight, bit3 is tightLepVeto"),
        nConstituents = Var("numberOfDaughters()",int,doc="Number of particles in the jet"),
        rawFactor = Var("1.-jecFactor('Uncorrected')",float,doc="1 - Factor to get back to raw pT",precision=6),
        tau1 = Var("userFloat('NjettinessAK8Puppi:tau1')", float, doc="Nsubjettiness (1 axis)", precision=10),
        tau2 = Var("userFloat('NjettinessAK8Puppi:tau2')", float, doc="Nsubjettiness (2 axis)", precision=10),
        tau3 = Var("userFloat('NjettinessAK8Puppi:tau3')", float, doc="Nsubjettiness (3 axis)", precision=10),
	tau4 = Var("userFloat('NjettinessAK8Puppi:tau4')", float, doc="Nsubjettiness (4 axis)", precision=10),
        n2b1 = Var("?hasUserFloat('nb1AK8PuppiSoftDrop:ecfN2')?userFloat('nb1AK8PuppiSoftDrop:ecfN2'):-99999.", float, doc="N2 with beta=1 (for jets with raw pT>250 GeV)", precision=10),
	n3b1 = Var("?hasUserFloat('nb1AK8PuppiSoftDrop:ecfN3')?userFloat('nb1AK8PuppiSoftDrop:ecfN3'):-99999.", float, doc="N3 with beta=1 (for jets with raw pT>250 GeV)", precision=10),
	chHEF = Var("chargedHadronEnergyFraction()", float, doc="charged Hadron Energy Fraction", precision= 6),
        neHEF = Var("neutralHadronEnergyFraction()", float, doc="neutral Hadron Energy Fraction", precision= 6),
        chEmEF = Var("chargedEmEnergyFraction()", float, doc="charged Electromagnetic Energy Fraction", precision= 6),
        neEmEF = Var("neutralEmEnergyFraction()", float, doc="neutral Electromagnetic Energy Fraction", precision= 6),
	muEF = Var("muonEnergyFraction()", float, doc="muon Energy Fraction", precision= 6),	
	)
    )
    print("DEBUG: Checkpoint 3")
    
    for prob in pfMassDecorrelatedParticleNetJetTagsProbs:
        name = 'ParticleNetMD_' + prob.split(':')[1]
        name = name.replace('QCDothers', 'QCD')
        setattr(process.selectedPatJetsAK8PFPuppiJTBTable.variables, name, Var("bDiscriminator('%s')" % prob, float, doc=prob, precision=-1))
    
#    process.selectedPatSubJetsAK8Table = cms.EDProducer("SimpleCandidateFlatTableProducer", src=cms.InputTag("selectedPatJetsAK8PFPuppiSoftDropPacked", "SubJets"), name=cms.string("SelectedSubJetAK8"), cut=cms.string(""), doc=cms.string("Selected AK8 PUPPI SubJets"), singleton=cms.bool(False), extension=cms.bool(False), variables=cms.PSet(P4Vars,
#	)
#    )
#    process.selectedPatSubJetsAK8Table.variables.pt.precision = 10
    print("DEBUG: Checkpoint 4")

    _addProcessAndTask(process, 'ak8WithUserData', process.ak8WithUserData)
    _addProcessAndTask(process, 'finalSelectedJetsAK8', process.finalSelectedJetsAK8)
    _addProcessAndTask(process, 'selectedPatJetsAK8PFPuppiJTBTable', process.selectedPatJetsAK8PFPuppiJTBTable)
#    _addProcessAndTask(process, 'selectedPatSubJetsAK8Table', process.selectedPatSubJetsAK8Table)


    #Avoid Circular Dependency
#    process.jetMC.remove(process.patJetPartons)
#    _addProcessAndTask(process, 'patJetPartons', process.patJetPartons)
#    '''
    print("test10")
    return process


# ---------------------------------------------------------

def nanoJTB_customizeMC(process):
    print("test9")
    run2_nanoAOD_94X2016.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_94XMiniAODv2.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_102Xv1.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_106Xv1.toModify(process, setupCustomizedJetToolbox)
    run2_nanoAOD_106Xv2.toModify(process, setupCustomizedJetToolbox)
    #process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)  # needed for crab publication
    return process
