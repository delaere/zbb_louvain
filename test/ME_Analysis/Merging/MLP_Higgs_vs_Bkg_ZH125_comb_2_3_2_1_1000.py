from math import exp

from math import tanh

class MLP_Higgs_vs_Bkg_ZH125_comb_2_3_2_1_1000:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.445235)/0.307413
		self.input1 = (in1 - 0.487302)/0.29068
		self.input2 = (in2 - 0.530975)/0.330691
		if index==0: return self.neuron0x7a87a10();
		return 0.
	def neuron0x7a74530(self):
		return self.input0
	def neuron0x7a74870(self):
		return self.input1
	def neuron0x7a85840(self):
		return self.input2
	def neuron0x7a85b90(self):
		input = -0.259654
		input = input + self.synapse0x7a3cd00()
		input = input + self.synapse0x7a5b290()
		input = input + self.synapse0x7a85e40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a85e80(self):
		input = -0.905738
		input = input + self.synapse0x7a861c0()
		input = input + self.synapse0x7a86200()
		input = input + self.synapse0x7a86240()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a86280(self):
		input = -0.193664
		input = input + self.synapse0x7a865c0()
		input = input + self.synapse0x7a86600()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a86640(self):
		input = -0.750552
		input = input + self.synapse0x7a86980()
		input = input + self.synapse0x7a869c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a86a00(self):
		input = 0.0260944
		input = input + self.synapse0x7a86d40()
		input = input + self.synapse0x7a86d80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a86dc0(self):
		input = -1.60122
		input = input + self.synapse0x7a87100()
		input = input + self.synapse0x7a87140()
		input = input + self.synapse0x7a87180()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a871c0(self):
		input = 0.698238
		input = input + self.synapse0x7a87500()
		input = input + self.synapse0x7a87540()
		input = input + self.synapse0x79e74a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a87690(self):
		input = -2.71241
		input = input + self.synapse0x79e74e0()
		input = input + self.synapse0x7a879d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x7a87a10(self):
		input = 11.2457
		input = input + self.synapse0x7a85a60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x7a3cd00(self):
		return (self.neuron0x7a74530()*0.134396)
	def synapse0x7a5b290(self):
		return (self.neuron0x7a74870()*0.148151)
	def synapse0x7a85e40(self):
		return (self.neuron0x7a85840()*-0.251209)
	def synapse0x7a861c0(self):
		return (self.neuron0x7a74530()*0.0558178)
	def synapse0x7a86200(self):
		return (self.neuron0x7a74870()*0.0984276)
	def synapse0x7a86240(self):
		return (self.neuron0x7a85840()*-0.163423)
	def synapse0x7a865c0(self):
		return (self.neuron0x7a85b90()*-2.15285)
	def synapse0x7a86600(self):
		return (self.neuron0x7a85e80()*3.78466)
	def synapse0x7a86980(self):
		return (self.neuron0x7a85b90()*-1.92636)
	def synapse0x7a869c0(self):
		return (self.neuron0x7a85e80()*4.33177)
	def synapse0x7a86d40(self):
		return (self.neuron0x7a85b90()*2.41261)
	def synapse0x7a86d80(self):
		return (self.neuron0x7a85e80()*-4.11169)
	def synapse0x7a87100(self):
		return (self.neuron0x7a86280()*3.33367)
	def synapse0x7a87140(self):
		return (self.neuron0x7a86640()*4.87019)
	def synapse0x7a87180(self):
		return (self.neuron0x7a86a00()*-4.22842)
	def synapse0x7a87500(self):
		return (self.neuron0x7a86280()*-3.08046)
	def synapse0x7a87540(self):
		return (self.neuron0x7a86640()*-2.22503)
	def synapse0x79e74a0(self):
		return (self.neuron0x7a86a00()*3.43274)
	def synapse0x79e74e0(self):
		return (self.neuron0x7a86dc0()*10.5679)
	def synapse0x7a879d0(self):
		return (self.neuron0x7a871c0()*-5.96202)
	def synapse0x7a85a60(self):
		return (self.neuron0x7a87690()*-23.9937)
