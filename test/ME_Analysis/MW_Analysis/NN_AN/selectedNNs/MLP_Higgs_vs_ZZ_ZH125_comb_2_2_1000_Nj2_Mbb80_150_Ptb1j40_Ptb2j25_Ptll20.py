from math import exp

from math import tanh

class FinalV7/MLP_Higgs_vs_ZZ_ZH125_comb_2_2_1000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 21.0522)/1.27673
		self.input1 = (in1 - 10.8558)/1.04163
		self.input2 = (in2 - 24.4862)/1.13705
		self.input3 = (in3 - 12.7271)/0.888688
		if index==0: return self.neuron0x19c9b9e0();
		return 0.
	def neuron0x19c99c80(self):
		return self.input0
	def neuron0x19c99fc0(self):
		return self.input1
	def neuron0x19c9a300(self):
		return self.input2
	def neuron0x19c9a640(self):
		return self.input3
	def neuron0x19c9aab0(self):
		input = -0.660511
		input = input + self.synapse0x19ca2950()
		input = input + self.synapse0x19c9ad60()
		input = input + self.synapse0x19c9ada0()
		input = input + self.synapse0x19c9ade0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x19c9ae20(self):
		input = 4.71466
		input = input + self.synapse0x19c9b160()
		input = input + self.synapse0x19c9b1a0()
		input = input + self.synapse0x19c9b1e0()
		input = input + self.synapse0x19c9b220()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x19c9b260(self):
		input = -0.402894
		input = input + self.synapse0x19c9b5a0()
		input = input + self.synapse0x19c9b5e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x19c9b620(self):
		input = 7.88185
		input = input + self.synapse0x19c9b960()
		input = input + self.synapse0x19c9b9a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x19c9b9e0(self):
		input = 2.27311
		input = input + self.synapse0x19c9bd20()
		input = input + self.synapse0x19c9bd60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x19ca2950(self):
		return (self.neuron0x19c99c80()*0.461181)
	def synapse0x19c9ad60(self):
		return (self.neuron0x19c99fc0()*-0.0647124)
	def synapse0x19c9ada0(self):
		return (self.neuron0x19c9a300()*-0.0595913)
	def synapse0x19c9ade0(self):
		return (self.neuron0x19c9a640()*-0.301952)
	def synapse0x19c9b160(self):
		return (self.neuron0x19c99c80()*-1.55528)
	def synapse0x19c9b1a0(self):
		return (self.neuron0x19c99fc0()*5.17936)
	def synapse0x19c9b1e0(self):
		return (self.neuron0x19c9a300()*-2.33392)
	def synapse0x19c9b220(self):
		return (self.neuron0x19c9a640()*-0.922679)
	def synapse0x19c9b5a0(self):
		return (self.neuron0x19c9aab0()*3.98986)
	def synapse0x19c9b5e0(self):
		return (self.neuron0x19c9ae20()*1.41217)
	def synapse0x19c9b960(self):
		return (self.neuron0x19c9aab0()*-9.4781)
	def synapse0x19c9b9a0(self):
		return (self.neuron0x19c9ae20()*-2.06902)
	def synapse0x19c9bd20(self):
		return (self.neuron0x19c9b260()*9.75169)
	def synapse0x19c9bd60(self):
		return (self.neuron0x19c9b620()*-11.3571)
