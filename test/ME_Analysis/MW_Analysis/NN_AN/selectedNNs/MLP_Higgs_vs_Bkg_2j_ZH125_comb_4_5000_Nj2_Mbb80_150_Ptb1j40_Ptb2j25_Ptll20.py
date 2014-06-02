from math import exp

from math import tanh

class FinalV8/MLP_Higgs_vs_Bkg_2j_ZH125_comb_4_5000_Nj2_Mbb80_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2):
		self.input0 = (in0 - 0.492195)/0.255462
		self.input1 = (in1 - 0.567862)/0.324105
		self.input2 = (in2 - 0.596078)/0.304322
		if index==0: return self.neuron0x2f8c5a60();
		return 0.
	def neuron0x2f8c4040(self):
		return self.input0
	def neuron0x2f8c4380(self):
		return self.input1
	def neuron0x2f8c46c0(self):
		return self.input2
	def neuron0x2f8c4b30(self):
		input = 0.345579
		input = input + self.synapse0x2f8ccd40()
		input = input + self.synapse0x2f8c4de0()
		input = input + self.synapse0x2f8c4e20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2f8c4e60(self):
		input = 0.569005
		input = input + self.synapse0x2f8c51a0()
		input = input + self.synapse0x2f8c51e0()
		input = input + self.synapse0x2f8c5220()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2f8c5260(self):
		input = -9.5062
		input = input + self.synapse0x2f8c55a0()
		input = input + self.synapse0x2f8c55e0()
		input = input + self.synapse0x2f8c5620()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2f8c5660(self):
		input = 2.84143
		input = input + self.synapse0x2f8c59a0()
		input = input + self.synapse0x2f8c59e0()
		input = input + self.synapse0x2f8c5a20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2f8c5a60(self):
		input = -4.02792
		input = input + self.synapse0x2f8c4a00()
		input = input + self.synapse0x2f8c5da0()
		input = input + self.synapse0x2f8c5de0()
		input = input + self.synapse0x2f8c5e20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x2f8ccd40(self):
		return (self.neuron0x2f8c4040()*-1.27089)
	def synapse0x2f8c4de0(self):
		return (self.neuron0x2f8c4380()*0.611048)
	def synapse0x2f8c4e20(self):
		return (self.neuron0x2f8c46c0()*0.844143)
	def synapse0x2f8c51a0(self):
		return (self.neuron0x2f8c4040()*-1.16844)
	def synapse0x2f8c51e0(self):
		return (self.neuron0x2f8c4380()*0.823278)
	def synapse0x2f8c5220(self):
		return (self.neuron0x2f8c46c0()*1.03581)
	def synapse0x2f8c55a0(self):
		return (self.neuron0x2f8c4040()*-5.13407)
	def synapse0x2f8c55e0(self):
		return (self.neuron0x2f8c4380()*0.0061512)
	def synapse0x2f8c5620(self):
		return (self.neuron0x2f8c46c0()*0.752944)
	def synapse0x2f8c59a0(self):
		return (self.neuron0x2f8c4040()*-0.0815118)
	def synapse0x2f8c59e0(self):
		return (self.neuron0x2f8c4380()*-0.587444)
	def synapse0x2f8c5a20(self):
		return (self.neuron0x2f8c46c0()*0.787141)
	def synapse0x2f8c4a00(self):
		return (self.neuron0x2f8c4b30()*-12.967)
	def synapse0x2f8c5da0(self):
		return (self.neuron0x2f8c4e60()*10.8267)
	def synapse0x2f8c5de0(self):
		return (self.neuron0x2f8c5260()*-9.34735)
	def synapse0x2f8c5e20(self):
		return (self.neuron0x2f8c5660()*5.38594)
