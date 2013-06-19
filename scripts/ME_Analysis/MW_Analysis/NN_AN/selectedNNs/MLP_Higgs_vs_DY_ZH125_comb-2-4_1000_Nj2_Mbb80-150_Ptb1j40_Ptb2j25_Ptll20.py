from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_DY_ZH125_comb-2-4_1000_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 19.6657)/0.978734
		self.input1 = (in1 - 20.3358)/0.823507
		self.input2 = (in2 - 24.2001)/1.26245
		self.input3 = (in3 - 12.5004)/0.729006
		if index==0: return self.neuron0x2555a6e0();
		return 0.
	def neuron0x25558170(self):
		return self.input0
	def neuron0x255584b0(self):
		return self.input1
	def neuron0x255587f0(self):
		return self.input2
	def neuron0x25558b30(self):
		return self.input3
	def neuron0x25558fa0(self):
		input = -1.40779
		input = input + self.synapse0x18970ad0()
		input = input + self.synapse0x255592e0()
		input = input + self.synapse0x25559320()
		input = input + self.synapse0x25559360()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x255593a0(self):
		input = -5.59548
		input = input + self.synapse0x255596e0()
		input = input + self.synapse0x25559720()
		input = input + self.synapse0x25559760()
		input = input + self.synapse0x255597a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x255597e0(self):
		input = 0.250241
		input = input + self.synapse0x25559b20()
		input = input + self.synapse0x25559b60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x25559ba0(self):
		input = -0.324374
		input = input + self.synapse0x25559ee0()
		input = input + self.synapse0x25559f20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x25559f60(self):
		input = -0.0813556
		input = input + self.synapse0x2555a2a0()
		input = input + self.synapse0x2555a2e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2555a320(self):
		input = 0.178193
		input = input + self.synapse0x2555a660()
		input = input + self.synapse0x2555a6a0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2555a6e0(self):
		input = -5.51206
		input = input + self.synapse0x2555aa20()
		input = input + self.synapse0x18970b10()
		input = input + self.synapse0x25548520()
		input = input + self.synapse0x18970710()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x18970ad0(self):
		return (self.neuron0x25558170()*1.43023)
	def synapse0x255592e0(self):
		return (self.neuron0x255584b0()*-0.0653412)
	def synapse0x25559320(self):
		return (self.neuron0x255587f0()*0.301925)
	def synapse0x25559360(self):
		return (self.neuron0x25558b30()*-1.47065)
	def synapse0x255596e0(self):
		return (self.neuron0x25558170()*-3.02778)
	def synapse0x25559720(self):
		return (self.neuron0x255584b0()*1.24588)
	def synapse0x25559760(self):
		return (self.neuron0x255587f0()*0.50992)
	def synapse0x255597a0(self):
		return (self.neuron0x25558b30()*1.0818)
	def synapse0x25559b20(self):
		return (self.neuron0x25558fa0()*-1.17793)
	def synapse0x25559b60(self):
		return (self.neuron0x255593a0()*1.59896)
	def synapse0x25559ee0(self):
		return (self.neuron0x25558fa0()*1.86754)
	def synapse0x25559f20(self):
		return (self.neuron0x255593a0()*-2.50637)
	def synapse0x2555a2a0(self):
		return (self.neuron0x25558fa0()*1.53611)
	def synapse0x2555a2e0(self):
		return (self.neuron0x255593a0()*-2.61328)
	def synapse0x2555a660(self):
		return (self.neuron0x25558fa0()*1.61364)
	def synapse0x2555a6a0(self):
		return (self.neuron0x255593a0()*-3.10554)
	def synapse0x2555aa20(self):
		return (self.neuron0x255597e0()*-2.77924)
	def synapse0x18970b10(self):
		return (self.neuron0x25559ba0()*3.56299)
	def synapse0x25548520(self):
		return (self.neuron0x25559f60()*3.10756)
	def synapse0x18970710(self):
		return (self.neuron0x2555a320()*5.7461)
