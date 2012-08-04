from math import exp

from math import tanh

class ../NN/MLP_Zbb_tt_Comb_met_EE:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 20.3256)/1.0298
		self.input1 = (in1 - 21.0098)/0.967296
		self.input2 = (in2 - 21.5918)/0.86144
		self.input3 = (in3 - 31.892)/15.308
		if index==0: return self.neuron0x11b9afe0();
		return 0.
	def neuron0x11bc2690(self):
		return self.input0
	def neuron0x11bc29a0(self):
		return self.input1
	def neuron0x11b981e0(self):
		return self.input2
	def neuron0x11b98520(self):
		return self.input3
	def neuron0x11b989a0(self):
		input = -0.0341202
		input = input + self.synapse0x11b3e9b0()
		input = input + self.synapse0x15416360()
		input = input + self.synapse0x154162e0()
		input = input + self.synapse0x11bc2490()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b98c20(self):
		input = 0.630851
		input = input + self.synapse0x11b3ea40()
		input = input + self.synapse0x11b98f30()
		input = input + self.synapse0x11b98f70()
		input = input + self.synapse0x11b98fb0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b98ff0(self):
		input = -1.13902
		input = input + self.synapse0x11b99300()
		input = input + self.synapse0x11b99340()
		input = input + self.synapse0x11b99380()
		input = input + self.synapse0x11b993c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b99400(self):
		input = -0.906292
		input = input + self.synapse0x11b99710()
		input = input + self.synapse0x11b99750()
		input = input + self.synapse0x11b99790()
		input = input + self.synapse0x11b997d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b99810(self):
		input = -3.20617
		input = input + self.synapse0x11b99b20()
		input = input + self.synapse0x11bc2b90()
		input = input + self.synapse0x12a12040()
		input = input + self.synapse0x12ab56c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b99c70(self):
		input = 0.0619692
		input = input + self.synapse0x11b99f80()
		input = input + self.synapse0x11b99fc0()
		input = input + self.synapse0x11b9a000()
		input = input + self.synapse0x11b9a040()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b9a080(self):
		input = 1.74288
		input = input + self.synapse0x11b9a390()
		input = input + self.synapse0x11b9a3d0()
		input = input + self.synapse0x11b9a410()
		input = input + self.synapse0x11b9a450()
		input = input + self.synapse0x11b9a490()
		input = input + self.synapse0x11b9a4d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b9a510(self):
		input = -4.33016
		input = input + self.synapse0x11b9a850()
		input = input + self.synapse0x11b9a890()
		input = input + self.synapse0x11b9a8d0()
		input = input + self.synapse0x11bc2440()
		input = input + self.synapse0x11b438c0()
		input = input + self.synapse0x12ab5700()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b9ab20(self):
		input = 0.835206
		input = input + self.synapse0x11b9ae60()
		input = input + self.synapse0x11b9aea0()
		input = input + self.synapse0x11b9aee0()
		input = input + self.synapse0x11b9af20()
		input = input + self.synapse0x11b9af60()
		input = input + self.synapse0x11b9afa0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b9afe0(self):
		input = 3.06218
		input = input + self.synapse0x11b9b320()
		input = input + self.synapse0x11b9b360()
		input = input + self.synapse0x11b9b3a0()
		return (input*1)+0
	def synapse0x11b3e9b0(self):
		return (self.neuron0x11bc2690()*1.35509)
	def synapse0x15416360(self):
		return (self.neuron0x11bc29a0()*-0.0876492)
	def synapse0x154162e0(self):
		return (self.neuron0x11b981e0()*3.83336)
	def synapse0x11bc2490(self):
		return (self.neuron0x11b98520()*0.0141313)
	def synapse0x11b3ea40(self):
		return (self.neuron0x11bc2690()*-1.39583)
	def synapse0x11b98f30(self):
		return (self.neuron0x11bc29a0()*-5.61967)
	def synapse0x11b98f70(self):
		return (self.neuron0x11b981e0()*3.50269)
	def synapse0x11b98fb0(self):
		return (self.neuron0x11b98520()*-0.969692)
	def synapse0x11b99300(self):
		return (self.neuron0x11bc2690()*-3.36786)
	def synapse0x11b99340(self):
		return (self.neuron0x11bc29a0()*-0.721964)
	def synapse0x11b99380(self):
		return (self.neuron0x11b981e0()*2.0201)
	def synapse0x11b993c0(self):
		return (self.neuron0x11b98520()*-1.0777)
	def synapse0x11b99710(self):
		return (self.neuron0x11bc2690()*-1.01606)
	def synapse0x11b99750(self):
		return (self.neuron0x11bc29a0()*-1.39868)
	def synapse0x11b99790(self):
		return (self.neuron0x11b981e0()*3.24592)
	def synapse0x11b997d0(self):
		return (self.neuron0x11b98520()*-4.59873)
	def synapse0x11b99b20(self):
		return (self.neuron0x11bc2690()*-1.37829)
	def synapse0x11bc2b90(self):
		return (self.neuron0x11bc29a0()*-0.660048)
	def synapse0x12a12040(self):
		return (self.neuron0x11b981e0()*2.73114)
	def synapse0x12ab56c0(self):
		return (self.neuron0x11b98520()*-1.92307)
	def synapse0x11b99f80(self):
		return (self.neuron0x11bc2690()*0.399087)
	def synapse0x11b99fc0(self):
		return (self.neuron0x11bc29a0()*0.0322995)
	def synapse0x11b9a000(self):
		return (self.neuron0x11b981e0()*1.67433)
	def synapse0x11b9a040(self):
		return (self.neuron0x11b98520()*0.0343952)
	def synapse0x11b9a390(self):
		return (self.neuron0x11b989a0()*0.130654)
	def synapse0x11b9a3d0(self):
		return (self.neuron0x11b98c20()*0.190429)
	def synapse0x11b9a410(self):
		return (self.neuron0x11b98ff0()*1.78991)
	def synapse0x11b9a450(self):
		return (self.neuron0x11b99400()*-1.28782)
	def synapse0x11b9a490(self):
		return (self.neuron0x11b99810()*1.28355)
	def synapse0x11b9a4d0(self):
		return (self.neuron0x11b99c70()*-0.523429)
	def synapse0x11b9a850(self):
		return (self.neuron0x11b989a0()*-0.202836)
	def synapse0x11b9a890(self):
		return (self.neuron0x11b98c20()*2.00151)
	def synapse0x11b9a8d0(self):
		return (self.neuron0x11b98ff0()*-0.398815)
	def synapse0x11bc2440(self):
		return (self.neuron0x11b99400()*1.84242)
	def synapse0x11b438c0(self):
		return (self.neuron0x11b99810()*2.20245)
	def synapse0x12ab5700(self):
		return (self.neuron0x11b99c70()*-0.0137901)
	def synapse0x11b9ae60(self):
		return (self.neuron0x11b989a0()*0.919129)
	def synapse0x11b9aea0(self):
		return (self.neuron0x11b98c20()*0.299754)
	def synapse0x11b9aee0(self):
		return (self.neuron0x11b98ff0()*-1.21633)
	def synapse0x11b9af20(self):
		return (self.neuron0x11b99400()*0.739003)
	def synapse0x11b9af60(self):
		return (self.neuron0x11b99810()*2.36841)
	def synapse0x11b9afa0(self):
		return (self.neuron0x11b99c70()*-1.56115)
	def synapse0x11b9b320(self):
		return (self.neuron0x11b9a080()*-1.89611)
	def synapse0x11b9b360(self):
		return (self.neuron0x11b9a510()*2.55145)
	def synapse0x11b9b3a0(self):
		return (self.neuron0x11b9ab20()*-2.37445)
