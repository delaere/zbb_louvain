from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_3_2_10000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x11ddaf20();
		return 0.
	def neuron0x11dc85d0(self):
		return self.input0
	def neuron0x11dc8910(self):
		return self.input1
	def neuron0x11dd98e0(self):
		return self.input2
	def neuron0x11dd9c30(self):
		input = -0.0885877
		input = input + self.synapse0x11d90e20()
		input = input + self.synapse0x11daf370()
		input = input + self.synapse0x11dd9ee0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11dd9f20(self):
		input = -7.30954
		input = input + self.synapse0x11dda260()
		input = input + self.synapse0x11dda2a0()
		input = input + self.synapse0x11dda2e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11dda320(self):
		input = -0.618381
		input = input + self.synapse0x11dda660()
		input = input + self.synapse0x11dda6a0()
		input = input + self.synapse0x11dda6e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11dda720(self):
		input = 9.94111
		input = input + self.synapse0x11ddaa60()
		input = input + self.synapse0x11ddaaa0()
		input = input + self.synapse0x11ddaae0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11ddab20(self):
		input = 8.87164
		input = input + self.synapse0x11ddae60()
		input = input + self.synapse0x11ddaea0()
		input = input + self.synapse0x11ddaee0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11ddaf20(self):
		input = -2.51561
		input = input + self.synapse0x11ddb140()
		input = input + self.synapse0x11ddb180()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x11d90e20(self):
		return (self.neuron0x11dc85d0()*-0.108109)
	def synapse0x11daf370(self):
		return (self.neuron0x11dc8910()*-0.210235)
	def synapse0x11dd9ee0(self):
		return (self.neuron0x11dd98e0()*0.00137662)
	def synapse0x11dda260(self):
		return (self.neuron0x11dc85d0()*0.255684)
	def synapse0x11dda2a0(self):
		return (self.neuron0x11dc8910()*0.72954)
	def synapse0x11dda2e0(self):
		return (self.neuron0x11dd98e0()*-2.24323)
	def synapse0x11dda660(self):
		return (self.neuron0x11dc85d0()*-1.67782)
	def synapse0x11dda6a0(self):
		return (self.neuron0x11dc8910()*3.60838)
	def synapse0x11dda6e0(self):
		return (self.neuron0x11dd98e0()*-0.289525)
	def synapse0x11ddaa60(self):
		return (self.neuron0x11dd9c30()*-15.5859)
	def synapse0x11ddaaa0(self):
		return (self.neuron0x11dd9f20()*-7.16614)
	def synapse0x11ddaae0(self):
		return (self.neuron0x11dda320()*-5.22764)
	def synapse0x11ddae60(self):
		return (self.neuron0x11dd9c30()*-11.8756)
	def synapse0x11ddaea0(self):
		return (self.neuron0x11dd9f20()*7.96331)
	def synapse0x11ddaee0(self):
		return (self.neuron0x11dda320()*-6.47921)
	def synapse0x11ddb140(self):
		return (self.neuron0x11dda720()*20.2899)
	def synapse0x11ddb180(self):
		return (self.neuron0x11ddab20()*-15.3469)
