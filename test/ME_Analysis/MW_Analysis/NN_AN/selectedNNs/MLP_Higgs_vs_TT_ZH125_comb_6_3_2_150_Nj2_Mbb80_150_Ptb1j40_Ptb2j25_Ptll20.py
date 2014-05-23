from math import exp

from math import tanh

class FinalV7/MLP_Higgs_vs_TT_ZH125_comb_6_3_2_150_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 22.4315)/3.22594
		self.input1 = (in1 - 24.3204)/1.258
		self.input2 = (in2 - 12.6542)/1.62116
		if index==0: return self.neuron0x145d1eb0();
		return 0.
	def neuron0x145ce500(self):
		return self.input0
	def neuron0x145ce840(self):
		return self.input1
	def neuron0x145ceb80(self):
		return self.input2
	def neuron0x145ceff0(self):
		input = -0.21842
		input = input + self.synapse0x145d7190()
		input = input + self.synapse0x10201270()
		input = input + self.synapse0x145cf2a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145cf2e0(self):
		input = 0.234063
		input = input + self.synapse0x145cf620()
		input = input + self.synapse0x145cf660()
		input = input + self.synapse0x145cf6a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145cf6e0(self):
		input = 1.94767
		input = input + self.synapse0x145cfa20()
		input = input + self.synapse0x145cfa60()
		input = input + self.synapse0x145cfaa0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145cfae0(self):
		input = -0.936175
		input = input + self.synapse0x145cfe20()
		input = input + self.synapse0x145cfe60()
		input = input + self.synapse0x145cfea0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145cfee0(self):
		input = -0.698
		input = input + self.synapse0x145d0220()
		input = input + self.synapse0x145d0260()
		input = input + self.synapse0x145d02a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d02e0(self):
		input = -0.0212373
		input = input + self.synapse0x145d0620()
		input = input + self.synapse0x145d0660()
		input = input + self.synapse0x102012b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d07b0(self):
		input = -0.225922
		input = input + self.synapse0x145d0a60()
		input = input + self.synapse0x145d0aa0()
		input = input + self.synapse0x145d0ae0()
		input = input + self.synapse0x145d0b20()
		input = input + self.synapse0x145d0b60()
		input = input + self.synapse0x145d0ba0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d0be0(self):
		input = 0.00277653
		input = input + self.synapse0x145d0f20()
		input = input + self.synapse0x145d0f60()
		input = input + self.synapse0x145d0fa0()
		input = input + self.synapse0x145d0fe0()
		input = input + self.synapse0x145d1020()
		input = input + self.synapse0x145d1060()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d10a0(self):
		input = 0.141791
		input = input + self.synapse0x145d13e0()
		input = input + self.synapse0x145d1420()
		input = input + self.synapse0x145d1460()
		input = input + self.synapse0x145d7140()
		input = input + self.synapse0x141969f0()
		input = input + self.synapse0x10201300()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d16b0(self):
		input = -3.06108
		input = input + self.synapse0x145d19f0()
		input = input + self.synapse0x145d1a30()
		input = input + self.synapse0x145d1a70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d1ab0(self):
		input = 1.22665
		input = input + self.synapse0x145d1df0()
		input = input + self.synapse0x145d1e30()
		input = input + self.synapse0x145d1e70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x145d1eb0(self):
		input = -2.75751
		input = input + self.synapse0x145d21f0()
		input = input + self.synapse0x145d2230()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x145d7190(self):
		return (self.neuron0x145ce500()*-1.26606)
	def synapse0x10201270(self):
		return (self.neuron0x145ce840()*-0.317126)
	def synapse0x145cf2a0(self):
		return (self.neuron0x145ceb80()*0.510375)
	def synapse0x145cf620(self):
		return (self.neuron0x145ce500()*0.514202)
	def synapse0x145cf660(self):
		return (self.neuron0x145ce840()*0.29468)
	def synapse0x145cf6a0(self):
		return (self.neuron0x145ceb80()*-0.268197)
	def synapse0x145cfa20(self):
		return (self.neuron0x145ce500()*1.4078)
	def synapse0x145cfa60(self):
		return (self.neuron0x145ce840()*-1.10335)
	def synapse0x145cfaa0(self):
		return (self.neuron0x145ceb80()*0.509504)
	def synapse0x145cfe20(self):
		return (self.neuron0x145ce500()*-2.00457)
	def synapse0x145cfe60(self):
		return (self.neuron0x145ce840()*0.810179)
	def synapse0x145cfea0(self):
		return (self.neuron0x145ceb80()*0.310367)
	def synapse0x145d0220(self):
		return (self.neuron0x145ce500()*1.54575)
	def synapse0x145d0260(self):
		return (self.neuron0x145ce840()*-0.821963)
	def synapse0x145d02a0(self):
		return (self.neuron0x145ceb80()*-1.65624)
	def synapse0x145d0620(self):
		return (self.neuron0x145ce500()*0.471635)
	def synapse0x145d0660(self):
		return (self.neuron0x145ce840()*-2.52576)
	def synapse0x102012b0(self):
		return (self.neuron0x145ceb80()*1.6523)
	def synapse0x145d0a60(self):
		return (self.neuron0x145ceff0()*0.274968)
	def synapse0x145d0aa0(self):
		return (self.neuron0x145cf2e0()*-0.9211)
	def synapse0x145d0ae0(self):
		return (self.neuron0x145cf6e0()*-1.36777)
	def synapse0x145d0b20(self):
		return (self.neuron0x145cfae0()*0.963055)
	def synapse0x145d0b60(self):
		return (self.neuron0x145cfee0()*-1.07571)
	def synapse0x145d0ba0(self):
		return (self.neuron0x145d02e0()*0.88895)
	def synapse0x145d0f20(self):
		return (self.neuron0x145ceff0()*-0.507435)
	def synapse0x145d0f60(self):
		return (self.neuron0x145cf2e0()*0.244033)
	def synapse0x145d0fa0(self):
		return (self.neuron0x145cf6e0()*1.36259)
	def synapse0x145d0fe0(self):
		return (self.neuron0x145cfae0()*-1.23828)
	def synapse0x145d1020(self):
		return (self.neuron0x145cfee0()*0.621996)
	def synapse0x145d1060(self):
		return (self.neuron0x145d02e0()*-1.06103)
	def synapse0x145d13e0(self):
		return (self.neuron0x145ceff0()*-0.349201)
	def synapse0x145d1420(self):
		return (self.neuron0x145cf2e0()*-0.421742)
	def synapse0x145d1460(self):
		return (self.neuron0x145cf6e0()*1.27432)
	def synapse0x145d7140(self):
		return (self.neuron0x145cfae0()*-1.9526)
	def synapse0x141969f0(self):
		return (self.neuron0x145cfee0()*0.740902)
	def synapse0x10201300(self):
		return (self.neuron0x145d02e0()*-1.38474)
	def synapse0x145d19f0(self):
		return (self.neuron0x145d07b0()*-1.42833)
	def synapse0x145d1a30(self):
		return (self.neuron0x145d0be0()*3.75747)
	def synapse0x145d1a70(self):
		return (self.neuron0x145d10a0()*3.00697)
	def synapse0x145d1df0(self):
		return (self.neuron0x145d07b0()*0.598386)
	def synapse0x145d1e30(self):
		return (self.neuron0x145d0be0()*-2.48567)
	def synapse0x145d1e70(self):
		return (self.neuron0x145d10a0()*-2.32495)
	def synapse0x145d21f0(self):
		return (self.neuron0x145d16b0()*8.88343)
	def synapse0x145d2230(self):
		return (self.neuron0x145d1ab0()*-3.72635)
