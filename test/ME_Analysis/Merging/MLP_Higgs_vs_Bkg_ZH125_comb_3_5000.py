from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_3_5000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x154a9c90();
		return 0.
	def neuron0x15497b00(self):
		return self.input0
	def neuron0x15497e40(self):
		return self.input1
	def neuron0x154a8e10(self):
		return self.input2
	def neuron0x154a9160(self):
		input = 2.7711
		input = input + self.synapse0x1545ff10()
		input = input + self.synapse0x154a9410()
		input = input + self.synapse0x154a9450()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x154a9490(self):
		input = -2.45782
		input = input + self.synapse0x154a97d0()
		input = input + self.synapse0x154a9810()
		input = input + self.synapse0x154a9850()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x154a9890(self):
		input = 7.00581
		input = input + self.synapse0x154a9bd0()
		input = input + self.synapse0x154a9c10()
		input = input + self.synapse0x154a9c50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x154a9c90(self):
		input = -1.10986
		input = input + self.synapse0x154a9eb0()
		input = input + self.synapse0x154a9ef0()
		input = input + self.synapse0x154a9f30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1545ff10(self):
		return (self.neuron0x15497b00()*0.364174)
	def synapse0x154a9410(self):
		return (self.neuron0x15497e40()*0.597486)
	def synapse0x154a9450(self):
		return (self.neuron0x154a8e10()*-0.107634)
	def synapse0x154a97d0(self):
		return (self.neuron0x15497b00()*-0.67245)
	def synapse0x154a9810(self):
		return (self.neuron0x15497e40()*1.14845)
	def synapse0x154a9850(self):
		return (self.neuron0x154a8e10()*-1.47236)
	def synapse0x154a9bd0(self):
		return (self.neuron0x15497b00()*-1.46949)
	def synapse0x154a9c10(self):
		return (self.neuron0x15497e40()*-0.512995)
	def synapse0x154a9c50(self):
		return (self.neuron0x154a8e10()*-1.4266)
	def synapse0x154a9eb0(self):
		return (self.neuron0x154a9160()*18.8978)
	def synapse0x154a9ef0(self):
		return (self.neuron0x154a9490()*-5.10573)
	def synapse0x154a9f30(self):
		return (self.neuron0x154a9890()*-16.2122)
