from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_3j_ZH125_comb_4_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20_5:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.467176)/0.243159
		self.input1 = (in1 - 0.52708)/0.296356
		self.input2 = (in2 - 0.534793)/0.314261
		if index==0: return self.neuron0x1af461f0();
		return 0.
	def neuron0x1af447d0(self):
		return self.input0
	def neuron0x1af44b10(self):
		return self.input1
	def neuron0x1af44e50(self):
		return self.input2
	def neuron0x1af452c0(self):
		input = 1.83721
		input = input + self.synapse0x1aee98b0()
		input = input + self.synapse0x1af45570()
		input = input + self.synapse0x1af455b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1af455f0(self):
		input = -6.69762
		input = input + self.synapse0x1af45930()
		input = input + self.synapse0x1af45970()
		input = input + self.synapse0x1af459b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1af459f0(self):
		input = 3.02561
		input = input + self.synapse0x1af45d30()
		input = input + self.synapse0x1af45d70()
		input = input + self.synapse0x1af45db0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1af45df0(self):
		input = 5.51948
		input = input + self.synapse0x1af46130()
		input = input + self.synapse0x1af46170()
		input = input + self.synapse0x1af461b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x1af461f0(self):
		input = -5.15244
		input = input + self.synapse0x1af46530()
		input = input + self.synapse0x1af46570()
		input = input + self.synapse0x1af465b0()
		input = input + self.synapse0x1af465f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1aee98b0(self):
		return (self.neuron0x1af447d0()*1.43032)
	def synapse0x1af45570(self):
		return (self.neuron0x1af44b10()*-0.667705)
	def synapse0x1af455b0(self):
		return (self.neuron0x1af44e50()*0.503382)
	def synapse0x1af45930(self):
		return (self.neuron0x1af447d0()*1.17169)
	def synapse0x1af45970(self):
		return (self.neuron0x1af44b10()*2.05728)
	def synapse0x1af459b0(self):
		return (self.neuron0x1af44e50()*0.23943)
	def synapse0x1af45d30(self):
		return (self.neuron0x1af447d0()*-1.56588)
	def synapse0x1af45d70(self):
		return (self.neuron0x1af44b10()*0.414075)
	def synapse0x1af45db0(self):
		return (self.neuron0x1af44e50()*-0.522695)
	def synapse0x1af46130(self):
		return (self.neuron0x1af447d0()*1.44453)
	def synapse0x1af46170(self):
		return (self.neuron0x1af44b10()*1.96007)
	def synapse0x1af461b0(self):
		return (self.neuron0x1af44e50()*-0.584645)
	def synapse0x1af46530(self):
		return (self.neuron0x1af452c0()*2.96846)
	def synapse0x1af46570(self):
		return (self.neuron0x1af455f0()*5.70525)
	def synapse0x1af465b0(self):
		return (self.neuron0x1af459f0()*-2.50075)
	def synapse0x1af465f0(self):
		return (self.neuron0x1af45df0()*5.10093)
