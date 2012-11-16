# to run this:
# use "-h" option to get help

import ROOT
import sys
import os
import commands
import itertools
import time
import glob
import math
import datetime
from copy import deepcopy
import numpy as np
import pickle
import pwd
import shutil

from DataFormats.FWLite import Events, Handle
import eventSelection as llbb
from zbbCommons import zbbfile, zbblabel

from LumiReWeighting import LumiReWeighting 
from LeptonsReweighting import LeptonsReWeighting
from btaggingWeight import btaggingWeight

class unfolder:
    """ Class to compute unfolding "matrices" """
    def __init__(self, infiles0 = "", whattodo = [], startup = [], finish = [], muchannel = None, save_output=True):
        """ Initialization: definition of all handles, etc ... """
        # allowing to use directories or filenames
        infiles = os.path.isdir(infiles0) and glob.glob(os.path.join(infiles0,"*")) or [infiles0]
        # variables that will become members
        self.collections = { "jets":          {"handle":"vector<pat::Jet>", "collection":zbblabel.jetlabel},
                             "muons":         {"handle":"vector<pat::Muon>", "collection":zbblabel.allmuonslabel},
                             "goodmuons":     {"handle":"vector<pat::Muon>", "collection":zbblabel.muonlabel},
                             "electrons":     {"handle":"vector<pat::Electron>", "collection":zbblabel.allelectronslabel},
                             "goodelectrons": {"handle":"vector<pat::Electron>", "collection":zbblabel.electronlabel},
                             "genjets":       {"handle":"vector<reco::GenJet>", "collection":"prunedJets"}, ## was ak5GenJets
                             "genparticles":  {"handle":"vector<reco::GenParticle>", "collection":"prunedGen"}, ## was zbblabel.genlabel
                             "zee":           {"handle":"vector<reco::CompositeCandidate>", "collection":"zelAllelAll"},
                             "zmumu":         {"handle":"vector<reco::CompositeCandidate>", "collection":"zmuAllmuAll"},
                             "zeegood":       {"handle":"vector<reco::CompositeCandidate>", "collection":zbblabel.zelelabel},
                             "zmumugood":     {"handle":"vector<reco::CompositeCandidate>", "collection":zbblabel.zmumulabel},
                             "met" :          {"handle":"vector<pat::MET>", "collection":zbblabel.metlabel}
                           }
        # defining all handles
        for key, value in self.collections.items():
            setattr(self, key+"Handle", Handle (value["handle"]))
            setattr(self, key+"Collection", value["collection"])
        # load events
        self.events = Events (infiles)
        # tasks
        self.whattodo = whattodo
        self.startup = startup
        self.finish = finish
        # creating tasks vector to avoid function lookup for each event
        self.funcs_todo = [getattr(self, "step_"+task) for task in self.whattodo]
        self.save_output = save_output
        # format outfile and logfile:
        if self.save_output:
            self.outfile = "unfolding_"+datetime.datetime.strftime(datetime.datetime.now(),"%Y%d%m_%H%M")+".txt"
            self.logfile = "unfolding_log_"+datetime.datetime.strftime(datetime.datetime.now(),"%Y%d%m_%H%M")+".txt"
            logf = open(self.logfile, "w")
            logf.write("Running on %s \n" % (infiles0))
            logf.write("Muchannel = %s \n" % (str(muchannel)))
            logf.write("Output file = %s \n" % self.outfile)
        # mu channel (True means muons)
        self.muchannel = muchannel
        self.counts = {}

    class usercontent:
        def __init__(self):
            self.stop = False

    def step(self, event):
        """ Run analysis step on one event. Everything should be done here """
        # get collections
        for key, value in self.collections.items():
            event.getByLabel(value["collection"], getattr(self,key+"Handle"))
            setattr(self, key, getattr(self,key+"Handle").product())
        # do magic
        ucont = self.usercontent()
        # initialize output
        ucont.event = event
        for task in self.funcs_todo:
            res = task(ucont)
            if ucont.stop: break
            if res:
                print "Error during", task
                return 1
        del ucont
               

    def run(self, tot = 1000):
        """ run on the first 'tot' events """
        num = 1
        dumpevery = 10000
        if dumpevery > tot and tot > 0 : dumpevery = tot
        dumpfile = "unfolding_"+datetime.datetime.strftime(datetime.datetime.now(),"%Y%d%m_%H%M")+".txt"
        print "============================"
        print "=== Initialization steps ==="
        print "============================"
        for start in self.startup:
            start_todo = getattr(self,"start_"+start)
            start_todo()
        print "============================"
        print "===  running on events   ==="
        print "============================"
        for event in self.events:
            # print the first ten events to see when it really starts
            if num < 10: print "event:", num 
            # regularly print where we are
            if not num%(tot/10) and tot > 0: print "event:", num
            # dump output every few events in case of long runs
            if not num%dumpevery:
                self.out = ""
                for fin in self.finish:
                    finish_todo = getattr(self,"finish_"+fin)
                    finish_todo()
                if self.save_output:
                    outf = open(self.outfile, "w")
                    outf.write(self.out)
                    outf.write("last update: %s \n" % (str(datetime.datetime.now())))
                    outf.close()
            self.step(event)
            num += 1
            if num > tot and tot > 0: break
        print "============================"
        print "===     Finalization     ==="
        print "============================"
        self.out = ""
        for fin in self.finish:
            finish_todo = getattr(self,"finish_"+fin)
            finish_todo()
        if self.save_output:
            outf = open(self.outfile, "w")
            outf.write(self.out)
            outf.write("last update: %s \n" % (str(datetime.datetime.now())))
            outf.close()
            print "Results are in:", self.outfile

    def run_all(self):
        """ run list of tasks on all events in file(s) """
        print "============================"
        print "=== Initialization steps ==="
        print "============================"
        for start in self.startup:
            start_todo = getattr(self,"start_"+start)
            start_todo()
        print "============================"
        print "===   running on events  ==="
        print "============================"
        for event in self.events:
            self.step(event)
        print "============================"
        print "===     Finalization     ==="
        print "============================"
        for fin in self.finish:
            finish_todo = getattr(self,"finish_"+fin)
            finish_todo()

    # starting here, methods are supposed to be run inside the "step" method 
    # and can be called by their names as arguments of said method.
    # all collections are also supposed to be well defined
    def step_stupid_test(self,ucont):
        """ As a basic test, print all jet PT's as a list"""
        print "Jets PT:"
        print ", ".join([f_2(jet.pt()) for jet in self.jets])

    def step_event_weight(self, ucont):
        """ computing weight """
        ucont.rw = self.pu_engine.weight( fwevent=ucont.event )
        return 0

    # starting here, we'll be doing one step per matrix in order to get a clearer view of the process
    def step_a_l(self, ucont):
        """ computing:
                # number of gen b-jets per event
                # global flavour of the event
                # events passing leptons baseline cuts in each gen b-jet bin
                # events passing leptons acceptance cuts in each b-jet bin
        """
        # print number of reco b-jets for cross-check
        # print "reco b-jets:", len([jet for jet in self.jets if llbb.isBJet(jet,"HE","SSV")])
        # count total number of events
        # ----------------------------
        try:
            self.total_events += ucont.rw
        except AttributeError:
            self.total_events = ucont.rw
        # baseline leptons from Z
        #------------------------
        gen_elec_pt_base = 20.0
        gen_elec_eta_base = 2.4
        #2.5
        gen_muon_pt_base = 20.0
        gen_muon_eta_base = 2.4
        #2.5
        gen_mass_l_base = 76.0
        gen_mass_u_base = 106.0
        ucont.gen_z_yes = False  ### True here to speed up
        ucont.flav = -1
        for particle in self.genparticles:
            if particle.pdgId() == 23:
                ucont.gen_leptons = [particle.daughter(i) for i in range(particle.numberOfDaughters()) if particle.daughter(i).pdgId() != 23]
                if ucont.gen_leptons:
                    if math.fabs(ucont.gen_leptons[0].pdgId()) == 13 and len([lep for lep in ucont.gen_leptons if acc_pt_eta(lep,gen_muon_pt_base,gen_muon_eta_base)])== 2 and gen_mass_l_base < (get_vec(ucont.gen_leptons[0]) + get_vec(ucont.gen_leptons[1])).M() < gen_mass_u_base:
                        ucont.flav = 13
                        if self.muchannel == True or self.muchannel == None:
                            ucont.gen_z_yes = True
                    elif math.fabs(ucont.gen_leptons[0].pdgId()) == 11 and len([lep for lep in ucont.gen_leptons if acc_pt_eta(lep,gen_elec_pt_base,gen_elec_eta_base)])== 2 and gen_mass_l_base < (get_vec(ucont.gen_leptons[0]) + get_vec(ucont.gen_leptons[1])).M() < gen_mass_u_base:
                        ucont.flav = 11
                        if self.muchannel == False or self.muchannel == None:
                            ucont.gen_z_yes = True
                    else:
                        ucont.flav = -1
                else: ucont.flav = -1
                break
        # number of gen b-jets + b-jets array
        # -----------------------------------
        gen_jet_pt  = 25.0
        gen_jet_eta = 2.1
        gen_jet_dr = 0.5
        gen_jet_lepton_dr = 0.5
        # match with b-hadrons
        # get final b-hadrons
        bparts = [part for part in self.genparticles if (499 < math.fabs(part.pdgId()) < 600) or (4999 < math.fabs(part.pdgId()) < 6000)]
        bhads = [part for part in bparts if is_final_bhad(part)]
        # bhads = [part for part in self.genparticles if is_final_bhad(part)]
        # list jets that match these by dr
        ucont.gen_b_jets = match_obo(self.genjets, bhads, gen_jet_dr)
        ucont.gen_b_jets_all = ucont.gen_b_jets[:]
        ucont.gen_b_jets = [jet for jet in ucont.gen_b_jets if acc_pt_eta(jet, gen_jet_pt, gen_jet_eta)]
        ucont.gen_b_jets = [jet for jet in ucont.gen_b_jets if not overlap(jet, ucont.gen_leptons, gen_jet_lepton_dr)]
        ucont.gen_b = len(ucont.gen_b_jets)>1 and 2 or len(ucont.gen_b_jets)
        if ucont.gen_z_yes:
            try:
                self.gen_baseline[ucont.gen_b] += ucont.rw
            except AttributeError:
                self.gen_baseline = [0,0,0]
                self.gen_baseline[ucont.gen_b] += ucont.rw
        # leptons in acceptance w/ correct reconstructed mass 
        # ---------------------------------------------------
        gen_elec_pt = 20.0 ## check the values !
        gen_elec_eta = 2.4
        gen_muon_pt = 20.0 ##
        gen_muon_eta = 2.4
        gen_mass_l = 76.0 
        gen_mass_u = 106.0
        ucont.gen_z_kin_yes = False
        ucont.gen_zb = 0
        if ucont.flav == 13 and len([lep for lep in ucont.gen_leptons if acc_pt_eta(lep,gen_muon_pt,gen_muon_eta)]) == 2 and (self.muchannel == True or self.muchannel == None):
            if gen_mass_l < (get_vec(ucont.gen_leptons[0]) + get_vec(ucont.gen_leptons[1])).M() < gen_mass_u:
                ucont.gen_z_kin_yes = True
        elif ucont.flav == 11 and len([lep for lep in ucont.gen_leptons if acc_pt_eta(lep,gen_elec_pt,gen_elec_eta)]) == 2 and (self.muchannel == False or self.muchannel == None):
            if gen_mass_l < (get_vec(ucont.gen_leptons[0]) + get_vec(ucont.gen_leptons[1])).M() < gen_mass_u:
                ucont.gen_z_kin_yes = True
        # number of gen b-jets after acceptance cuts
        if ucont.gen_z_kin_yes: 
            ucont.gen_zb = ucont.gen_b
            try:
                self.gen_acc[ucont.gen_b] += ucont.rw
            except AttributeError:
                self.gen_acc = [0,0,0]
                self.gen_acc[ucont.gen_b] += ucont.rw
        if not ucont.gen_z_kin_yes: ucont.stop = True

    def finish_print_a_l(self):
        """ print resume from A_l computation """
        if not hasattr(self,"out"): self.out = ""
        self.a_l = [0,0,0]
        for i in range(3):
             if self.gen_baseline[i]:
                 self.a_l[i] = self.gen_acc[i]/float(self.gen_baseline[i])
        self.out += "===             A_l                ===\n"
        self.out += "Total events: %i\n" % (self.total_events)
        self.out += "Gen b-jets    :\t0\t1\t2\n"
        self.out += "Baseline cuts :\t"+"\t".join([f_2(el) for el in self.gen_baseline])+"\n" 
        self.out += "Acceptance    :\t"+"\t".join([f_2(el) for el in self.gen_acc])+"\n" 
        self.out += "A_l           :\t"+"\t".join([f_2(el) for el in self.a_l])+"\n"
        self.counts["All"] = self.total_events
        self.counts["Base"] = self.gen_baseline
        self.counts["A_l"] = self.gen_acc
        

    def step_e_r(self, ucont):
        """ computing:
                # events with a reconstructed Z (should i use findBestCandidate as it does not match gen leptons ?)
                # events with reconstructed jets matching the gen b-jets and inside acceptance cuts
                # e_r matrix
                # needs the gen_zb variable from a_l routine
        """
        # print "z cands (mu): all:", len(self.zmumu), "good:", len(self.zmumugood)
        # print "z cands (el): all:", len(self.zee), "good:", len(self.zeegood)
        ucont.rec_z_yes = False
        ucont.reco_leptons = []
        # getting best reco Z candidate
        # -----------------------------
        ucont.reco_z = False
        # removing candidates whose leptons are not matching the gen ones
        gen_lep_dr = 0.3
        zmumu_match = []
        if (self.muchannel == True or self.muchannel == None):
            for z in self.zmumu:
                if (len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2 \
                    and z.daughter(0).pt()>20 \
                    and math.fabs(z.daughter(0).eta())<2.4 \
                    and z.daughter(1).pt()>20 \
                    and math.fabs(z.daughter(1).eta())<2.4 ):  
                #if len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2:
                    zmumu_match.append(z) 
        zelel_match = []
        if (self.muchannel == False or self.muchannel == None):
            for z in self.zee:
                if (len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2 \
                    and z.daughter(0).pt()>20 \
                    and ((math.fabs(z.daughter(0).eta())< 1.442)or((1.566<(math.fabs(z.daughter(0).eta())))and((math.fabs(z.daughter(0).eta())<2.4)))) \
                    and z.daughter(1).pt()>20 \
                    and ((math.fabs(z.daughter(1).eta())< 1.442)or((1.566<(math.fabs(z.daughter(1).eta())))and((math.fabs(z.daughter(1).eta())<2.4)))) \
                    and math.fabs(z.daughter(0).eta())<2.4 \
                    and math.fabs(z.daughter(1).eta())<2.4 ):  
                #if (len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2):
                    zelel_match.append(z) 
        ucont.reco_z = llbb.findBestCandidate(self.muchannel, None, zelel_match, zmumu_match)
        if ucont.reco_z:
            ucont.rec_z_yes = True
            ucont.reco_leptons = [ucont.reco_z.daughter(0), ucont.reco_z.daughter(1)]
        # getting good jets matching the gen b-jets 
        # -----------------------------------------------------------------
        ucont.rec_b = 0
        ucont.rec_zb = 0
        reco_jet_gen_jet_dr = 0.5
        # select good jets
        ucont.reco_jets = [jet for jet in self.jets if llbb.isGoodJet(jet,ucont.reco_z)]
        # keep jets that match gen b-jets by 0.5
        # ucont.reco_jets = [jet for jet in ucont.reco_jets if overlap(jet, ucont.gen_b_jets, reco_jet_gen_jet_dr)]
        ucont.reco_jets = match_obo(ucont.reco_jets, ucont.gen_b_jets_all, reco_jet_gen_jet_dr)
        ucont.rec_b = len(ucont.reco_jets)>1 and 2 or len(ucont.reco_jets)
        if ucont.rec_z_yes : ucont.rec_zb = ucont.rec_b
        try:
            self.rec_zb[ucont.rec_zb] += ucont.rw
        except AttributeError:
            self.rec_zb = [0,0,0]
            self.rec_zb[ucont.rec_zb] += ucont.rw
        # computing e_r matrix
        # --------------------
        try:
            self.mat_e_r[ucont.rec_zb][ucont.gen_zb] += ucont.rw
        except AttributeError:
            self.mat_e_r = [[0,0,0],[0,0,0],[0,0,0]]
            self.mat_e_r[ucont.rec_zb][ucont.gen_zb] += ucont.rw 
        # interrupt if there's no reco z cand
        # -----------------------------------
        if not ucont.rec_zb: ucont.stop = True       

    def finish_print_e_r(self):  
        if not hasattr(self,"out"): self.out = ""      
        self.out += "===             E_r                ===\n"
        self.out += "--------------------------------------\n"
        self.out += "gen b:\t\t0\t1\t2\n"
        # print "-------- un-normalized ---------------"
        # for i, row in enumerate(self.mat_e_r):
        #     print "rec j: ", f_2(i), " :\t", "\t".join(["%.2f" % (el) for el in row])
        # print "--------- normalized -----------------"
        self.e_r_norm = deepcopy(self.mat_e_r)
        norms = norm_by_column(self.e_r_norm)
        for i, row in enumerate(self.e_r_norm):
            self.out += "rec j: "+str(i)+" :\t"+"\t".join(["%.2f" % (el) for el in row])+"\n"
        self.out += "--------------------------------------\n"
        self.out += "norms:\t\t"+"\t".join([f_2(norm) for norm in norms])+"\n"
        self.out += "--------------------------------------\n"
        self.rfact = (norms[1]+norms[2]) and norms[0]/float(norms[1]+norms[2]) or 0
        self.out += "R-factor:"+str(self.rfact)+"\n"
        self.out += "--------------------------------------\n"
        self.counts["e_r"] = self.mat_e_r

    def step_e_l(self, ucont):
        """ compute lepton efficiency for each rec_zb bin """
        # ucont.goodleps = [lep for lep in ucont.reco_leptons if (llbb.isGoodElectron(lep,'matched') or llbb.isGoodMuon(lep,'matched'))]
        gen_lep_dr = 0.3

        zmumu_match = []
        if (self.muchannel == True or self.muchannel == None):
            for z in self.zmumugood:
                if (len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2 \
                    and z.daughter(0).pt()>20 \
                    and math.fabs(z.daughter(0).eta())<2.4 \
                    and z.daughter(1).pt()>20 \
                    and math.fabs(z.daughter(1).eta())<2.4):
                #if len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2:
                    zmumu_match.append(z) 

        zelel_match = []
        if (self.muchannel == False or self.muchannel == None):
            for z in self.zeegood:
                if (len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2 \
                    and z.daughter(0).pt()>20 \
                    and ((math.fabs(z.daughter(0).eta())< 1.442)or((1.566<(math.fabs(z.daughter(0).eta())))and((math.fabs(z.daughter(0).eta())<2.4)))) \
                    and z.daughter(1).pt()>20 \
                    and ((math.fabs(z.daughter(1).eta())< 1.442)or((1.566<(math.fabs(z.daughter(1).eta())))and((math.fabs(z.daughter(1).eta())<2.4)))) \
                    and math.fabs(z.daughter(0).eta())<2.4 \
                    and math.fabs(z.daughter(1).eta())<2.4 ):
                #if (len(match_obo([z.daughter(0), z.daughter(1)], ucont.gen_leptons, gen_lep_dr)) == 2):
                    zelel_match.append(z) 

        reco_z_good = llbb.findBestCandidate(self.muchannel, None, zelel_match, zmumu_match)
        if reco_z_good and ucont.rec_z_yes:
            ucont.el_weight = self.el_engine.weight(fwevent=ucont.event, muChannel=self.muchannel)
            try: 
                self.lep_eff[ucont.rec_zb] += ucont.rw*ucont.el_weight
            except AttributeError:
                self.lep_eff = [0,0,0]
                self.lep_eff[ucont.rec_zb] += ucont.rw*ucont.el_weight
        else:
            ucont.stop = True

    def finish_print_e_l(self):
        if not hasattr(self,"lep_eff"):
            self.out += "== No events passed the lepton selection =="
        else:
            self.e_l = [self.lep_eff[i]/float(self.rec_zb[i]) if self.rec_zb[i] else 0 for i in range(3)]
            self.out += "===             E_l                ===\n"
            self.out += "Reco b-jets    :   0\t1\t2\n"
            self.out += "basic Z + jet  : "+"\t".join([f_2(el) for el in self.rec_zb])+"\n"
            self.out += "Lepton iso/ID  : "+"\t".join([f_2(el) for el in self.lep_eff])+"\n"
            self.out += "E_l            : "+"\t".join([f_2(el) for el in self.e_l])+"\n"
            self.counts["e_l"] = self.lep_eff

    def step_e_b(self, ucont):
        """ computes:
                the e_b matrix based on b-tagging
        """
        algo = "SSV"
        n_he = len([jet for jet in ucont.reco_jets if llbb.isBJet(jet, "HE", algo)])
        n_hp = len([jet for jet in ucont.reco_jets if llbb.isBJet(jet, "HP", algo)])
        if n_he > 2: n_he = 2
        if n_hp > 2: n_hp = 2
        ucont.n_he = n_he
        ucont.n_hp = n_hp
        he_modes = [None, "HEexcl", "HEHE"]
        hp_modes = [None, "HPexcl", "HPHP"]
        heweight = 1
        # working point HPexcl - HEHE does not preserve normalisation and thus requires additional steps
        if n_hp == 1:
            self.btag_engine.setMode("HPexcl")
            mixweight = self.btag_engine.weight(ucont.event,self.muchannel)
            try:
                self.mat_e_b_mixed[1][ucont.rec_zb] += ucont.rw*mixweight*ucont.el_weight
            except:
                self.mat_e_b_mixed = [[0,0,0],[0,0,0],[0,0,0]]
                self.mat_e_b_mixed[1][ucont.rec_zb] += ucont.rw*mixweight*ucont.el_weight
        if n_he >= 2:
            self.btag_engine.setMode("HEHE")
            mixweight = self.btag_engine.weight(ucont.event,self.muchannel)
            try:
                self.mat_e_b_mixed[2][ucont.rec_zb] += ucont.rw*mixweight*ucont.el_weight
            except:
                self.mat_e_b_mixed = [[0,0,0],[0,0,0],[0,0,0]]
                self.mat_e_b_mixed[2][ucont.rec_zb] += ucont.rw*mixweight*ucont.el_weight

        # HEexcl - HEHE and HPexcl - HPHP are straightforward
        if he_modes[ucont.n_he]: 
            self.btag_engine.setMode(he_modes[ucont.n_he])
            heweight = self.btag_engine.weight(ucont.event,self.muchannel)
        hpweight = 1
        if hp_modes[ucont.n_hp]:
            self.btag_engine.setMode(hp_modes[ucont.n_hp])
            hpweight = self.btag_engine.weight(ucont.event,self.muchannel)
        try:
            self.mat_e_b_he[ucont.n_he][ucont.rec_zb] += ucont.rw*heweight*ucont.el_weight
            self.mat_e_b_hp[ucont.n_hp][ucont.rec_zb] += ucont.rw*hpweight*ucont.el_weight
        except AttributeError:
            self.mat_e_b_he = [[0,0,0],[0,0,0],[0,0,0]]
            self.mat_e_b_hp = [[0,0,0],[0,0,0],[0,0,0]]
            self.mat_e_b_he[ucont.n_he][ucont.rec_zb] += ucont.rw*heweight*ucont.el_weight
            self.mat_e_b_hp[ucont.n_hp][ucont.rec_zb] += ucont.rw*hpweight*ucont.el_weight

    def finish_print_e_b(self):
        if not hasattr(self,"mat_e_b_he") or not hasattr(self,"mat_e_b_hp") or not hasattr(self,"mat_e_b_mixed"):
            self.out += "== some e_b matrices are empty =="
        else:
            self.out += "--------------------------------------\n"
            self.out += "                E_b                   \n"
            self.out += "--------------------------------------\n"
            self.out += "--------------------------------------\n"
            self.out += "rec b:\t\t0\t1\t2\n"
            self.out += "--------------------------------------\n"
            self.e_b_he_norm = deepcopy(self.mat_e_b_he)
            # norms_he = norm_by_column(self.e_b_he_norm)
            norms_he = norm_columns_from_vec(self.e_b_he_norm, self.lep_eff)
            for i, row in enumerate(self.e_b_he_norm):
                self.out += "HE b: "+str(i)+" :\t"+"\t".join(["%.2f" % (el) for el in row])+"\n"
            self.out += "--------------------------------------\n"
            self.out += "norms:\t\t"+"\t".join([f_2(norm) for norm in norms_he])+"\n"
            self.out += "--------------------------------------\n"
            self.e_b_hp_norm = deepcopy(self.mat_e_b_hp)
            # norms_hp = norm_by_column(self.e_b_hp_norm)
            norms_hp = norm_columns_from_vec(self.e_b_hp_norm, self.lep_eff)
            for i, row in enumerate(self.e_b_hp_norm):
                self.out += "HP b: "+str(i)+" :\t"+"\t".join(["%.2f" % (el) for el in row])+"\n"
            self.out += "--------------------------------------\n"
            self.out += "norms:\t\t"+"\t".join([f_2(norm) for norm in norms_hp])+"\n"
            self.out += "--------------------------------------\n"
            self.e_b_mixed_norm = deepcopy(self.mat_e_b_mixed)
            # norms_mixed = norm_by_column(self.e_b_mixed_norm)
            norms_mixed = norm_columns_from_vec(self.e_b_mixed_norm, self.lep_eff)
            for i, row in enumerate(self.e_b_mixed_norm):
                self.out += "'mixed' b: "+str(i)+" :\t"+"\t".join(["%.2f" % (el) for el in row])+"\n"
            self.out += "--------------------------------------\n"
            self.out += "norms:\t\t"+"\t".join([f_2(norm) for norm in norms_mixed])+"\n"
            self.out += "--------------------------------------\n"
            self.counts["e_b_he"] = self.mat_e_b_he
            self.counts["e_b_hp"] = self.mat_e_b_hp
            self.counts["e_b_mixed"] = self.mat_e_b_mixed

            

###################### MET Matrix #################################
    def step_e_m(self, ucont):
        """ compute met efficiency for each rec_zb bin with at least two bjets HE """
        # ucont.goodleps = [lep for lep in ucont.reco_leptons if (llbb.isGoodElectron(lep,'matched') or llbb.isGoodMuon(lep,'matched'))]
        #ucont.reco_jets = [jet for jet in self.jets if llbb.isGoodJet(jet,ucont.reco_z)]
        ucont.good_met =  [met for met in self.met if llbb.isGoodMet_Sig(met,cut=10)]      
        # print "ucont.n_he",ucont.n_he
        if ucont.rec_z_yes and ucont.n_he>=2 and ucont.good_met :
            #self.mat_e_b_mixed[2][2]
            self.btag_engine.setMode("HEHE")
            bweight = self.btag_engine.weight(ucont.event,self.muchannel)
            # print "bweight HEHE", bweight
            try: 
                self.met_eff[ucont.rec_zb] += ucont.rw*bweight*ucont.el_weight
            except AttributeError:
                self.met_eff =[0,0,0] 
                self.met_eff[ucont.rec_zb] += ucont.rw*bweight*ucont.el_weight
        else:
            ucont.stop = True

                
    def finish_print_e_m(self):
        if not hasattr(self,"met_eff"):
            self.out += "== No events passed the met selection =="
        else:
            print "float(self.e_b_he_norm[2][2])", float(self.mat_e_b_he[2][2])
            print "self.met_eff[2]",self.met_eff[2] 
            print "self.met_eff[1]",self.met_eff[1] 
            print "self.met_eff[0]",self.met_eff[0] 
            self.e_m = self.met_eff[2]/(float(self.mat_e_b_he[2][2])) if self.mat_e_b_he[2][2] else 0
            self.out += "===             MET                ===\n"            
            self.out += "MET            : "+"\t"+f_2(self.e_m)+"\n"
            self.counts["e_m"] = self.met_eff[2]

                           

    # do not use this as selections have chanegd too much for any of this to make sense anymore
    def finish_comparison(self):
        """ compares with values from imperial """
        # for muons 
        eb_11_m = 49.7
        eb_21_m = 50.4
        eb_22_m = 26.2
        el_1_m  = 84.7
        el_2_m  = 84.0
        er_11_m = 81.8
        er_21_m = 13.1
        er_12_m = 1.10
        er_22_m = 77.2
        er_01_m = 0.78
        er_02_m = 0.01
        rfact_m = 12.9
        al_1_m  = 88.2
        al_2_m  = 88.9 
        # for electrons
        eb_11_e = 49.7
        eb_21_e = 49.5
        eb_22_e = 26.8
        el_1_e  = 62.9
        el_2_e  = 63.7
        er_11_e = 71.6
        er_21_e = 13.1
        er_12_e = 1.10
        er_22_e = 69.9
        er_01_e = 0.78
        er_02_e = 0.02
        rfact_e = 12.9
        al_1_e  = 84.4
        al_2_e  = 83.8
        # printing comparisons A_l:
        all_ok = True
        if hasattr(self,"a_l"):
            self.out += "--------------------------------------\n"
            self.out += "A_l comparison:\ta_l_1\ta_l_2\n"
            self.out += "this study    :\t%.2f\t%.2f\n" % (self.a_l[1], self.a_l[2])
        else:
            all_ok = False
            print "no events in a_l"
        # self.out += "imp, electrons:\t%.2f\t%.2f\n" % (al_1_e, al_2_e)
        # self.out += "imp, muons    :\t%.2f\t%.2f\n" % (al_1_m, al_2_m)
        # E_r
        if hasattr(self,"e_r_norm"):
            self.out += "--------------------------------------\n"
            self.out += "e_r comparison:\te_r_11\te_r_12\te_r_21\te_r_22\tR\n"
            self.out += "this study    :\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" % (self.e_r_norm[1][1], self.e_r_norm[2][1], self.e_r_norm[1][2], self.e_r_norm[2][2], self.rfact)
        else:
            all_ok = False
            print "no events in e_r"
        # self.out += "imp, electrons:\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" % (er_11_e, er_12_e, er_21_e, er_22_e, rfact_e)
        # self.out += "imp, muons    :\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" % (er_11_m, er_12_m, er_21_m, er_22_m, rfact_m)
        # E_l
        if hasattr(self,"e_l"):
            self.out += "--------------------------------------\n"
            self.out += "e_l comparison:\te_l_1\te_l_2\n"
            self.out += "this study    :\t%.2f\t%.2f\n" % (self.e_l[1], self.e_l[2])
        else:
            all_ok = False
            print "no events in e_l"
        # self.out += "imp, electrons:\t%.2f\t%.2f\n" % (el_1_e, el_2_e)
        # self.out += "imp, muons    :\t%.2f\t%.2f\n" % (el_1_m, el_2_m)
        # E_b
        if hasattr(self,"e_b_he_norm"):
            self.out += "--------------------------------------\n"
            self.out += "e_b comparison:\te_b_11\te_b_21\te_b_22\n"
            self.out += "this study    :\t%.2f\t%.2f\t%.2f\n" % (self.e_b_he_norm[1][1], self.e_b_he_norm[1][2], self.e_b_he_norm[2][2])
        else:
            all_ok = False
            print "no events in e_b"
        # self.out += "imp, electrons:\t%.2f\t%.2f\t%.2f\n" % (eb_11_e, eb_21_e, eb_22_e)
        # self.out += "imp, muons    :\t%.2f\t%.2f\t%.2f\n" % (eb_11_m, eb_21_m, eb_22_m)
        # full matrix comparison
        self.out += "--------------------------------------\n"
        print self.out

        if not hasattr(self,"e_m"): self.e_m = 0.
        if all_ok:
            vals = {"al_1":self.a_l[1], "al_2":self.a_l[2],
                "el_1":self.e_l[1], "el_2":self.e_l[2],
                "er_01":self.e_r_norm[1][0]/100., "er_02":self.e_r_norm[2][0]/100., 
                "er_11":self.e_r_norm[1][1]/100., "er_12":self.e_r_norm[2][1]/100.,
                "er_21":self.e_r_norm[1][2]/100., "er_22":self.e_r_norm[2][2]/100.,
                "rfact":self.rfact,
                "eb_11":self.e_b_he_norm[1][1]/100., "eb_21":self.e_b_he_norm[1][2]/100., "eb_22":self.e_b_he_norm[2][2]/100.,
                "em_22":self.e_m
                }
            try: 
                this_mat = compute_fullmatrix(**vals)
            except:
                print "Matrix is singular, most likely statistics is not high enough"
            else:
                print this_mat
      
        # the end
        self.out += "--------------------------------------\n"


    def start_weights(self):
        self.pu_engine = LumiReWeighting()
        self.el_engine = LeptonsReWeighting()
        self.btag_engine = btaggingWeight(0,999,0,999)

# helper functions

def compute_fullmatrix(al_1, al_2, el_1, el_2, er_01, er_02, er_11, er_12, er_21, er_22, rfact, eb_11, eb_21, eb_22, em_22):
    # arguments should be normalized to 1 (not 100)
    # making matrices:
    try:
        al_mat = np.matrix([[1/al_1, 0],[0, 1/al_2]])
    except ZeroDivisionError:
        print "A_l_1 or A_l_2 is empty"
        return None
    print "A_l-1 :", al_mat
    er_mat = np.matrix([[er_11 + er_01*rfact, er_21 + er_01*rfact],[er_12 + er_02*rfact, er_22 + er_02*rfact]]).getI()
    print "e_r-1 :", er_mat
    try:
        el_mat = np.matrix([[1/el_1, 0],[0, 1/el_2]])
    except ZeroDivisionError:
        print "e_l_1 or e_l_2 is empty"
        return None
    print "e_l-1 :", el_mat
    try:
        eb_mat = np.matrix([[1/eb_11, -eb_21/(eb_22*eb_11)],[0, 1/eb_22]]) 
    except ZeroDivisionError:
        print "e_b_11 or e_b_22 is empty"
        return None
    print "e_b-1 :", eb_mat
    try:
        em_mat = np.matrix([[1, 0],[0, 1/em_22]]) 
    except ZeroDivisionError:
        print "em_22 is empty"
        return None
    print "e_m-1 :", em_mat
    final_mat = al_mat*er_mat*el_mat*eb_mat*em_mat
    return final_mat

def acc_pt_eta(vec, ptcut, etacut):
    if (math.fabs(vec.eta()) > etacut) or (vec.pt() < ptcut): return False
    return True

def jet_b_parton(genjet):
    """ returns the first b quark in jet based on first particle path (this is not sufficient), or the initial parton """
    cons0 = genjet.getGenConstituent(0)
    while True:
        if cons0.numberOfMothers() and cons0.mother(0).pdgId() != 2212 and math.fabs(cons0.pdgId()) != 5:
            cons0 = cons0.mother(0)
        else:
            return cons0

def user_members(obj):
    from inspect import getmembers
    return dict([mem for mem in getmembers(obj) if mem[0][0] != "_"])

def is_equal(vec1,vec2):
    if vec1 and vec2:
        return vec1.pt() == vec2.pt() and vec1.eta() == vec2.eta() and vec1.phi() == vec2.phi() and vec1.pdgId() == vec2.pdgId()
    return False

def get_vec(part):
    return ROOT.TLorentzVector(part.px(), part.py(), part.pz(), part.energy())

def delta_phi(phi1, phi2):
    deltaphi = math.fabs(phi1 - phi2)
    if deltaphi > math.pi:
        return 2*math.pi - deltaphi
    return deltaphi

def overlap(vec, collection, dr):
    for obj in collection:
        if math.hypot((vec.eta() - obj.eta()), delta_phi(vec.phi(), obj.phi())) < dr: return True
    return False

def match_obo(rec, gen, dr):
    gen2 = deepcopy(gen)
    matching = []
    for vec in rec:
        in_cone = []
        for part in gen2:
            deltar = math.hypot((vec.eta() - part.eta()), delta_phi(vec.phi(), part.phi()))
            if deltar < dr: in_cone.append([deltar, part])
        if in_cone:
            bestmatch = min(in_cone)[1]
            matching.append(vec)
            gen2.remove(bestmatch)
    return matching

def norm_by_column(mat):
    """ only for matrices with positive values """
    cols = len(mat[0])
    norms = [0]*cols
    for i in range(cols):
        for row in mat:
            norms[i] += row[i]
    for j, row in enumerate(mat):
        for i, el in enumerate(row):
            if norms[i]:
                mat[j][i] = el/float(norms[i]) * 100
    return norms

def norm_columns_from_vec(mat, vec):
    """ normalise matrix elements using vector to define column sums"""
    cols = len(mat[0])
    if len(vec) != cols:
        print "Vector has size",len(vec),"while matrix has",cols,"columns, aborting"
        return 1
    for j, row in enumerate(mat):
        for i, el in enumerate(row):
            mat[j][i] = vec[i] and el/float(vec[i]) * 100 or 0
    return vec

def norm_by_line(mat):
    for i, row in enumerate(mat):
        norm = sum(row)
        if norm:
            mat[i] = [el/float(norm) for el in row]
    return [0]*len(mat[0])

def f_2(num):
    return "%.2f" % (num)

def is_bhad(genpart):
    pdgid = math.fabs(genpart.pdgId())
    return (499 < pdgid < 600) or (4999 < pdgid < 6000)

def is_final_bhad(genpart):
    if not is_bhad(genpart): return False
    if len([genpart.daughter(i) for i in range(genpart.numberOfDaughters()) if is_bhad(genpart.daughter(i))]): return False
    return True

def compare_matrices():
    vals_imp_mu = {"al_1":0.882, "al_2":0.889, "el_1":0.847, "el_2":0.840, "er_01":0.008, "er_02":0.000, 
        "er_11":0.818, "er_12":0.011, "er_21":0.131, "er_22":0.772, "rfact":12.17, "eb_11":0.497, "eb_21":0.504, "eb_22":0.262}
    vals_imp_el = {"al_1":0.844, "al_2":0.838, "el_1":0.629, "el_2":0.637, "er_01":0.008, "er_02":0.000, 
        "er_11":0.716, "er_12":0.011, "er_21":0.102, "er_22":0.699, "rfact":12.93, "eb_11":0.497, "eb_21":0.495, "eb_22":0.268} 
    vals_cp3_mu = {"al_1":0.910, "al_2":0.910, "el_1":0.730, "el_2":0.700, "er_01":0.000, "er_02":0.000, 
        "er_11":0.836, "er_12":0.002, "er_21":0.228, "er_22":0.740, "rfact":212.4, "eb_11":0.507, "eb_21":0.470, "eb_22":0.276} 
    vals_cp3_el = {"al_1":0.860, "al_2":0.860, "el_1":0.640, "el_2":0.620, "er_01":0.000, "er_02":0.000, 
        "er_11":0.839, "er_12":0.002, "er_21":0.244, "er_22":0.724, "rfact":180.8, "eb_11":0.502, "eb_21":0.500, "eb_22":0.157}
    print "cp3, electrons:"
    print compute_fullmatrix(**vals_cp3_el)
    print "imperial, electrons:" 
    print compute_fullmatrix(**vals_imp_el)
    print "cp3, muons:"
    print compute_fullmatrix(**vals_cp3_mu)
    print "imperial, muons:"
    print compute_fullmatrix(**vals_imp_mu)

def sum_scalvecmat(dict, dict2):
    """ adds values from dict2 to dict1 keys. adds missing keys. works only to D=2 (no tensors) """
    dict1 = deepcopy(dict)
    for key, val in dict2.items():
        if key in dict1:
            # sum with previous value
            if not type(val) == type([]):
                # it's a scalar, easy
                dict1[key] += val
            elif not type(val[0]) == type([]):
                # it's a vector (we hope)
                dict1[key] = [x+y for x,y in zip(dict1[key],dict2[key])]
            else:
                # it's a matrix
                for i, line in enumerate(dict1[key]):
                    dict1[key][i] = [x+y for x,y in zip(line,dict2[key][i])]
        else:
            dict1[key] = val
    return dict1
    

def beanstalk_worker(muchannel, jobid):
    sys.path.append("/home/fynu/jdf")
    from beanstalk import beanstalkc
    beanstalk = beanstalkc.Connection(host='10.1.1.21', port=11300)
    if muchannel == None:
        mu_options = "_b"
    elif muchannel == True:
        mu_options = "_m"
    elif muchannel == False:
        mu_options = "_e"

    user = get_username()
    jobqueue = "unfolding_queue_%s%s_%s" % (user, mu_options, jobid)
    resqueue = "unfolding_resqueue_%s%s_%s" % (user, mu_options, jobid)
    beanstalk.watch(jobqueue)
    job = beanstalk.reserve(timeout=5)
    scratch_dir = os.environ["_CONDOR_SCRATCH_DIR"]
    input_file = os.path.join(scratch_dir,"input.root")
    if job:
        hostname = os.uname()[1]
        print "Running on", job.body
        body = job.body
        job.delete()
        beanstalk.close()
        shutil.copy(body,input_file)
        output = {"host":hostname, "arg":job.body, "out":main(dataset=input_file, muchannel=muchannel, save_output=False)}
        os.remove(input_file)
        output = pickle.dumps(output)
        beanstalk = beanstalkc.Connection(host='10.1.1.21', port=11300)
        beanstalk.use(resqueue)
        beanstalk.put(output)
    beanstalk.close()


def purge_queue(queue_name):
    sys.path.append("/home/fynu/jdf")
    from beanstalk import beanstalkc
    beanstalk = beanstalkc.Connection(host='10.1.1.21', port=11300)
    queue_to_purge = queue_name
    beanstalk.watch(queue_to_purge)
    while True:
        job = beanstalk.reserve(timeout=0)
        if job:
            print job.body
            job.delete()
        else:
            break
    beanstalk.close()


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def beanstalk_client(path_to_files, muchannel, jobid):
    ## this still needs a proper handling of errors, for instance if not all jobs come back
    # yaml and beanstalk are there, it is needed
    sys.path.append("/home/fynu/jdf")
    from beanstalk import beanstalkc
    beanstalk = beanstalkc.Connection(host='10.1.1.21', port=11300)
    # queue names have to change as a function of user to avoid filling each other's queue
    if muchannel == None:
        mu_options = "_b"
    elif muchannel == True:
        mu_options = "_m"
    elif muchannel == False:
        mu_options = "_e"
    user = get_username()
    if not jobid:
        qtubes = [tube for tube in beanstalk.tubes() if user in tube and "unfolding_queue" in tube]
        rtubes = [tube for tube in beanstalk.tubes() if user in tube and "unfolding_resqueue" in tube]
        if qtubes:
            print "The following tubes have jobs queued/running:"
            for tube in qtubes:
                restube = tube.replace("queue","resqueue",1)
                waiting = beanstalk.stats_tube(tube)["current-jobs-ready"]
                reserved = beanstalk.stats_tube(tube)["current-jobs-reserved"]
                try:
                    done = beanstalk.stats_tube(restube)["current-jobs-ready"]
                except:
                    done = 0
                print tube.split("_",4)[4], ", waiting:",waiting,"reserved:",reserved,"done:",done
        if rtubes:
            print "The following tubes have results ready:"
            for tube in rtubes:
                print tube.split("_",4)[4], ", done:",beanstalk.stats_tube(tube)["current-jobs-ready"]
        jobid = raw_input("Please enter desired job id (or nothing to abort):\n")
        if not jobid:
            print "No jobid, aborting"
            sys.exit(1)
    jobqueue = "unfolding_queue_%s%s_%s" % (user, mu_options, jobid)
    resqueue = "unfolding_resqueue_%s%s_%s" % (user, mu_options, jobid)
    beanstalk.use(jobqueue)
    beanstalk.watch(resqueue)

    files = os.path.isdir(path_to_files) and glob.glob(os.path.join(path_to_files,"*")) or [path_to_files]
    files = files[:10]
    nfiles = len(files)

    fill = True
    submit = True
    res_len = 0
    if beanstalk.stats_tube(resqueue)["current-jobs-ready"] > 0:
        print "There are results waiting: no new jobs submitted, just fetching results."
        submit = False
        fill = False
        res_len = beanstalk.stats_tube(resqueue)["current-jobs-ready"]
    elif beanstalk.stats_tube(jobqueue)["current-jobs-ready"] > 0:
        print "There are %i data files in queue, purging" % (beanstalk.stats_tube(jobqueue)["current-jobs-ready"])
        purge_queue(jobqueue)
        print "Queue is now empty"
        sys.exit(0)
    elif beanstalk.stats_tube(jobqueue)["current-jobs-reserved"] > 0:
        print "There are data files reserved, jobs are still running, quitting"
        sys.exit(1)

    if fill:
        print "Filling the queue with %i jobs" % (nfiles)
        for file in files:
            beanstalk.put(file)

    if submit:
        # write condor cmd file
        condfile = open("unfolding_worker_%s.cmd" % (jobid),"w")
        text = """
executable = unfolding_worker_%s.sh
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
universe = vanilla
requirements = (CMSFARM =?= TRUE)
output         = condor/beans.$(Cluster).$(Process).out
error          = condor/beans.$(Cluster).$(Process).err
log            = condor/beans.$(Cluster).$(Process).log
""" % (jobid)
        condfile.write(text)
        condfile.write("queue %i" % (nfiles))
        condfile.close()

        if options.muchannel == None:
            mu_options = "-b"
        elif options.muchannel == True:
            mu_options = "-m"
        elif options.muchannel == False:
            mu_options = "-e"

        # write condor sh file
        thisdir = os.getcwd()
        shname  = "unfolding_worker_%s.sh" % (jobid)
        submitcmd = "condor_submit unfolding_worker_%s.cmd" % (jobid) 
        thisfile = os.path.basename(__file__)
        shfile = open(shname,"w")
        shfile.write("cd %s\n" % (thisdir))
        text = """
source /nfs/soft/cms/cmsset_default.sh
eval `scramv1 runtime -sh`
python %s -w %s -j %s
""" % (thisfile, mu_options, jobid)
        shfile.write(text)
        shfile.close()
        os.chmod(shname,0755)

        # submit condor jobs
        print "Submitting condor jobs"
        commands.getstatusoutput(submitcmd)
        print "Done"
        cont = ""
        while cont not in ["Y","y","N","n"]:
            cont = raw_input("Do you want to wait for results (Y/N) ? ")
        if cont in ["N","n"]:
            print "Exiting. Run this script again when all jobs are done to get results"
            sys.exit(0)

    outs = []
    processed = 0
    counts = {}
    if res_len: nfiles=res_len
    while processed < nfiles:
        job = beanstalk.reserve()
        out = pickle.loads(job.body)
        outs.append(out["out"])
        counts = sum_scalvecmat(counts, out["out"])
        processed += 1
        print "==================================="
        print "got output from", out["host"], " on file:", out["arg"]
        print "temp results:"
        for key, value in counts.items():
            print key,":", value
        print "==================================="
        try:
            counts_to_mats(counts)
        except:
            print "this job returned ill results, skipping"
        print "==================================="
        job.delete()

    beanstalk.close()

    print "=== everybody's back ==="
    for key, value in counts.items():
        print key,":", value
    print "========================================"
    print "Don't forget to condor_rm remaining jobs"
    print "========================================"
    counts_to_mats(counts)
    # print "===     details      ==="
    # print outs

def counts_to_mats(counts_1):
    counts = deepcopy(counts_1)
    print "==================================="
    for key, value in counts.items():
        print key,":", value
    print "==================================="     
        
    total = counts.get("All",0)
    e_r = counts.get("e_r",[[0,0,0],[0,0,0],[0,0,0]])
    # here set which matrix you want to use
    e_b = counts.get("e_b_he",[[0,0,0],[0,0,0],[0,0,0]])
    e_l = counts.get("e_l",[0,0,0])
    e_m = counts.get("e_m",0.)

    # normalization
    # first normalize e_met, using the unnormalized e_b
    try:
        em_22 = e_m/(e_b[2][2])    
    except ZeroDivisionError:
        em_22 = 0.
    # then normalize the rest
    norms_rec_er = [sum(line) for line in e_r]
    norms = norm_by_column(e_r)
    rfact = (norms[1]+norms[2]) and norms[0]/float(norms[1]+norms[2]) or 0
    norms_e_b = norm_columns_from_vec(e_b,e_l)
    e_l = [x/y if y > 0 else 0 for x,y in zip(e_l,norms_rec_er)]

    print "rfact:", rfact
    print "e_r:", e_r
    print "e_l:", e_l
    print "e_b:", e_b
    print "e_m:", e_m


    vals = {"al_1":1.0, "al_2":1.0,
            "el_1":e_l[1], "el_2":e_l[2],
            "er_01":e_r[1][0]/100., "er_02":e_r[2][0]/100.,
            "er_11":e_r[1][1]/100., "er_12":e_r[2][1]/100.,
            "er_21":e_r[1][2]/100., "er_22":e_r[2][2]/100.,
            "rfact":rfact,
            "eb_11":e_b[1][1]/100., "eb_21":e_b[1][2]/100., "eb_22":e_b[2][2]/100.,
            "em_22":em_22
        }
    try:
        print compute_fullmatrix(**vals)
    except:
        print "Could not compute matrices. Probably not enough statistics" 


def main(dataset="/storage/data/cms/users/llbb/productionJune2012_444/ZbSkims/Zbb_MC/", muchannel = None, num = -1, save_output = True):
    startup = ["weights"]
    steps = ["event_weight","a_l", "e_r", "e_l", "e_b","e_m"]
    finish = ["print_a_l", "print_e_r", "print_e_l", "print_e_b", "print_e_m", "comparison"]
    testu = unfolder(dataset, steps, startup, finish, muchannel, save_output)
    testu.run(num)
    return testu.counts

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(description="Compute unfolding matrices from MC dataset")
    parser.add_option("-d", "--dataset", type="string", dest="dataset", help="Path to root file or directory containing root files")
    parser.add_option("-m", action="store_const", const=True,  dest="muchannel", help="Muon channel", default=None)
    parser.add_option("-e", action="store_const", const=False, dest="muchannel", help="Electron channel")
    parser.add_option("-b", action="store_const", const=None,  dest="muchannel", help="Both lepton channels (default)")
    parser.add_option("-n", type="int", dest="num", help="Number of events to process, defaults to all", default=-1)
    parser.add_option("-c","--condor", action="store_const", const=True, dest="condor", help="create condor file, do not run anything", default=False)
    parser.add_option("-i","--interactive", action="store_const", const=True, dest="beanstalk_c", help="run in semi-interactive mode", default=False)
    parser.add_option("-j", "--jobid", type="string", dest="jobid", help="job identifier, (no spaces or special chars please)", default = "")
    parser.add_option("-w","--worker", action="store_const", const=True, dest="beanstalk_w", help="wait for jobs in queue, do not use", default=False)
    (options, args) = parser.parse_args()
    if not options.dataset and not options.beanstalk_w:
        print
        print "ERROR: You should specify a dataset"
        print
        parser.print_help()
        exit(-1)
    
    if not options.beanstalk_w:
        print "Running on:", options.dataset
        if options.num > 0: 
            print "Running on", options.num, "first events"
        else:
            print "Running on all events"
        if options.muchannel == None:
            print "For both electrons and muons"
        elif options.muchannel == True:
            print "For muons only"
        elif options.muchannel == False:
            print "For electrons only"

    # caution: muchannel is always True here !
    if options.condor:
        thisdir = os.getcwd() 
        condfile = open("condor_unfolding.cmd","w")
        infiles = os.path.isdir(options.dataset) and glob.glob(os.path.join(options.dataset,"*")) or [options.dataset]
        condfile.write("executable = condor_unfolding.sh\n")
        condfile.write("should_transfer_files = YES\n")
        condfile.write("when_to_transfer_output = ON_EXIT\n")
        condfile.write("universe = vanilla\n")
        condfile.write("requirements = (CMSFARM =?= TRUE)\n\n")
        for file in infiles:
            condfile.write("arguments = %s\n" % (file))
            file = os.path.basename(file)
            file = os.path.splitext(file)[0]
            condfile.write("output = condor/%s.out\n" % (file))
            condfile.write("error  = condor/%s.err\n" % (file))
            condfile.write("log    = condor/%s.log\n" % (file))
            condfile.write("queue\n\n")
        condfile.close()
        shfile = open("condor_unfolding.sh","w")
        shfile.write("cd %s\n" % (thisdir))
        shfile.write("source /nfs/soft/cms/cmsset_default.sh\n")
        shfile.write("eval `scramv1 runtime -sh`\n")
        shfile.write("python compute_unfolding_matrices.py -m -d $1\n")
        shfile.close()
        os.chmod("condor_unfolding.sh",0755)
    elif options.beanstalk_c:
        beanstalk_client(options.dataset, options.muchannel, options.jobid)
    elif options.beanstalk_w:
        beanstalk_worker(options.muchannel, options.jobid)
    else:
        main(options.dataset, options.muchannel, options.num)


