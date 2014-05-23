from math import exp

from math import tanh

class FinalV8/MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_2_500_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.492195)/0.255462
		self.input1 = (in1 - 0.567862)/0.324105
		self.input2 = (in2 - 0.596078)/0.304322
		if index==0: return self.neuron0x3a6db5a0();
		return 0.
	def neuron0x3a6d9270(self):
		return self.input0
	def neuron0x3a6d95b0(self):
		return self.input1
	def neuron0x3a6d98f0(self):
		return self.input2
	def neuron0x3a6d9d60(self):
		input = 1.55242
		input = input + self.synapse0x3a6e1f70()
		input = input + self.synapse0x3a6da010()
		input = input + self.synapse0x3a6da050()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a6da090(self):
		input = 6.38049
		input = input + self.synapse0x3a6da3d0()
		input = input + self.synapse0x3a6da410()
		input = input + self.synapse0x3a6da450()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a6da490(self):
		input = 1.71672
		input = input + self.synapse0x3a6da7d0()
		input = input + self.synapse0x3a6da810()
		input = input + self.synapse0x3a6da850()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a6da890(self):
		input = 3.61959
		input = input + self.synapse0x3a6dabd0()
		input = input + self.synapse0x3a6dac10()
		input = input + self.synapse0x3a6dac50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a6dac90(self):
		input = 3.38776
		input = input + self.synapse0x3a6dafd0()
		input = input + self.synapse0x3a6db010()
		input = input + self.synapse0x3a6db050()
		input = input + self.synapse0x3a6db090()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a6db0d0(self):
		input = -2.56364
		input = input + self.synapse0x3a6db410()
		input = input + self.synapse0x3a66ddd0()
		input = input + self.synapse0x3a66de10()
		input = input + self.synapse0x3a6db560()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a6db5a0(self):
		input = -0.20283
		input = input + self.synapse0x3a6d9c30()
		input = input + self.synapse0x3a6db8e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x3a6e1f70(self):
		return (self.neuron0x3a6d9270()*0.767233)
	def synapse0x3a6da010(self):
		return (self.neuron0x3a6d95b0()*0.0149494)
	def synapse0x3a6da050(self):
		return (self.neuron0x3a6d98f0()*1.5602)
	def synapse0x3a6da3d0(self):
		return (self.neuron0x3a6d9270()*2.22895)
	def synapse0x3a6da410(self):
		return (self.neuron0x3a6d95b0()*1.31885)
	def synapse0x3a6da450(self):
		return (self.neuron0x3a6d98f0()*0.0337837)
	def synapse0x3a6da7d0(self):
		return (self.neuron0x3a6d9270()*1.32181)
	def synapse0x3a6da810(self):
		return (self.neuron0x3a6d95b0()*-0.315246)
	def synapse0x3a6da850(self):
		return (self.neuron0x3a6d98f0()*-0.716874)
	def synapse0x3a6dabd0(self):
		return (self.neuron0x3a6d9270()*-1.13616)
	def synapse0x3a6dac10(self):
		return (self.neuron0x3a6d95b0()*-0.134219)
	def synapse0x3a6dac50(self):
		return (self.neuron0x3a6d98f0()*-0.276811)
	def synapse0x3a6dafd0(self):
		return (self.neuron0x3a6d9d60()*-2.07323)
	def synapse0x3a6db010(self):
		return (self.neuron0x3a6da090()*-4.14259)
	def synapse0x3a6db050(self):
		return (self.neuron0x3a6da490()*-4.93308)
	def synapse0x3a6db090(self):
		return (self.neuron0x3a6da890()*2.66719)
	def synapse0x3a6db410(self):
		return (self.neuron0x3a6d9d60()*3.25251)
	def synapse0x3a66ddd0(self):
		return (self.neuron0x3a6da090()*-0.855535)
	def synapse0x3a66de10(self):
		return (self.neuron0x3a6da490()*3.50037)
	def synapse0x3a6db560(self):
		return (self.neuron0x3a6da890()*-4.83074)
	def synapse0x3a6d9c30(self):
		return (self.neuron0x3a6dac90()*-8.57098)
	def synapse0x3a6db8e0(self):
		return (self.neuron0x3a6db0d0()*8.2086)
