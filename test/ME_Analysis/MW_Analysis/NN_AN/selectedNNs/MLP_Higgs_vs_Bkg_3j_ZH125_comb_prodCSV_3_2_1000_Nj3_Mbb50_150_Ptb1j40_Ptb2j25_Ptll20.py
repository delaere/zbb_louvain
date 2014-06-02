from math import exp

from math import tanh

class Final11/MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_3_2_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 0.46033)/0.237691
		self.input1 = (in1 - 0.512403)/0.275496
		self.input2 = (in2 - 0.527936)/0.286352
		self.input3 = (in3 - 0.639559)/0.256908
		if index==0: return self.neuron0x3c605c80();
		return 0.
	def neuron0x3c603a10(self):
		return self.input0
	def neuron0x3c603d50(self):
		return self.input1
	def neuron0x3c604090(self):
		return self.input2
	def neuron0x3c6043d0(self):
		return self.input3
	def neuron0x3c604840(self):
		input = 3.06454
		input = input + self.synapse0x3c5f2c70()
		input = input + self.synapse0x3c580cd0()
		input = input + self.synapse0x3c580d10()
		input = input + self.synapse0x3c604af0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3c604b30(self):
		input = -3.06524
		input = input + self.synapse0x3c604e70()
		input = input + self.synapse0x3c604eb0()
		input = input + self.synapse0x3c604ef0()
		input = input + self.synapse0x3c604f30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3c604f70(self):
		input = 1.26953
		input = input + self.synapse0x3c6052b0()
		input = input + self.synapse0x3c6052f0()
		input = input + self.synapse0x3c605330()
		input = input + self.synapse0x3c605370()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3c6053b0(self):
		input = -3.61494
		input = input + self.synapse0x3c6056f0()
		input = input + self.synapse0x3c605730()
		input = input + self.synapse0x3c605770()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3c6057b0(self):
		input = 4.00689
		input = input + self.synapse0x3c605af0()
		input = input + self.synapse0x3c605b30()
		input = input + self.synapse0x3c580830()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3c605c80(self):
		input = 0.0596264
		input = input + self.synapse0x3c605ea0()
		input = input + self.synapse0x3c605ee0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x3c5f2c70(self):
		return (self.neuron0x3c603a10()*0.0789822)
	def synapse0x3c580cd0(self):
		return (self.neuron0x3c603d50()*-0.00446146)
	def synapse0x3c580d10(self):
		return (self.neuron0x3c604090()*1.43575)
	def synapse0x3c604af0(self):
		return (self.neuron0x3c6043d0()*-0.733502)
	def synapse0x3c604e70(self):
		return (self.neuron0x3c603a10()*1.06431)
	def synapse0x3c604eb0(self):
		return (self.neuron0x3c603d50()*-0.31494)
	def synapse0x3c604ef0(self):
		return (self.neuron0x3c604090()*0.482415)
	def synapse0x3c604f30(self):
		return (self.neuron0x3c6043d0()*0.195342)
	def synapse0x3c6052b0(self):
		return (self.neuron0x3c603a10()*1.05861)
	def synapse0x3c6052f0(self):
		return (self.neuron0x3c603d50()*0.0476278)
	def synapse0x3c605330(self):
		return (self.neuron0x3c604090()*-0.468373)
	def synapse0x3c605370(self):
		return (self.neuron0x3c6043d0()*0.534139)
	def synapse0x3c6056f0(self):
		return (self.neuron0x3c604840()*-0.443136)
	def synapse0x3c605730(self):
		return (self.neuron0x3c604b30()*5.25324)
	def synapse0x3c605770(self):
		return (self.neuron0x3c604f70()*2.14199)
	def synapse0x3c605af0(self):
		return (self.neuron0x3c604840()*-3.99508)
	def synapse0x3c605b30(self):
		return (self.neuron0x3c604b30()*-1.75747)
	def synapse0x3c580830(self):
		return (self.neuron0x3c604f70()*-3.69247)
	def synapse0x3c605ea0(self):
		return (self.neuron0x3c6053b0()*6.58762)
	def synapse0x3c605ee0(self):
		return (self.neuron0x3c6057b0()*-9.26856)
