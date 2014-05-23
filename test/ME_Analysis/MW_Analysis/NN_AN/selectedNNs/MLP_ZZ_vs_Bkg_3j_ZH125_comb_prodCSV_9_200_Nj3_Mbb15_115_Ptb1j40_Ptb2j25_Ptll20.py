from math import exp

from math import tanh

class Final13/MLP_ZZ_vs_Bkg_3j_ZH125_comb_prodCSV_9_200_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.477235)/0.179129
		self.input1 = (in1 - 0.563571)/0.303163
		self.input2 = (in2 - 0.614876)/0.258553
		if index==0: return self.neuron0x36ca7740();
		return 0.
	def neuron0x36c93d60(self):
		return self.input0
	def neuron0x36c940a0(self):
		return self.input1
	def neuron0x36ca5070(self):
		return self.input2
	def neuron0x36ca53c0(self):
		input = 0.602971
		input = input + self.synapse0x36c3b7a0()
		input = input + self.synapse0x36c3b7e0()
		input = input + self.synapse0x36ca5670()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca56b0(self):
		input = 1.29742
		input = input + self.synapse0x36ca59f0()
		input = input + self.synapse0x36ca5a30()
		input = input + self.synapse0x36ca5a70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca5ab0(self):
		input = 0.131621
		input = input + self.synapse0x36ca5df0()
		input = input + self.synapse0x36ca5e30()
		input = input + self.synapse0x36ca5e70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca5eb0(self):
		input = -0.710056
		input = input + self.synapse0x36ca61f0()
		input = input + self.synapse0x36ca6230()
		input = input + self.synapse0x36ca6270()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca62b0(self):
		input = 2.67348
		input = input + self.synapse0x36ca65f0()
		input = input + self.synapse0x36ca6630()
		input = input + self.synapse0x36ca6670()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca66b0(self):
		input = 0.926045
		input = input + self.synapse0x36ca69f0()
		input = input + self.synapse0x36ca6a30()
		input = input + self.synapse0x36c3b380()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca6b80(self):
		input = -0.25386
		input = input + self.synapse0x36c3b3c0()
		input = input + self.synapse0x36ca6ec0()
		input = input + self.synapse0x36ca6f00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca6f40(self):
		input = -4.5283
		input = input + self.synapse0x36ca7280()
		input = input + self.synapse0x36ca72c0()
		input = input + self.synapse0x36ca7300()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca7340(self):
		input = 3.40211
		input = input + self.synapse0x36ca7680()
		input = input + self.synapse0x36ca76c0()
		input = input + self.synapse0x36ca7700()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x36ca7740(self):
		input = -0.521386
		input = input + self.synapse0x36ca5290()
		input = input + self.synapse0x36ca5360()
		input = input + self.synapse0x36ca79f0()
		input = input + self.synapse0x36ca7a30()
		input = input + self.synapse0x36ca7a70()
		input = input + self.synapse0x36ca7ab0()
		input = input + self.synapse0x36775170()
		input = input + self.synapse0x36c3b830()
		input = input + self.synapse0x36c3b870()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x36c3b7a0(self):
		return (self.neuron0x36c93d60()*-2.18335)
	def synapse0x36c3b7e0(self):
		return (self.neuron0x36c940a0()*0.0857444)
	def synapse0x36ca5670(self):
		return (self.neuron0x36ca5070()*-0.38929)
	def synapse0x36ca59f0(self):
		return (self.neuron0x36c93d60()*2.56531)
	def synapse0x36ca5a30(self):
		return (self.neuron0x36c940a0()*-0.141882)
	def synapse0x36ca5a70(self):
		return (self.neuron0x36ca5070()*5.84083)
	def synapse0x36ca5df0(self):
		return (self.neuron0x36c93d60()*0.388345)
	def synapse0x36ca5e30(self):
		return (self.neuron0x36c940a0()*0.0496091)
	def synapse0x36ca5e70(self):
		return (self.neuron0x36ca5070()*-0.156401)
	def synapse0x36ca61f0(self):
		return (self.neuron0x36c93d60()*-1.15639)
	def synapse0x36ca6230(self):
		return (self.neuron0x36c940a0()*0.581205)
	def synapse0x36ca6270(self):
		return (self.neuron0x36ca5070()*-0.294001)
	def synapse0x36ca65f0(self):
		return (self.neuron0x36c93d60()*-0.822051)
	def synapse0x36ca6630(self):
		return (self.neuron0x36c940a0()*-0.812958)
	def synapse0x36ca6670(self):
		return (self.neuron0x36ca5070()*-1.45747)
	def synapse0x36ca69f0(self):
		return (self.neuron0x36c93d60()*-0.284668)
	def synapse0x36ca6a30(self):
		return (self.neuron0x36c940a0()*-0.165089)
	def synapse0x36c3b380(self):
		return (self.neuron0x36ca5070()*0.660346)
	def synapse0x36c3b3c0(self):
		return (self.neuron0x36c93d60()*0.711735)
	def synapse0x36ca6ec0(self):
		return (self.neuron0x36c940a0()*-0.297217)
	def synapse0x36ca6f00(self):
		return (self.neuron0x36ca5070()*-0.102536)
	def synapse0x36ca7280(self):
		return (self.neuron0x36c93d60()*-0.443815)
	def synapse0x36ca72c0(self):
		return (self.neuron0x36c940a0()*-2.11611)
	def synapse0x36ca7300(self):
		return (self.neuron0x36ca5070()*0.606064)
	def synapse0x36ca7680(self):
		return (self.neuron0x36c93d60()*0.599568)
	def synapse0x36ca76c0(self):
		return (self.neuron0x36c940a0()*-0.645846)
	def synapse0x36ca7700(self):
		return (self.neuron0x36ca5070()*-1.63897)
	def synapse0x36ca5290(self):
		return (self.neuron0x36ca53c0()*0.909905)
	def synapse0x36ca5360(self):
		return (self.neuron0x36ca56b0()*0.958483)
	def synapse0x36ca79f0(self):
		return (self.neuron0x36ca5ab0()*1.20556)
	def synapse0x36ca7a30(self):
		return (self.neuron0x36ca5eb0()*-1.44344)
	def synapse0x36ca7a70(self):
		return (self.neuron0x36ca62b0()*-1.81856)
	def synapse0x36ca7ab0(self):
		return (self.neuron0x36ca66b0()*-1.52492)
	def synapse0x36775170(self):
		return (self.neuron0x36ca6b80()*0.369875)
	def synapse0x36c3b830(self):
		return (self.neuron0x36ca6f40()*-3.65439)
	def synapse0x36c3b870(self):
		return (self.neuron0x36ca7340()*2.15357)
