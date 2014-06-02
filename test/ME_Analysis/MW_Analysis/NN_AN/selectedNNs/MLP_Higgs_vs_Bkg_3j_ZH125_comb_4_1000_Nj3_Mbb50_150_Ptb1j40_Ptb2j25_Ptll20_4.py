from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_4:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.467176)/0.243159
		self.input1 = (in1 - 0.52708)/0.296356
		self.input2 = (in2 - 0.534793)/0.314261
		if index==0: return self.neuron0x25593ed0();
		return 0.
	def neuron0x255924b0(self):
		return self.input0
	def neuron0x255927f0(self):
		return self.input1
	def neuron0x25592b30(self):
		return self.input2
	def neuron0x25592fa0(self):
		input = -4.55567
		input = input + self.synapse0x25537690()
		input = input + self.synapse0x25593250()
		input = input + self.synapse0x25593290()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x255932d0(self):
		input = -0.932204
		input = input + self.synapse0x25593610()
		input = input + self.synapse0x25593650()
		input = input + self.synapse0x25593690()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x255936d0(self):
		input = -4.08063
		input = input + self.synapse0x25593a10()
		input = input + self.synapse0x25593a50()
		input = input + self.synapse0x25593a90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x25593ad0(self):
		input = -1.85149
		input = input + self.synapse0x25593e10()
		input = input + self.synapse0x25593e50()
		input = input + self.synapse0x25593e90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x25593ed0(self):
		input = 1.40773
		input = input + self.synapse0x25537720()
		input = input + self.synapse0x25594210()
		input = input + self.synapse0x25594250()
		input = input + self.synapse0x25594290()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x25537690(self):
		return (self.neuron0x255924b0()*0.804113)
	def synapse0x25593250(self):
		return (self.neuron0x255927f0()*0.969853)
	def synapse0x25593290(self):
		return (self.neuron0x25592b30()*0.548829)
	def synapse0x25593610(self):
		return (self.neuron0x255924b0()*-0.930656)
	def synapse0x25593650(self):
		return (self.neuron0x255927f0()*1.11734)
	def synapse0x25593690(self):
		return (self.neuron0x25592b30()*0.510812)
	def synapse0x25593a10(self):
		return (self.neuron0x255924b0()*-1.21567)
	def synapse0x25593a50(self):
		return (self.neuron0x255927f0()*-1.19317)
	def synapse0x25593a90(self):
		return (self.neuron0x25592b30()*0.52627)
	def synapse0x25593e10(self):
		return (self.neuron0x255924b0()*-0.359804)
	def synapse0x25593e50(self):
		return (self.neuron0x255927f0()*0.0877854)
	def synapse0x25593e90(self):
		return (self.neuron0x25592b30()*-1.13552)
	def synapse0x25537720(self):
		return (self.neuron0x25592fa0()*8.39681)
	def synapse0x25594210(self):
		return (self.neuron0x255932d0()*-2.26312)
	def synapse0x25594250(self):
		return (self.neuron0x255936d0()*-6.63535)
	def synapse0x25594290(self):
		return (self.neuron0x25593ad0()*-3.43646)
