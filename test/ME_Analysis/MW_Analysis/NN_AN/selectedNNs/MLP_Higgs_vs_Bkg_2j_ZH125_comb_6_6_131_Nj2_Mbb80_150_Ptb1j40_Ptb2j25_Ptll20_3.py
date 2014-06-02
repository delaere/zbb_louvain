from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_Bkg_2j_ZH125_comb_6_6_131_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20_3:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.500017)/0.25242
		self.input1 = (in1 - 0.592179)/0.338539
		self.input2 = (in2 - 0.679468)/0.281065
		if index==0: return self.neuron0x2923b480();
		return 0.
	def neuron0x292375e0(self):
		return self.input0
	def neuron0x29237890(self):
		return self.input1
	def neuron0x29237bd0(self):
		return self.input2
	def neuron0x29238040(self):
		input = -3.54726
		input = input + self.synapse0x29226a10()
		input = input + self.synapse0x29226a50()
		input = input + self.synapse0x292382f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29238330(self):
		input = -0.0812031
		input = input + self.synapse0x29238670()
		input = input + self.synapse0x292386b0()
		input = input + self.synapse0x292386f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29238730(self):
		input = 1.67389
		input = input + self.synapse0x29238a70()
		input = input + self.synapse0x29238ab0()
		input = input + self.synapse0x29238af0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29238b30(self):
		input = -1.79907
		input = input + self.synapse0x29238e70()
		input = input + self.synapse0x29238eb0()
		input = input + self.synapse0x29238ef0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29238f30(self):
		input = 1.17917
		input = input + self.synapse0x29239270()
		input = input + self.synapse0x292392b0()
		input = input + self.synapse0x292392f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29239330(self):
		input = -1.87417
		input = input + self.synapse0x29239670()
		input = input + self.synapse0x292396b0()
		input = input + self.synapse0x291cba60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29239800(self):
		input = -0.140583
		input = input + self.synapse0x291cbaa0()
		input = input + self.synapse0x29239b40()
		input = input + self.synapse0x29239b80()
		input = input + self.synapse0x29239bc0()
		input = input + self.synapse0x29239c00()
		input = input + self.synapse0x29239c40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x29239c80(self):
		input = -0.00171116
		input = input + self.synapse0x29239fc0()
		input = input + self.synapse0x2923a000()
		input = input + self.synapse0x2923a040()
		input = input + self.synapse0x2923a080()
		input = input + self.synapse0x2923a0c0()
		input = input + self.synapse0x2923a100()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2923a140(self):
		input = -0.196101
		input = input + self.synapse0x2923a480()
		input = input + self.synapse0x2923a4c0()
		input = input + self.synapse0x2923a500()
		input = input + self.synapse0x291cbe70()
		input = input + self.synapse0x291cbf50()
		input = input + self.synapse0x291cbf90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2923a750(self):
		input = 0.039299
		input = input + self.synapse0x29239780()
		input = input + self.synapse0x292397c0()
		input = input + self.synapse0x2923aa00()
		input = input + self.synapse0x2923aa40()
		input = input + self.synapse0x2923aa80()
		input = input + self.synapse0x2923aac0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2923ab00(self):
		input = 0.0163075
		input = input + self.synapse0x2923ae40()
		input = input + self.synapse0x2923ae80()
		input = input + self.synapse0x2923aec0()
		input = input + self.synapse0x2923af00()
		input = input + self.synapse0x2923af40()
		input = input + self.synapse0x2923af80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2923afc0(self):
		input = 0.106204
		input = input + self.synapse0x2923b300()
		input = input + self.synapse0x2923b340()
		input = input + self.synapse0x2923b380()
		input = input + self.synapse0x2923b3c0()
		input = input + self.synapse0x2923b400()
		input = input + self.synapse0x2923b440()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2923b480(self):
		input = 0.488792
		input = input + self.synapse0x29237f10()
		input = input + self.synapse0x29237fe0()
		input = input + self.synapse0x2923b730()
		input = input + self.synapse0x2923b770()
		input = input + self.synapse0x2923b7b0()
		input = input + self.synapse0x2923b7f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x29226a10(self):
		return (self.neuron0x292375e0()*-1.82401)
	def synapse0x29226a50(self):
		return (self.neuron0x29237890()*-0.246655)
	def synapse0x292382f0(self):
		return (self.neuron0x29237bd0()*0.0696949)
	def synapse0x29238670(self):
		return (self.neuron0x292375e0()*0.0395607)
	def synapse0x292386b0(self):
		return (self.neuron0x29237890()*0.784165)
	def synapse0x292386f0(self):
		return (self.neuron0x29237bd0()*0.0522537)
	def synapse0x29238a70(self):
		return (self.neuron0x292375e0()*-0.894786)
	def synapse0x29238ab0(self):
		return (self.neuron0x29237890()*1.72249)
	def synapse0x29238af0(self):
		return (self.neuron0x29237bd0()*0.221621)
	def synapse0x29238e70(self):
		return (self.neuron0x292375e0()*0.770492)
	def synapse0x29238eb0(self):
		return (self.neuron0x29237890()*0.138352)
	def synapse0x29238ef0(self):
		return (self.neuron0x29237bd0()*0.232703)
	def synapse0x29239270(self):
		return (self.neuron0x292375e0()*0.150702)
	def synapse0x292392b0(self):
		return (self.neuron0x29237890()*0.452883)
	def synapse0x292392f0(self):
		return (self.neuron0x29237bd0()*0.0777144)
	def synapse0x29239670(self):
		return (self.neuron0x292375e0()*0.744193)
	def synapse0x292396b0(self):
		return (self.neuron0x29237890()*-0.0841958)
	def synapse0x291cba60(self):
		return (self.neuron0x29237bd0()*0.16081)
	def synapse0x291cbaa0(self):
		return (self.neuron0x29238040()*1.83441)
	def synapse0x29239b40(self):
		return (self.neuron0x29238330()*0.580619)
	def synapse0x29239b80(self):
		return (self.neuron0x29238730()*-0.8446)
	def synapse0x29239bc0(self):
		return (self.neuron0x29238b30()*-1.38016)
	def synapse0x29239c00(self):
		return (self.neuron0x29238f30()*1.3331)
	def synapse0x29239c40(self):
		return (self.neuron0x29239330()*-1.06921)
	def synapse0x29239fc0(self):
		return (self.neuron0x29238040()*-1.14034)
	def synapse0x2923a000(self):
		return (self.neuron0x29238330()*-1.23978)
	def synapse0x2923a040(self):
		return (self.neuron0x29238730()*0.741657)
	def synapse0x2923a080(self):
		return (self.neuron0x29238b30()*1.58621)
	def synapse0x2923a0c0(self):
		return (self.neuron0x29238f30()*-1.25438)
	def synapse0x2923a100(self):
		return (self.neuron0x29239330()*1.51565)
	def synapse0x2923a480(self):
		return (self.neuron0x29238040()*-1.34674)
	def synapse0x2923a4c0(self):
		return (self.neuron0x29238330()*-0.194419)
	def synapse0x2923a500(self):
		return (self.neuron0x29238730()*0.560091)
	def synapse0x291cbe70(self):
		return (self.neuron0x29238b30()*0.940709)
	def synapse0x291cbf50(self):
		return (self.neuron0x29238f30()*-0.287631)
	def synapse0x291cbf90(self):
		return (self.neuron0x29239330()*0.825554)
	def synapse0x29239780(self):
		return (self.neuron0x29238040()*-1.04247)
	def synapse0x292397c0(self):
		return (self.neuron0x29238330()*-0.51005)
	def synapse0x2923aa00(self):
		return (self.neuron0x29238730()*0.0959321)
	def synapse0x2923aa40(self):
		return (self.neuron0x29238b30()*0.338553)
	def synapse0x2923aa80(self):
		return (self.neuron0x29238f30()*-0.679893)
	def synapse0x2923aac0(self):
		return (self.neuron0x29239330()*1.30021)
	def synapse0x2923ae40(self):
		return (self.neuron0x29238040()*-0.162993)
	def synapse0x2923ae80(self):
		return (self.neuron0x29238330()*-0.643888)
	def synapse0x2923aec0(self):
		return (self.neuron0x29238730()*1.2564)
	def synapse0x2923af00(self):
		return (self.neuron0x29238b30()*0.60598)
	def synapse0x2923af40(self):
		return (self.neuron0x29238f30()*-0.184876)
	def synapse0x2923af80(self):
		return (self.neuron0x29239330()*0.071494)
	def synapse0x2923b300(self):
		return (self.neuron0x29238040()*1.39966)
	def synapse0x2923b340(self):
		return (self.neuron0x29238330()*0.565472)
	def synapse0x2923b380(self):
		return (self.neuron0x29238730()*-1.01402)
	def synapse0x2923b3c0(self):
		return (self.neuron0x29238b30()*-1.65903)
	def synapse0x2923b400(self):
		return (self.neuron0x29238f30()*1.32508)
	def synapse0x2923b440(self):
		return (self.neuron0x29239330()*-0.963351)
	def synapse0x29237f10(self):
		return (self.neuron0x29239800()*-4.76678)
	def synapse0x29237fe0(self):
		return (self.neuron0x29239c80()*5.55044)
	def synapse0x2923b730(self):
		return (self.neuron0x2923a140()*2.07243)
	def synapse0x2923b770(self):
		return (self.neuron0x2923a750()*1.75912)
	def synapse0x2923b7b0(self):
		return (self.neuron0x2923ab00()*1.00721)
	def synapse0x2923b7f0(self):
		return (self.neuron0x2923afc0()*-3.82828)
