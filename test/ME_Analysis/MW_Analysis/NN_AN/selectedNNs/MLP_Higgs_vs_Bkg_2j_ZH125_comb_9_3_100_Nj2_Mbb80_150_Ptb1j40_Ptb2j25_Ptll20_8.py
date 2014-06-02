from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_8:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.500017)/0.25242
		self.input1 = (in1 - 0.592179)/0.338539
		self.input2 = (in2 - 0.679468)/0.281065
		if index==0: return self.neuron0x18c5f7b0();
		return 0.
	def neuron0x18c5b780(self):
		return self.input0
	def neuron0x18c5bac0(self):
		return self.input1
	def neuron0x18c5be00(self):
		return self.input2
	def neuron0x18c5c270(self):
		input = 1.83652
		input = input + self.synapse0x18c00920()
		input = input + self.synapse0x18c5c520()
		input = input + self.synapse0x18c5c560()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5c5a0(self):
		input = -0.065199
		input = input + self.synapse0x18c5c8e0()
		input = input + self.synapse0x18c5c920()
		input = input + self.synapse0x18c5c960()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5c9a0(self):
		input = -0.15171
		input = input + self.synapse0x18c5cce0()
		input = input + self.synapse0x18c5cd20()
		input = input + self.synapse0x18c5cd60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5cda0(self):
		input = -0.583318
		input = input + self.synapse0x18c5d0e0()
		input = input + self.synapse0x18c5d120()
		input = input + self.synapse0x18c5d160()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5d1a0(self):
		input = 2.5169
		input = input + self.synapse0x18c5d4e0()
		input = input + self.synapse0x18c5d520()
		input = input + self.synapse0x18c5d560()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5d5a0(self):
		input = 1.34963
		input = input + self.synapse0x18c5d8e0()
		input = input + self.synapse0x18c5d920()
		input = input + self.synapse0x18c00960()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5da70(self):
		input = 0.847552
		input = input + self.synapse0x18c5dd20()
		input = input + self.synapse0x18c5dd60()
		input = input + self.synapse0x18c5dda0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5dde0(self):
		input = 0.308146
		input = input + self.synapse0x18c5e120()
		input = input + self.synapse0x18c5e160()
		input = input + self.synapse0x18c5e1a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5e1e0(self):
		input = 0.543133
		input = input + self.synapse0x18c5e520()
		input = input + self.synapse0x18c5e560()
		input = input + self.synapse0x18c5e5a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5e5e0(self):
		input = -0.243548
		input = input + self.synapse0x18c5e920()
		input = input + self.synapse0x18c5e960()
		input = input + self.synapse0x18c5e9a0()
		input = input + self.synapse0x18c5e9e0()
		input = input + self.synapse0x18c5ea20()
		input = input + self.synapse0x18c5ea60()
		input = input + self.synapse0x18bf0f60()
		input = input + self.synapse0x18bf1040()
		input = input + self.synapse0x18bf1080()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5ecb0(self):
		input = 1.5258
		input = input + self.synapse0x18c5eff0()
		input = input + self.synapse0x18c5f030()
		input = input + self.synapse0x18c5f070()
		input = input + self.synapse0x18c5f0b0()
		input = input + self.synapse0x18c5f0f0()
		input = input + self.synapse0x18c5f130()
		input = input + self.synapse0x18c5f170()
		input = input + self.synapse0x18c5f1b0()
		input = input + self.synapse0x18c5f1f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5f230(self):
		input = 0.148596
		input = input + self.synapse0x18c5f570()
		input = input + self.synapse0x18c5f5b0()
		input = input + self.synapse0x18c5f5f0()
		input = input + self.synapse0x18c5f630()
		input = input + self.synapse0x18c5f670()
		input = input + self.synapse0x18c5f6b0()
		input = input + self.synapse0x18c5f6f0()
		input = input + self.synapse0x18c5f730()
		input = input + self.synapse0x18c5f770()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x18c5f7b0(self):
		input = 4.76233
		input = input + self.synapse0x18c009e0()
		input = input + self.synapse0x18c5faf0()
		input = input + self.synapse0x18c5fb30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x18c00920(self):
		return (self.neuron0x18c5b780()*-2.48711)
	def synapse0x18c5c520(self):
		return (self.neuron0x18c5bac0()*0.752282)
	def synapse0x18c5c560(self):
		return (self.neuron0x18c5be00()*-0.200274)
	def synapse0x18c5c8e0(self):
		return (self.neuron0x18c5b780()*1.80406)
	def synapse0x18c5c920(self):
		return (self.neuron0x18c5bac0()*0.953523)
	def synapse0x18c5c960(self):
		return (self.neuron0x18c5be00()*-0.0458923)
	def synapse0x18c5cce0(self):
		return (self.neuron0x18c5b780()*-1.88959)
	def synapse0x18c5cd20(self):
		return (self.neuron0x18c5bac0()*-0.0341409)
	def synapse0x18c5cd60(self):
		return (self.neuron0x18c5be00()*-0.600231)
	def synapse0x18c5d0e0(self):
		return (self.neuron0x18c5b780()*-0.918071)
	def synapse0x18c5d120(self):
		return (self.neuron0x18c5bac0()*-0.316664)
	def synapse0x18c5d160(self):
		return (self.neuron0x18c5be00()*0.455631)
	def synapse0x18c5d4e0(self):
		return (self.neuron0x18c5b780()*0.636445)
	def synapse0x18c5d520(self):
		return (self.neuron0x18c5bac0()*0.674723)
	def synapse0x18c5d560(self):
		return (self.neuron0x18c5be00()*-0.493185)
	def synapse0x18c5d8e0(self):
		return (self.neuron0x18c5b780()*2.08925)
	def synapse0x18c5d920(self):
		return (self.neuron0x18c5bac0()*-1.45334)
	def synapse0x18c00960(self):
		return (self.neuron0x18c5be00()*0.912624)
	def synapse0x18c5dd20(self):
		return (self.neuron0x18c5b780()*-1.48984)
	def synapse0x18c5dd60(self):
		return (self.neuron0x18c5bac0()*-3.44398)
	def synapse0x18c5dda0(self):
		return (self.neuron0x18c5be00()*-0.174005)
	def synapse0x18c5e120(self):
		return (self.neuron0x18c5b780()*1.1768)
	def synapse0x18c5e160(self):
		return (self.neuron0x18c5bac0()*0.362673)
	def synapse0x18c5e1a0(self):
		return (self.neuron0x18c5be00()*0.929067)
	def synapse0x18c5e520(self):
		return (self.neuron0x18c5b780()*0.283246)
	def synapse0x18c5e560(self):
		return (self.neuron0x18c5bac0()*-0.571649)
	def synapse0x18c5e5a0(self):
		return (self.neuron0x18c5be00()*-0.924393)
	def synapse0x18c5e920(self):
		return (self.neuron0x18c5c270()*1.42685)
	def synapse0x18c5e960(self):
		return (self.neuron0x18c5c5a0()*-1.81641)
	def synapse0x18c5e9a0(self):
		return (self.neuron0x18c5c9a0()*1.39762)
	def synapse0x18c5e9e0(self):
		return (self.neuron0x18c5cda0()*2.48768)
	def synapse0x18c5ea20(self):
		return (self.neuron0x18c5d1a0()*-3.21294)
	def synapse0x18c5ea60(self):
		return (self.neuron0x18c5d5a0()*-1.94541)
	def synapse0x18bf0f60(self):
		return (self.neuron0x18c5da70()*-1.83081)
	def synapse0x18bf1040(self):
		return (self.neuron0x18c5dde0()*0.282928)
	def synapse0x18bf1080(self):
		return (self.neuron0x18c5e1e0()*-0.0947616)
	def synapse0x18c5eff0(self):
		return (self.neuron0x18c5c270()*4.81593)
	def synapse0x18c5f030(self):
		return (self.neuron0x18c5c5a0()*-2.54011)
	def synapse0x18c5f070(self):
		return (self.neuron0x18c5c9a0()*2.78227)
	def synapse0x18c5f0b0(self):
		return (self.neuron0x18c5cda0()*3.99593)
	def synapse0x18c5f0f0(self):
		return (self.neuron0x18c5d1a0()*-0.745601)
	def synapse0x18c5f130(self):
		return (self.neuron0x18c5d5a0()*-0.0656231)
	def synapse0x18c5f170(self):
		return (self.neuron0x18c5da70()*0.00927977)
	def synapse0x18c5f1b0(self):
		return (self.neuron0x18c5dde0()*0.692425)
	def synapse0x18c5f1f0(self):
		return (self.neuron0x18c5e1e0()*1.47633)
	def synapse0x18c5f570(self):
		return (self.neuron0x18c5c270()*-0.383763)
	def synapse0x18c5f5b0(self):
		return (self.neuron0x18c5c5a0()*0.536909)
	def synapse0x18c5f5f0(self):
		return (self.neuron0x18c5c9a0()*-0.504128)
	def synapse0x18c5f630(self):
		return (self.neuron0x18c5cda0()*0.482966)
	def synapse0x18c5f670(self):
		return (self.neuron0x18c5d1a0()*0.976153)
	def synapse0x18c5f6b0(self):
		return (self.neuron0x18c5d5a0()*-0.34625)
	def synapse0x18c5f6f0(self):
		return (self.neuron0x18c5da70()*0.467057)
	def synapse0x18c5f730(self):
		return (self.neuron0x18c5dde0()*0.831468)
	def synapse0x18c5f770(self):
		return (self.neuron0x18c5e1e0()*-0.932493)
	def synapse0x18c009e0(self):
		return (self.neuron0x18c5e5e0()*-4.86466)
	def synapse0x18c5faf0(self):
		return (self.neuron0x18c5ecb0()*-6.47404)
	def synapse0x18c5fb30(self):
		return (self.neuron0x18c5f230()*2.96932)
