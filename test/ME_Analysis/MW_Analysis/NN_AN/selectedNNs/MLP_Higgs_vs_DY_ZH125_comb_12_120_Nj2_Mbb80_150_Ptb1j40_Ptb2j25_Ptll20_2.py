from math import exp

from math import tanh

class FinalV7/MLP_Higgs_vs_DY_ZH125_comb_12_120_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_2:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 19.5711)/0.977992
		self.input1 = (in1 - 20.2766)/0.818811
		self.input2 = (in2 - 24.2646)/1.23737
		self.input3 = (in3 - 12.5907)/0.782629
		if index==0: return self.neuron0x24a38250();
		return 0.
	def neuron0x24a34050(self):
		return self.input0
	def neuron0x24a34390(self):
		return self.input1
	def neuron0x24a346d0(self):
		return self.input2
	def neuron0x24a34a10(self):
		return self.input3
	def neuron0x24a34e80(self):
		input = 0.244718
		input = input + self.synapse0x24a3cd20()
		input = input + self.synapse0x24a35130()
		input = input + self.synapse0x24a35170()
		input = input + self.synapse0x24a351b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a351f0(self):
		input = 0.638656
		input = input + self.synapse0x24a35530()
		input = input + self.synapse0x24a35570()
		input = input + self.synapse0x24a355b0()
		input = input + self.synapse0x24a355f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a35630(self):
		input = 0.216967
		input = input + self.synapse0x24a35970()
		input = input + self.synapse0x24a359b0()
		input = input + self.synapse0x24a359f0()
		input = input + self.synapse0x24a35a30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a35a70(self):
		input = -0.633879
		input = input + self.synapse0x24a35db0()
		input = input + self.synapse0x24a35df0()
		input = input + self.synapse0x24a35e30()
		input = input + self.synapse0x24a35e70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a35eb0(self):
		input = 0.837594
		input = input + self.synapse0x24a361f0()
		input = input + self.synapse0x24a3cd60()
		input = input + self.synapse0x17e31ed0()
		input = input + self.synapse0x17e31f10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a36340(self):
		input = 1.16185
		input = input + self.synapse0x24a36680()
		input = input + self.synapse0x24a366c0()
		input = input + self.synapse0x24a36700()
		input = input + self.synapse0x24a36740()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a36780(self):
		input = -1.44389
		input = input + self.synapse0x24a36ac0()
		input = input + self.synapse0x24a36b00()
		input = input + self.synapse0x24a36b40()
		input = input + self.synapse0x24a36b80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a36bc0(self):
		input = 0.862406
		input = input + self.synapse0x24a36f00()
		input = input + self.synapse0x24a36f40()
		input = input + self.synapse0x24a36f80()
		input = input + self.synapse0x24a36fc0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a37000(self):
		input = 0.476175
		input = input + self.synapse0x24a37340()
		input = input + self.synapse0x17e322e0()
		input = input + self.synapse0x24a0ccd0()
		input = input + self.synapse0x24a0cd10()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a37590(self):
		input = 0.0225882
		input = input + self.synapse0x24a378d0()
		input = input + self.synapse0x24a37910()
		input = input + self.synapse0x24a37950()
		input = input + self.synapse0x24a37990()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a379d0(self):
		input = -0.31207
		input = input + self.synapse0x24a37d10()
		input = input + self.synapse0x24a37d50()
		input = input + self.synapse0x24a37d90()
		input = input + self.synapse0x24a37dd0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a37e10(self):
		input = 0.391683
		input = input + self.synapse0x24a38150()
		input = input + self.synapse0x24a38190()
		input = input + self.synapse0x24a381d0()
		input = input + self.synapse0x24a38210()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x24a38250(self):
		input = 0.653114
		input = input + self.synapse0x24a38590()
		input = input + self.synapse0x24a385d0()
		input = input + self.synapse0x24a38610()
		input = input + self.synapse0x24a38650()
		input = input + self.synapse0x24a38690()
		input = input + self.synapse0x24a386d0()
		input = input + self.synapse0x24a38710()
		input = input + self.synapse0x24a38750()
		input = input + self.synapse0x24a38790()
		input = input + self.synapse0x24a387d0()
		input = input + self.synapse0x24a38810()
		input = input + self.synapse0x24a38850()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x24a3cd20(self):
		return (self.neuron0x24a34050()*-0.313444)
	def synapse0x24a35130(self):
		return (self.neuron0x24a34390()*0.254269)
	def synapse0x24a35170(self):
		return (self.neuron0x24a346d0()*-0.140457)
	def synapse0x24a351b0(self):
		return (self.neuron0x24a34a10()*0.941615)
	def synapse0x24a35530(self):
		return (self.neuron0x24a34050()*0.183672)
	def synapse0x24a35570(self):
		return (self.neuron0x24a34390()*-1.31587)
	def synapse0x24a355b0(self):
		return (self.neuron0x24a346d0()*-0.360918)
	def synapse0x24a355f0(self):
		return (self.neuron0x24a34a10()*1.4911)
	def synapse0x24a35970(self):
		return (self.neuron0x24a34050()*0.222196)
	def synapse0x24a359b0(self):
		return (self.neuron0x24a34390()*-0.167023)
	def synapse0x24a359f0(self):
		return (self.neuron0x24a346d0()*0.585595)
	def synapse0x24a35a30(self):
		return (self.neuron0x24a34a10()*-0.217972)
	def synapse0x24a35db0(self):
		return (self.neuron0x24a34050()*0.454001)
	def synapse0x24a35df0(self):
		return (self.neuron0x24a34390()*-0.0637628)
	def synapse0x24a35e30(self):
		return (self.neuron0x24a346d0()*-0.149209)
	def synapse0x24a35e70(self):
		return (self.neuron0x24a34a10()*-1.92397)
	def synapse0x24a361f0(self):
		return (self.neuron0x24a34050()*0.562058)
	def synapse0x24a3cd60(self):
		return (self.neuron0x24a34390()*-0.018284)
	def synapse0x17e31ed0(self):
		return (self.neuron0x24a346d0()*-0.870783)
	def synapse0x17e31f10(self):
		return (self.neuron0x24a34a10()*-0.0362116)
	def synapse0x24a36680(self):
		return (self.neuron0x24a34050()*-0.197269)
	def synapse0x24a366c0(self):
		return (self.neuron0x24a34390()*-1.13907)
	def synapse0x24a36700(self):
		return (self.neuron0x24a346d0()*0.391518)
	def synapse0x24a36740(self):
		return (self.neuron0x24a34a10()*0.28271)
	def synapse0x24a36ac0(self):
		return (self.neuron0x24a34050()*-2.5024)
	def synapse0x24a36b00(self):
		return (self.neuron0x24a34390()*2.02869)
	def synapse0x24a36b40(self):
		return (self.neuron0x24a346d0()*0.660873)
	def synapse0x24a36b80(self):
		return (self.neuron0x24a34a10()*-0.720041)
	def synapse0x24a36f00(self):
		return (self.neuron0x24a34050()*0.476874)
	def synapse0x24a36f40(self):
		return (self.neuron0x24a34390()*0.295996)
	def synapse0x24a36f80(self):
		return (self.neuron0x24a346d0()*-0.357037)
	def synapse0x24a36fc0(self):
		return (self.neuron0x24a34a10()*-0.655346)
	def synapse0x24a37340(self):
		return (self.neuron0x24a34050()*0.586445)
	def synapse0x17e322e0(self):
		return (self.neuron0x24a34390()*0.103591)
	def synapse0x24a0ccd0(self):
		return (self.neuron0x24a346d0()*-0.364288)
	def synapse0x24a0cd10(self):
		return (self.neuron0x24a34a10()*-1.22428)
	def synapse0x24a378d0(self):
		return (self.neuron0x24a34050()*1.67802)
	def synapse0x24a37910(self):
		return (self.neuron0x24a34390()*0.136795)
	def synapse0x24a37950(self):
		return (self.neuron0x24a346d0()*-0.639887)
	def synapse0x24a37990(self):
		return (self.neuron0x24a34a10()*-1.42471)
	def synapse0x24a37d10(self):
		return (self.neuron0x24a34050()*-1.16364)
	def synapse0x24a37d50(self):
		return (self.neuron0x24a34390()*-1.17647)
	def synapse0x24a37d90(self):
		return (self.neuron0x24a346d0()*3.61525)
	def synapse0x24a37dd0(self):
		return (self.neuron0x24a34a10()*-0.0913012)
	def synapse0x24a38150(self):
		return (self.neuron0x24a34050()*-1.29886)
	def synapse0x24a38190(self):
		return (self.neuron0x24a34390()*-0.274124)
	def synapse0x24a381d0(self):
		return (self.neuron0x24a346d0()*1.1995)
	def synapse0x24a38210(self):
		return (self.neuron0x24a34a10()*1.73493)
	def synapse0x24a38590(self):
		return (self.neuron0x24a34e80()*-1.18698)
	def synapse0x24a385d0(self):
		return (self.neuron0x24a351f0()*-2.85439)
	def synapse0x24a38610(self):
		return (self.neuron0x24a35630()*-0.291235)
	def synapse0x24a38650(self):
		return (self.neuron0x24a35a70()*0.7626)
	def synapse0x24a38690(self):
		return (self.neuron0x24a35eb0()*2.65399)
	def synapse0x24a386d0(self):
		return (self.neuron0x24a36340()*-1.93391)
	def synapse0x24a38710(self):
		return (self.neuron0x24a36780()*-3.30073)
	def synapse0x24a38750(self):
		return (self.neuron0x24a36bc0()*1.87909)
	def synapse0x24a38790(self):
		return (self.neuron0x24a37000()*0.058986)
	def synapse0x24a387d0(self):
		return (self.neuron0x24a37590()*-0.259473)
	def synapse0x24a38810(self):
		return (self.neuron0x24a379d0()*1.92949)
	def synapse0x24a38850(self):
		return (self.neuron0x24a37e10()*0.112681)
