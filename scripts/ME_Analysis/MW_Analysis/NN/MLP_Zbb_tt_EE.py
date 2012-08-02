from math import exp

from math import tanh

class ../NN/MLP_Zbb_tt_EE:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 21.6321)/1.05575
		self.input1 = (in1 - 20.9125)/1.08293
		self.input2 = (in2 - 21.6884)/0.800382
		self.input3 = (in3 - 65.8143)/37.6943
		if index==0: return self.neuron0x84e43f0();
		return 0.
	def neuron0x84e2230(self):
		return self.input0
	def neuron0x84e2540(self):
		return self.input1
	def neuron0x84e2850(self):
		return self.input2
	def neuron0x84e2b60(self):
		return self.input3
	def neuron0x84e2fe0(self):
		input = 3.91307
		input = input + self.synapse0x7eedcc0()
		input = input + self.synapse0x84e3260()
		input = input + self.synapse0x84e32a0()
		input = input + self.synapse0x84e32e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x84e3320(self):
		input = -4.78883
		input = input + self.synapse0x84e3630()
		input = input + self.synapse0x84e3670()
		input = input + self.synapse0x84e36b0()
		input = input + self.synapse0x84e36f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x84e3730(self):
		input = 0.183607
		input = input + self.synapse0x84e3a40()
		input = input + self.synapse0x84e3a80()
		input = input + self.synapse0x84e3ac0()
		input = input + self.synapse0x84e3b00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x84e3b40(self):
		input = -0.727824
		input = input + self.synapse0x84e3e50()
		input = input + self.synapse0x84e3e90()
		input = input + self.synapse0x84e3ed0()
		input = input + self.synapse0x84e3f10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x84e3f50(self):
		input = 0.678719
		input = input + self.synapse0x84e4260()
		input = input + self.synapse0x7ec7c50()
		input = input + self.synapse0x7ec7c90()
		input = input + self.synapse0x84e43b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x84e43f0(self):
		input = 0.0873911
		input = input + self.synapse0x84e4700()
		input = input + self.synapse0x84e4740()
		input = input + self.synapse0x84e4780()
		input = input + self.synapse0x84e47c0()
		input = input + self.synapse0x84e4800()
		return (input*1)+0
	def synapse0x7eedcc0(self):
		return (self.neuron0x84e2230()*1.06069)
	def synapse0x84e3260(self):
		return (self.neuron0x84e2540()*0.878525)
	def synapse0x84e32a0(self):
		return (self.neuron0x84e2850()*-1.09927)
	def synapse0x84e32e0(self):
		return (self.neuron0x84e2b60()*2.92194)
	def synapse0x84e3630(self):
		return (self.neuron0x84e2230()*-0.994501)
	def synapse0x84e3670(self):
		return (self.neuron0x84e2540()*-0.954715)
	def synapse0x84e36b0(self):
		return (self.neuron0x84e2850()*1.57134)
	def synapse0x84e36f0(self):
		return (self.neuron0x84e2b60()*-3.78254)
	def synapse0x84e3a40(self):
		return (self.neuron0x84e2230()*0.367564)
	def synapse0x84e3a80(self):
		return (self.neuron0x84e2540()*0.140711)
	def synapse0x84e3ac0(self):
		return (self.neuron0x84e2850()*0.633645)
	def synapse0x84e3b00(self):
		return (self.neuron0x84e2b60()*0.639149)
	def synapse0x84e3e50(self):
		return (self.neuron0x84e2230()*-1.11863)
	def synapse0x84e3e90(self):
		return (self.neuron0x84e2540()*-1.35516)
	def synapse0x84e3ed0(self):
		return (self.neuron0x84e2850()*0.649655)
	def synapse0x84e3f10(self):
		return (self.neuron0x84e2b60()*-0.809122)
	def synapse0x84e4260(self):
		return (self.neuron0x84e2230()*0.0529839)
	def synapse0x7ec7c50(self):
		return (self.neuron0x84e2540()*-0.0992181)
	def synapse0x7ec7c90(self):
		return (self.neuron0x84e2850()*0.557022)
	def synapse0x84e43b0(self):
		return (self.neuron0x84e2b60()*0.373086)
	def synapse0x84e4700(self):
		return (self.neuron0x84e2fe0()*0.0255088)
	def synapse0x84e4740(self):
		return (self.neuron0x84e3320()*1.01198)
	def synapse0x84e4780(self):
		return (self.neuron0x84e3730()*0.139235)
	def synapse0x84e47c0(self):
		return (self.neuron0x84e3b40()*0.0446161)
	def synapse0x84e4800(self):
		return (self.neuron0x84e3f50()*-0.289454)
