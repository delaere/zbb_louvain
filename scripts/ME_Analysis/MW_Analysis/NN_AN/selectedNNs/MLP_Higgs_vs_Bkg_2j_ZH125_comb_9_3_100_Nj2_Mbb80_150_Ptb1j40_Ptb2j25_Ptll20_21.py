from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_2j_ZH125_comb_9_3_100_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_21:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.500017)/0.25242
		self.input1 = (in1 - 0.592179)/0.338539
		self.input2 = (in2 - 0.679468)/0.281065
		if index==0: return self.neuron0x136ce990();
		return 0.
	def neuron0x136caa00(self):
		return self.input0
	def neuron0x136cad40(self):
		return self.input1
	def neuron0x136cb080(self):
		return self.input2
	def neuron0x136cb3c0(self):
		input = -1.45806
		input = input + self.synapse0x1366fb80()
		input = input + self.synapse0x136cb670()
		input = input + self.synapse0x136cb6b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cb6f0(self):
		input = -0.768892
		input = input + self.synapse0x136cba30()
		input = input + self.synapse0x136cba70()
		input = input + self.synapse0x136cbab0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cbaf0(self):
		input = -1.0523
		input = input + self.synapse0x136cbe30()
		input = input + self.synapse0x136cbe70()
		input = input + self.synapse0x136cbeb0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cbef0(self):
		input = 0.741483
		input = input + self.synapse0x136cc230()
		input = input + self.synapse0x136cc270()
		input = input + self.synapse0x136cc2b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cc2f0(self):
		input = -0.466653
		input = input + self.synapse0x136cc630()
		input = input + self.synapse0x136cc670()
		input = input + self.synapse0x136cc6b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cc6f0(self):
		input = -0.651768
		input = input + self.synapse0x136cca30()
		input = input + self.synapse0x136cca70()
		input = input + self.synapse0x1365fdc0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136ccbc0(self):
		input = -1.10573
		input = input + self.synapse0x136ccf00()
		input = input + self.synapse0x136ccf40()
		input = input + self.synapse0x136ccf80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136ccfc0(self):
		input = 0.918854
		input = input + self.synapse0x136cd300()
		input = input + self.synapse0x136cd340()
		input = input + self.synapse0x136cd380()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cd3c0(self):
		input = -0.0641341
		input = input + self.synapse0x136cd700()
		input = input + self.synapse0x136cd740()
		input = input + self.synapse0x136cd780()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cd7c0(self):
		input = 0.77846
		input = input + self.synapse0x136cdb00()
		input = input + self.synapse0x136cdb40()
		input = input + self.synapse0x136cdb80()
		input = input + self.synapse0x136cdbc0()
		input = input + self.synapse0x136cdc00()
		input = input + self.synapse0x136cdc40()
		input = input + self.synapse0x1365fe00()
		input = input + self.synapse0x13660200()
		input = input + self.synapse0x136602e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136cde90(self):
		input = -1.38461
		input = input + self.synapse0x136ce1d0()
		input = input + self.synapse0x136ce210()
		input = input + self.synapse0x136ce250()
		input = input + self.synapse0x136ce290()
		input = input + self.synapse0x136ce2d0()
		input = input + self.synapse0x136ce310()
		input = input + self.synapse0x136ce350()
		input = input + self.synapse0x136ce390()
		input = input + self.synapse0x136ce3d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136ce410(self):
		input = -0.287511
		input = input + self.synapse0x136ce750()
		input = input + self.synapse0x136ce790()
		input = input + self.synapse0x136ce7d0()
		input = input + self.synapse0x136ce810()
		input = input + self.synapse0x136ce850()
		input = input + self.synapse0x136ce890()
		input = input + self.synapse0x136ce8d0()
		input = input + self.synapse0x136ce910()
		input = input + self.synapse0x136ce950()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x136ce990(self):
		input = 1.34852
		input = input + self.synapse0x136cecd0()
		input = input + self.synapse0x136ced10()
		input = input + self.synapse0x136ced50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x1366fb80(self):
		return (self.neuron0x136caa00()*-0.20565)
	def synapse0x136cb670(self):
		return (self.neuron0x136cad40()*0.0777419)
	def synapse0x136cb6b0(self):
		return (self.neuron0x136cb080()*1.03242)
	def synapse0x136cba30(self):
		return (self.neuron0x136caa00()*-0.281481)
	def synapse0x136cba70(self):
		return (self.neuron0x136cad40()*-0.531079)
	def synapse0x136cbab0(self):
		return (self.neuron0x136cb080()*0.798855)
	def synapse0x136cbe30(self):
		return (self.neuron0x136caa00()*-0.571457)
	def synapse0x136cbe70(self):
		return (self.neuron0x136cad40()*-0.304806)
	def synapse0x136cbeb0(self):
		return (self.neuron0x136cb080()*1.2937)
	def synapse0x136cc230(self):
		return (self.neuron0x136caa00()*0.011078)
	def synapse0x136cc270(self):
		return (self.neuron0x136cad40()*0.289356)
	def synapse0x136cc2b0(self):
		return (self.neuron0x136cb080()*-0.724542)
	def synapse0x136cc630(self):
		return (self.neuron0x136caa00()*-0.553766)
	def synapse0x136cc670(self):
		return (self.neuron0x136cad40()*0.467186)
	def synapse0x136cc6b0(self):
		return (self.neuron0x136cb080()*-0.186003)
	def synapse0x136cca30(self):
		return (self.neuron0x136caa00()*-0.288457)
	def synapse0x136cca70(self):
		return (self.neuron0x136cad40()*-0.430509)
	def synapse0x1365fdc0(self):
		return (self.neuron0x136cb080()*-0.212088)
	def synapse0x136ccf00(self):
		return (self.neuron0x136caa00()*0.467024)
	def synapse0x136ccf40(self):
		return (self.neuron0x136cad40()*-0.9291)
	def synapse0x136ccf80(self):
		return (self.neuron0x136cb080()*-0.212492)
	def synapse0x136cd300(self):
		return (self.neuron0x136caa00()*0.543042)
	def synapse0x136cd340(self):
		return (self.neuron0x136cad40()*-0.917385)
	def synapse0x136cd380(self):
		return (self.neuron0x136cb080()*-0.376285)
	def synapse0x136cd700(self):
		return (self.neuron0x136caa00()*-0.0333071)
	def synapse0x136cd740(self):
		return (self.neuron0x136cad40()*0.213805)
	def synapse0x136cd780(self):
		return (self.neuron0x136cb080()*-0.192208)
	def synapse0x136cdb00(self):
		return (self.neuron0x136cb3c0()*1.60743)
	def synapse0x136cdb40(self):
		return (self.neuron0x136cb6f0()*-1.04442)
	def synapse0x136cdb80(self):
		return (self.neuron0x136cbaf0()*-1.39612)
	def synapse0x136cdbc0(self):
		return (self.neuron0x136cbef0()*-1.40995)
	def synapse0x136cdc00(self):
		return (self.neuron0x136cc2f0()*-0.560093)
	def synapse0x136cdc40(self):
		return (self.neuron0x136cc6f0()*-0.668486)
	def synapse0x1365fe00(self):
		return (self.neuron0x136ccbc0()*-1.01784)
	def synapse0x13660200(self):
		return (self.neuron0x136ccfc0()*1.35918)
	def synapse0x136602e0(self):
		return (self.neuron0x136cd3c0()*-1.17116)
	def synapse0x136ce1d0(self):
		return (self.neuron0x136cb3c0()*-1.63514)
	def synapse0x136ce210(self):
		return (self.neuron0x136cb6f0()*1.13727)
	def synapse0x136ce250(self):
		return (self.neuron0x136cbaf0()*1.00397)
	def synapse0x136ce290(self):
		return (self.neuron0x136cbef0()*1.59581)
	def synapse0x136ce2d0(self):
		return (self.neuron0x136cc2f0()*-0.0460608)
	def synapse0x136ce310(self):
		return (self.neuron0x136cc6f0()*0.843075)
	def synapse0x136ce350(self):
		return (self.neuron0x136ccbc0()*1.41318)
	def synapse0x136ce390(self):
		return (self.neuron0x136ccfc0()*-2.15426)
	def synapse0x136ce3d0(self):
		return (self.neuron0x136cd3c0()*1.5814)
	def synapse0x136ce750(self):
		return (self.neuron0x136cb3c0()*-1.23811)
	def synapse0x136ce790(self):
		return (self.neuron0x136cb6f0()*0.702581)
	def synapse0x136ce7d0(self):
		return (self.neuron0x136cbaf0()*0.401896)
	def synapse0x136ce810(self):
		return (self.neuron0x136cbef0()*0.441683)
	def synapse0x136ce850(self):
		return (self.neuron0x136cc2f0()*0.334033)
	def synapse0x136ce890(self):
		return (self.neuron0x136cc6f0()*0.509851)
	def synapse0x136ce8d0(self):
		return (self.neuron0x136ccbc0()*0.795843)
	def synapse0x136ce910(self):
		return (self.neuron0x136ccfc0()*-0.734003)
	def synapse0x136ce950(self):
		return (self.neuron0x136cd3c0()*0.921218)
	def synapse0x136cecd0(self):
		return (self.neuron0x136cd7c0()*9.03548)
	def synapse0x136ced10(self):
		return (self.neuron0x136cde90()*-5.72764)
	def synapse0x136ced50(self):
		return (self.neuron0x136ce410()*-1.5543)
