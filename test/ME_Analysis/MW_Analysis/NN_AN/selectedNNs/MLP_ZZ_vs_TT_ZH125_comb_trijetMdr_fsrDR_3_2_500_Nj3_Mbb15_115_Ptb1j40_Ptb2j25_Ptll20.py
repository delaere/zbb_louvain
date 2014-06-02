from math import exp

from math import tanh

class Final12/MLP_ZZ_vs_TT_ZH125_comb_trijetMdr_fsrDR_3_2_500_Nj3_Mbb15_115_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4):
		self.input0 = (in0 - 22.1385)/2.5002
		self.input1 = (in1 - 21.3492)/1.92682
		self.input2 = (in2 - 10.929)/1.53598
		self.input3 = (in3 - 10.1565)/34.0949
		self.input4 = (in4 - 1.77307)/0.814378
		if index==0: return self.neuron0x346a9400();
		return 0.
	def neuron0x346a6e60(self):
		return self.input0
	def neuron0x346a7110(self):
		return self.input1
	def neuron0x346a7450(self):
		return self.input2
	def neuron0x346a7790(self):
		return self.input3
	def neuron0x346a7ad0(self):
		return self.input4
	def neuron0x346a7f40(self):
		input = -0.459377
		input = input + self.synapse0x346677e0()
		input = input + self.synapse0x3460eb60()
		input = input + self.synapse0x346962d0()
		input = input + self.synapse0x346a81f0()
		input = input + self.synapse0x346a8230()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x346a8270(self):
		input = -2.89946
		input = input + self.synapse0x346a85b0()
		input = input + self.synapse0x346a85f0()
		input = input + self.synapse0x346a8630()
		input = input + self.synapse0x346a8670()
		input = input + self.synapse0x346a86b0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x346a86f0(self):
		input = 5.20711
		input = input + self.synapse0x346a8a30()
		input = input + self.synapse0x346a8a70()
		input = input + self.synapse0x346a8ab0()
		input = input + self.synapse0x346a8af0()
		input = input + self.synapse0x346a8b30()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x346a8b70(self):
		input = -2.06274
		input = input + self.synapse0x346a8eb0()
		input = input + self.synapse0x346a8ef0()
		input = input + self.synapse0x3460e6a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x346a9040(self):
		input = 4.31137
		input = input + self.synapse0x3460e6e0()
		input = input + self.synapse0x346a9380()
		input = input + self.synapse0x346a93c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x346a9400(self):
		input = 0.627507
		input = input + self.synapse0x346a9620()
		input = input + self.synapse0x346a9660()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x346677e0(self):
		return (self.neuron0x346a6e60()*1.96967)
	def synapse0x3460eb60(self):
		return (self.neuron0x346a7110()*0.274329)
	def synapse0x346962d0(self):
		return (self.neuron0x346a7450()*-1.90656)
	def synapse0x346a81f0(self):
		return (self.neuron0x346a7790()*-0.0151211)
	def synapse0x346a8230(self):
		return (self.neuron0x346a7ad0()*0.0775719)
	def synapse0x346a85b0(self):
		return (self.neuron0x346a6e60()*-0.0906499)
	def synapse0x346a85f0(self):
		return (self.neuron0x346a7110()*0.020969)
	def synapse0x346a8630(self):
		return (self.neuron0x346a7450()*2.33168)
	def synapse0x346a8670(self):
		return (self.neuron0x346a7790()*0.024352)
	def synapse0x346a86b0(self):
		return (self.neuron0x346a7ad0()*-0.0900179)
	def synapse0x346a8a30(self):
		return (self.neuron0x346a6e60()*1.46146)
	def synapse0x346a8a70(self):
		return (self.neuron0x346a7110()*-3.23227)
	def synapse0x346a8ab0(self):
		return (self.neuron0x346a7450()*-0.963121)
	def synapse0x346a8af0(self):
		return (self.neuron0x346a7790()*-0.00474405)
	def synapse0x346a8b30(self):
		return (self.neuron0x346a7ad0()*0.0489739)
	def synapse0x346a8eb0(self):
		return (self.neuron0x346a7f40()*1.69497)
	def synapse0x346a8ef0(self):
		return (self.neuron0x346a8270()*1.19567)
	def synapse0x3460e6a0(self):
		return (self.neuron0x346a86f0()*2.40614)
	def synapse0x3460e6e0(self):
		return (self.neuron0x346a7f40()*-3.1946)
	def synapse0x346a9380(self):
		return (self.neuron0x346a8270()*-3.87097)
	def synapse0x346a93c0(self):
		return (self.neuron0x346a86f0()*-3.37775)
	def synapse0x346a9620(self):
		return (self.neuron0x346a8b70()*4.10422)
	def synapse0x346a9660(self):
		return (self.neuron0x346a9040()*-9.32061)
