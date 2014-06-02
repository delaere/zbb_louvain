from math import exp

from math import tanh

class Final12/MLP_ZZ_vs_DY_ZH125_comb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 19.2663)/0.885575
		self.input1 = (in1 - 19.8397)/0.749967
		self.input2 = (in2 - 20.7205)/1.37919
		self.input3 = (in3 - 10.4438)/0.936439
		if index==0: return self.neuron0x3a9f04a0();
		return 0.
	def neuron0x3a9ec2a0(self):
		return self.input0
	def neuron0x3a9ec5e0(self):
		return self.input1
	def neuron0x3a9ec920(self):
		return self.input2
	def neuron0x3a9ecc60(self):
		return self.input3
	def neuron0x3a9ed0d0(self):
		input = -1.22419
		input = input + self.synapse0x3a969920()
		input = input + self.synapse0x3a9ed380()
		input = input + self.synapse0x3a9ed3c0()
		input = input + self.synapse0x3a9ed400()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ed440(self):
		input = -1.0744
		input = input + self.synapse0x3a9ed780()
		input = input + self.synapse0x3a9ed7c0()
		input = input + self.synapse0x3a9ed800()
		input = input + self.synapse0x3a9ed840()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ed880(self):
		input = -0.0676176
		input = input + self.synapse0x3a9edbc0()
		input = input + self.synapse0x3a9edc00()
		input = input + self.synapse0x3a9edc40()
		input = input + self.synapse0x3a9edc80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9edcc0(self):
		input = 0.474989
		input = input + self.synapse0x3a9ee000()
		input = input + self.synapse0x3a9ee040()
		input = input + self.synapse0x3a9ee080()
		input = input + self.synapse0x3a9ee0c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ee100(self):
		input = 0.779235
		input = input + self.synapse0x3a9ee440()
		input = input + self.synapse0x3a969960()
		input = input + self.synapse0x3a9f4f10()
		input = input + self.synapse0x3a969520()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ee590(self):
		input = 0.696128
		input = input + self.synapse0x3a9ee8d0()
		input = input + self.synapse0x3a9ee910()
		input = input + self.synapse0x3a9ee950()
		input = input + self.synapse0x3a9ee990()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ee9d0(self):
		input = -0.216513
		input = input + self.synapse0x3a9eed10()
		input = input + self.synapse0x3a9eed50()
		input = input + self.synapse0x3a9eed90()
		input = input + self.synapse0x3a9eedd0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9eee10(self):
		input = 0.521203
		input = input + self.synapse0x3a9ef150()
		input = input + self.synapse0x3a9ef190()
		input = input + self.synapse0x3a9ef1d0()
		input = input + self.synapse0x3a9ef210()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ef250(self):
		input = 0.168264
		input = input + self.synapse0x3a9ef590()
		input = input + self.synapse0x3a969560()
		input = input + self.synapse0x3a9698d0()
		input = input + self.synapse0x3a9699b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9ef7e0(self):
		input = 0.160099
		input = input + self.synapse0x3a9efb20()
		input = input + self.synapse0x3a9efb60()
		input = input + self.synapse0x3a9efba0()
		input = input + self.synapse0x3a9efbe0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9efc20(self):
		input = -0.212836
		input = input + self.synapse0x3a9eff60()
		input = input + self.synapse0x3a9effa0()
		input = input + self.synapse0x3a9effe0()
		input = input + self.synapse0x3a9f0020()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9f0060(self):
		input = 0.256782
		input = input + self.synapse0x3a9f03a0()
		input = input + self.synapse0x3a9f03e0()
		input = input + self.synapse0x3a9f0420()
		input = input + self.synapse0x3a9f0460()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x3a9f04a0(self):
		input = 0.814346
		input = input + self.synapse0x3a9f07e0()
		input = input + self.synapse0x3a9f0820()
		input = input + self.synapse0x3a9f0860()
		input = input + self.synapse0x3a9f08a0()
		input = input + self.synapse0x3a9f08e0()
		input = input + self.synapse0x3a9f0920()
		input = input + self.synapse0x3a9f0960()
		input = input + self.synapse0x3a9f09a0()
		input = input + self.synapse0x3a9f09e0()
		input = input + self.synapse0x3a9f0a20()
		input = input + self.synapse0x3a9f0a60()
		input = input + self.synapse0x3a9f0aa0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x3a969920(self):
		return (self.neuron0x3a9ec2a0()*-2.3358)
	def synapse0x3a9ed380(self):
		return (self.neuron0x3a9ec5e0()*1.78118)
	def synapse0x3a9ed3c0(self):
		return (self.neuron0x3a9ec920()*-2.15553)
	def synapse0x3a9ed400(self):
		return (self.neuron0x3a9ecc60()*1.62274)
	def synapse0x3a9ed780(self):
		return (self.neuron0x3a9ec2a0()*-1.70767)
	def synapse0x3a9ed7c0(self):
		return (self.neuron0x3a9ec5e0()*1.43062)
	def synapse0x3a9ed800(self):
		return (self.neuron0x3a9ec920()*-1.81733)
	def synapse0x3a9ed840(self):
		return (self.neuron0x3a9ecc60()*1.97876)
	def synapse0x3a9edbc0(self):
		return (self.neuron0x3a9ec2a0()*0.786361)
	def synapse0x3a9edc00(self):
		return (self.neuron0x3a9ec5e0()*0.187866)
	def synapse0x3a9edc40(self):
		return (self.neuron0x3a9ec920()*-0.101959)
	def synapse0x3a9edc80(self):
		return (self.neuron0x3a9ecc60()*-1.08329)
	def synapse0x3a9ee000(self):
		return (self.neuron0x3a9ec2a0()*0.264152)
	def synapse0x3a9ee040(self):
		return (self.neuron0x3a9ec5e0()*0.0377118)
	def synapse0x3a9ee080(self):
		return (self.neuron0x3a9ec920()*-0.656572)
	def synapse0x3a9ee0c0(self):
		return (self.neuron0x3a9ecc60()*-0.055897)
	def synapse0x3a9ee440(self):
		return (self.neuron0x3a9ec2a0()*-1.3883)
	def synapse0x3a969960(self):
		return (self.neuron0x3a9ec5e0()*0.471855)
	def synapse0x3a9f4f10(self):
		return (self.neuron0x3a9ec920()*0.574879)
	def synapse0x3a969520(self):
		return (self.neuron0x3a9ecc60()*1.80636)
	def synapse0x3a9ee8d0(self):
		return (self.neuron0x3a9ec2a0()*-0.527318)
	def synapse0x3a9ee910(self):
		return (self.neuron0x3a9ec5e0()*-0.270297)
	def synapse0x3a9ee950(self):
		return (self.neuron0x3a9ec920()*0.232225)
	def synapse0x3a9ee990(self):
		return (self.neuron0x3a9ecc60()*0.192438)
	def synapse0x3a9eed10(self):
		return (self.neuron0x3a9ec2a0()*-0.306298)
	def synapse0x3a9eed50(self):
		return (self.neuron0x3a9ec5e0()*0.122609)
	def synapse0x3a9eed90(self):
		return (self.neuron0x3a9ec920()*-0.028788)
	def synapse0x3a9eedd0(self):
		return (self.neuron0x3a9ecc60()*0.847179)
	def synapse0x3a9ef150(self):
		return (self.neuron0x3a9ec2a0()*1.02101)
	def synapse0x3a9ef190(self):
		return (self.neuron0x3a9ec5e0()*-0.418922)
	def synapse0x3a9ef1d0(self):
		return (self.neuron0x3a9ec920()*0.0328314)
	def synapse0x3a9ef210(self):
		return (self.neuron0x3a9ecc60()*-0.781338)
	def synapse0x3a9ef590(self):
		return (self.neuron0x3a9ec2a0()*-0.610183)
	def synapse0x3a969560(self):
		return (self.neuron0x3a9ec5e0()*-0.276835)
	def synapse0x3a9698d0(self):
		return (self.neuron0x3a9ec920()*0.146308)
	def synapse0x3a9699b0(self):
		return (self.neuron0x3a9ecc60()*0.50681)
	def synapse0x3a9efb20(self):
		return (self.neuron0x3a9ec2a0()*0.855684)
	def synapse0x3a9efb60(self):
		return (self.neuron0x3a9ec5e0()*0.133946)
	def synapse0x3a9efba0(self):
		return (self.neuron0x3a9ec920()*-0.858929)
	def synapse0x3a9efbe0(self):
		return (self.neuron0x3a9ecc60()*-0.705682)
	def synapse0x3a9eff60(self):
		return (self.neuron0x3a9ec2a0()*-0.826402)
	def synapse0x3a9effa0(self):
		return (self.neuron0x3a9ec5e0()*0.927211)
	def synapse0x3a9effe0(self):
		return (self.neuron0x3a9ec920()*-0.263607)
	def synapse0x3a9f0020(self):
		return (self.neuron0x3a9ecc60()*0.607531)
	def synapse0x3a9f03a0(self):
		return (self.neuron0x3a9ec2a0()*0.363037)
	def synapse0x3a9f03e0(self):
		return (self.neuron0x3a9ec5e0()*-0.152221)
	def synapse0x3a9f0420(self):
		return (self.neuron0x3a9ec920()*-0.450761)
	def synapse0x3a9f0460(self):
		return (self.neuron0x3a9ecc60()*-0.500271)
	def synapse0x3a9f07e0(self):
		return (self.neuron0x3a9ed0d0()*-1.16953)
	def synapse0x3a9f0820(self):
		return (self.neuron0x3a9ed440()*-1.73841)
	def synapse0x3a9f0860(self):
		return (self.neuron0x3a9ed880()*0.116625)
	def synapse0x3a9f08a0(self):
		return (self.neuron0x3a9edcc0()*0.614163)
	def synapse0x3a9f08e0(self):
		return (self.neuron0x3a9ee100()*-0.691127)
	def synapse0x3a9f0920(self):
		return (self.neuron0x3a9ee590()*-1.37224)
	def synapse0x3a9f0960(self):
		return (self.neuron0x3a9ee9d0()*-0.758421)
	def synapse0x3a9f09a0(self):
		return (self.neuron0x3a9eee10()*-0.347869)
	def synapse0x3a9f09e0(self):
		return (self.neuron0x3a9ef250()*-0.951586)
	def synapse0x3a9f0a20(self):
		return (self.neuron0x3a9ef7e0()*0.274388)
	def synapse0x3a9f0a60(self):
		return (self.neuron0x3a9efc20()*1.44305)
	def synapse0x3a9f0aa0(self):
		return (self.neuron0x3a9f0060()*2.05229)
