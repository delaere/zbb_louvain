from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_9:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.467176)/0.243159
		self.input1 = (in1 - 0.52708)/0.296356
		self.input2 = (in2 - 0.534793)/0.314261
		if index==0: return self.neuron0x2841f170();
		return 0.
	def neuron0x2841d750(self):
		return self.input0
	def neuron0x2841da90(self):
		return self.input1
	def neuron0x2841ddd0(self):
		return self.input2
	def neuron0x2841e240(self):
		input = 5.94125
		input = input + self.synapse0x283c2830()
		input = input + self.synapse0x2841e4f0()
		input = input + self.synapse0x2841e530()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2841e570(self):
		input = 3.39967
		input = input + self.synapse0x2841e8b0()
		input = input + self.synapse0x2841e8f0()
		input = input + self.synapse0x2841e930()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2841e970(self):
		input = -1.50806
		input = input + self.synapse0x2841ecb0()
		input = input + self.synapse0x2841ecf0()
		input = input + self.synapse0x2841ed30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2841ed70(self):
		input = 1.73542
		input = input + self.synapse0x2841f0b0()
		input = input + self.synapse0x2841f0f0()
		input = input + self.synapse0x2841f130()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2841f170(self):
		input = -4.27819
		input = input + self.synapse0x2841f4b0()
		input = input + self.synapse0x2841f4f0()
		input = input + self.synapse0x2841f530()
		input = input + self.synapse0x2841f570()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x283c2830(self):
		return (self.neuron0x2841d750()*-0.927533)
	def synapse0x2841e4f0(self):
		return (self.neuron0x2841da90()*-1.91728)
	def synapse0x2841e530(self):
		return (self.neuron0x2841ddd0()*-0.442914)
	def synapse0x2841e8b0(self):
		return (self.neuron0x2841d750()*1.01507)
	def synapse0x2841e8f0(self):
		return (self.neuron0x2841da90()*0.819626)
	def synapse0x2841e930(self):
		return (self.neuron0x2841ddd0()*-0.474331)
	def synapse0x2841ecb0(self):
		return (self.neuron0x2841d750()*-1.779)
	def synapse0x2841ecf0(self):
		return (self.neuron0x2841da90()*2.50767)
	def synapse0x2841ed30(self):
		return (self.neuron0x2841ddd0()*0.910969)
	def synapse0x2841f0b0(self):
		return (self.neuron0x2841d750()*0.27185)
	def synapse0x2841f0f0(self):
		return (self.neuron0x2841da90()*-0.18447)
	def synapse0x2841f130(self):
		return (self.neuron0x2841ddd0()*0.876041)
	def synapse0x2841f4b0(self):
		return (self.neuron0x2841e240()*-7.43548)
	def synapse0x2841f4f0(self):
		return (self.neuron0x2841e570()*8.52666)
	def synapse0x2841f530(self):
		return (self.neuron0x2841e970()*-1.26515)
	def synapse0x2841f570(self):
		return (self.neuron0x2841ed70()*4.76686)
