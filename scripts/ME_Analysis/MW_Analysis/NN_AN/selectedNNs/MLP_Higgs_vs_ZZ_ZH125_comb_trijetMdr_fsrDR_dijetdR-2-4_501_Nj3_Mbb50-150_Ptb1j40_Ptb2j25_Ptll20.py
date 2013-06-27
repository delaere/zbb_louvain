from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_ZZ_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_501_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4,in5,in6):
		self.input0 = (in0 - 21.2603)/1.24213
		self.input1 = (in1 - 10.925)/1.0292
		self.input2 = (in2 - 24.8133)/1.20085
		self.input3 = (in3 - 13.128)/1.2544
		self.input4 = (in4 - 8.01918)/31.6482
		self.input5 = (in5 - 1.81682)/0.811669
		self.input6 = (in6 - 1.95854)/0.692368
		if index==0: return self.neuron0x2dfb01b0();
		return 0.
	def neuron0x2dfad150(self):
		return self.input0
	def neuron0x2dfad490(self):
		return self.input1
	def neuron0x2dfad7d0(self):
		return self.input2
	def neuron0x2dfadb10(self):
		return self.input3
	def neuron0x2dfade50(self):
		return self.input4
	def neuron0x2dfae190(self):
		return self.input5
	def neuron0x2dfae4d0(self):
		return self.input6
	def neuron0x2dfae940(self):
		input = 3.26482
		input = input + self.synapse0x2df571f0()
		input = input + self.synapse0x2dfaebf0()
		input = input + self.synapse0x2dfaec30()
		input = input + self.synapse0x2dfaec70()
		input = input + self.synapse0x2dfaecb0()
		input = input + self.synapse0x2dfaecf0()
		input = input + self.synapse0x2dfaed30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2dfaed70(self):
		input = 0.145062
		input = input + self.synapse0x2dfaf0b0()
		input = input + self.synapse0x2dfaf0f0()
		input = input + self.synapse0x2dfaf130()
		input = input + self.synapse0x2dfaf170()
		input = input + self.synapse0x2dfaf1b0()
		input = input + self.synapse0x2dfaf1f0()
		input = input + self.synapse0x2dfaf230()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2dfaf270(self):
		input = -0.281069
		input = input + self.synapse0x2dfaf5b0()
		input = input + self.synapse0x2dfaf5f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2dfaf630(self):
		input = 0.196249
		input = input + self.synapse0x2dfaf970()
		input = input + self.synapse0x2cc4fa50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2dfafac0(self):
		input = 0.239937
		input = input + self.synapse0x2dfafd70()
		input = input + self.synapse0x2dfafdb0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2dfafdf0(self):
		input = 0.186459
		input = input + self.synapse0x2dfb0130()
		input = input + self.synapse0x2dfb0170()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2dfb01b0(self):
		input = 0.709598
		input = input + self.synapse0x2dfb04f0()
		input = input + self.synapse0x2dfb0530()
		input = input + self.synapse0x2dfb0570()
		input = input + self.synapse0x2dfb05b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x2df571f0(self):
		return (self.neuron0x2dfad150()*-0.624413)
	def synapse0x2dfaebf0(self):
		return (self.neuron0x2dfad490()*2.19807)
	def synapse0x2dfaec30(self):
		return (self.neuron0x2dfad7d0()*-1.37307)
	def synapse0x2dfaec70(self):
		return (self.neuron0x2dfadb10()*-0.15223)
	def synapse0x2dfaecb0(self):
		return (self.neuron0x2dfade50()*0.0467743)
	def synapse0x2dfaecf0(self):
		return (self.neuron0x2dfae190()*-0.231604)
	def synapse0x2dfaed30(self):
		return (self.neuron0x2dfae4d0()*0.23783)
	def synapse0x2dfaf0b0(self):
		return (self.neuron0x2dfad150()*-0.243255)
	def synapse0x2dfaf0f0(self):
		return (self.neuron0x2dfad490()*0.0453616)
	def synapse0x2dfaf130(self):
		return (self.neuron0x2dfad7d0()*0.0189165)
	def synapse0x2dfaf170(self):
		return (self.neuron0x2dfadb10()*0.319285)
	def synapse0x2dfaf1b0(self):
		return (self.neuron0x2dfade50()*0.0197834)
	def synapse0x2dfaf1f0(self):
		return (self.neuron0x2dfae190()*-0.0525457)
	def synapse0x2dfaf230(self):
		return (self.neuron0x2dfae4d0()*0.130258)
	def synapse0x2dfaf5b0(self):
		return (self.neuron0x2dfae940()*1.8961)
	def synapse0x2dfaf5f0(self):
		return (self.neuron0x2dfaed70()*-2.8178)
	def synapse0x2dfaf970(self):
		return (self.neuron0x2dfae940()*1.31506)
	def synapse0x2cc4fa50(self):
		return (self.neuron0x2dfaed70()*-2.54901)
	def synapse0x2dfafd70(self):
		return (self.neuron0x2dfae940()*-1.60978)
	def synapse0x2dfafdb0(self):
		return (self.neuron0x2dfaed70()*2.36786)
	def synapse0x2dfb0130(self):
		return (self.neuron0x2dfae940()*-1.78024)
	def synapse0x2dfb0170(self):
		return (self.neuron0x2dfaed70()*3.38453)
	def synapse0x2dfb04f0(self):
		return (self.neuron0x2dfaf270()*4.76768)
	def synapse0x2dfb0530(self):
		return (self.neuron0x2dfaf630()*3.78289)
	def synapse0x2dfb0570(self):
		return (self.neuron0x2dfafac0()*-2.74774)
	def synapse0x2dfb05b0(self):
		return (self.neuron0x2dfafdf0()*-5.20935)
