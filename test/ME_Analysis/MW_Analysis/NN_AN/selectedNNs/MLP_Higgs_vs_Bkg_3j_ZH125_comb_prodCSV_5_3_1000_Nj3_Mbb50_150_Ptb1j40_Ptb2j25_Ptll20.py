from math import exp

from math import tanh

class Final11/MLP_Higgs_vs_Bkg_3j_ZH125_comb_prodCSV_5_3_1000_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 0.46033)/0.237691
		self.input1 = (in1 - 0.512403)/0.275496
		self.input2 = (in2 - 0.527936)/0.286352
		self.input3 = (in3 - 0.639559)/0.256908
		if index==0: return self.neuron0x35da7aa0();
		return 0.
	def neuron0x35da48e0(self):
		return self.input0
	def neuron0x35da4c20(self):
		return self.input1
	def neuron0x35da4f60(self):
		return self.input2
	def neuron0x35da52a0(self):
		return self.input3
	def neuron0x35da5710(self):
		input = -1.02591
		input = input + self.synapse0x35d93b40()
		input = input + self.synapse0x35d21ba0()
		input = input + self.synapse0x35d21be0()
		input = input + self.synapse0x35da59c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da5a00(self):
		input = 3.83862
		input = input + self.synapse0x35da5d40()
		input = input + self.synapse0x35da5d80()
		input = input + self.synapse0x35da5dc0()
		input = input + self.synapse0x35da5e00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da5e40(self):
		input = 4.24296
		input = input + self.synapse0x35da6180()
		input = input + self.synapse0x35da61c0()
		input = input + self.synapse0x35da6200()
		input = input + self.synapse0x35da6240()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da6280(self):
		input = 3.5656
		input = input + self.synapse0x35da65c0()
		input = input + self.synapse0x35da6600()
		input = input + self.synapse0x35da6640()
		input = input + self.synapse0x35da6680()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da66c0(self):
		input = -1.62931
		input = input + self.synapse0x35da6a00()
		input = input + self.synapse0x35d21700()
		input = input + self.synapse0x35d21740()
		input = input + self.synapse0x35da6b50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da6b90(self):
		input = 0.932811
		input = input + self.synapse0x35da6ed0()
		input = input + self.synapse0x35da6f10()
		input = input + self.synapse0x35da6f50()
		input = input + self.synapse0x35da6f90()
		input = input + self.synapse0x35da6fd0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da7010(self):
		input = -0.989269
		input = input + self.synapse0x35da7350()
		input = input + self.synapse0x35da7390()
		input = input + self.synapse0x35da73d0()
		input = input + self.synapse0x35da7410()
		input = input + self.synapse0x35da7450()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da7490(self):
		input = -0.563702
		input = input + self.synapse0x35da77d0()
		input = input + self.synapse0x35da7810()
		input = input + self.synapse0x35da7850()
		input = input + self.synapse0x35d21b50()
		input = input + self.synapse0x35d93ac0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x35da7aa0(self):
		input = 3.03419
		input = input + self.synapse0x35d93b00()
		input = input + self.synapse0x35da5670()
		input = input + self.synapse0x35da56b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x35d93b40(self):
		return (self.neuron0x35da48e0()*-0.432204)
	def synapse0x35d21ba0(self):
		return (self.neuron0x35da4c20()*0.454449)
	def synapse0x35d21be0(self):
		return (self.neuron0x35da4f60()*1.01856)
	def synapse0x35da59c0(self):
		return (self.neuron0x35da52a0()*-0.130958)
	def synapse0x35da5d40(self):
		return (self.neuron0x35da48e0()*0.995659)
	def synapse0x35da5d80(self):
		return (self.neuron0x35da4c20()*0.995967)
	def synapse0x35da5dc0(self):
		return (self.neuron0x35da4f60()*0.0842328)
	def synapse0x35da5e00(self):
		return (self.neuron0x35da52a0()*-0.33623)
	def synapse0x35da6180(self):
		return (self.neuron0x35da48e0()*-1.16313)
	def synapse0x35da61c0(self):
		return (self.neuron0x35da4c20()*0.0745181)
	def synapse0x35da6200(self):
		return (self.neuron0x35da4f60()*-0.676147)
	def synapse0x35da6240(self):
		return (self.neuron0x35da52a0()*-0.22729)
	def synapse0x35da65c0(self):
		return (self.neuron0x35da48e0()*0.337888)
	def synapse0x35da6600(self):
		return (self.neuron0x35da4c20()*-0.780896)
	def synapse0x35da6640(self):
		return (self.neuron0x35da4f60()*1.29326)
	def synapse0x35da6680(self):
		return (self.neuron0x35da52a0()*-0.528718)
	def synapse0x35da6a00(self):
		return (self.neuron0x35da48e0()*-0.557046)
	def synapse0x35d21700(self):
		return (self.neuron0x35da4c20()*-0.232388)
	def synapse0x35d21740(self):
		return (self.neuron0x35da4f60()*-0.394391)
	def synapse0x35da6b50(self):
		return (self.neuron0x35da52a0()*-0.895533)
	def synapse0x35da6ed0(self):
		return (self.neuron0x35da5710()*-0.250882)
	def synapse0x35da6f10(self):
		return (self.neuron0x35da5a00()*-1.24711)
	def synapse0x35da6f50(self):
		return (self.neuron0x35da5e40()*2.0887)
	def synapse0x35da6f90(self):
		return (self.neuron0x35da6280()*-1.24785)
	def synapse0x35da6fd0(self):
		return (self.neuron0x35da66c0()*0.707453)
	def synapse0x35da7350(self):
		return (self.neuron0x35da5710()*1.03249)
	def synapse0x35da7390(self):
		return (self.neuron0x35da5a00()*1.02468)
	def synapse0x35da73d0(self):
		return (self.neuron0x35da5e40()*-2.42174)
	def synapse0x35da7410(self):
		return (self.neuron0x35da6280()*1.05023)
	def synapse0x35da7450(self):
		return (self.neuron0x35da66c0()*-1.43649)
	def synapse0x35da77d0(self):
		return (self.neuron0x35da5710()*2.53838)
	def synapse0x35da7810(self):
		return (self.neuron0x35da5a00()*-2.94391)
	def synapse0x35da7850(self):
		return (self.neuron0x35da5e40()*4.2163)
	def synapse0x35d21b50(self):
		return (self.neuron0x35da6280()*-3.34918)
	def synapse0x35d93ac0(self):
		return (self.neuron0x35da66c0()*1.1416)
	def synapse0x35d93b00(self):
		return (self.neuron0x35da6b90()*-3.1046)
	def synapse0x35da5670(self):
		return (self.neuron0x35da7010()*4.51598)
	def synapse0x35da56b0(self):
		return (self.neuron0x35da7490()*-9.70837)
