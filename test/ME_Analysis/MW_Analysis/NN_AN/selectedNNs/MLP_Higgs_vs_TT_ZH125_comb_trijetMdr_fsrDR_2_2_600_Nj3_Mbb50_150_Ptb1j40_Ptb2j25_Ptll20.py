from math import exp

from math import tanh

class FinalV7/MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_2_2_600_Nj3_Mbb50_150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4):
		self.input0 = (in0 - 22.3555)/3.33759
		self.input1 = (in1 - 24.8885)/1.622
		self.input2 = (in2 - 13.4369)/2.90769
		self.input3 = (in3 - 8.31698)/32.0035
		self.input4 = (in4 - 1.78431)/0.808376
		if index==0: return self.neuron0x2205e270();
		return 0.
	def neuron0x2205c190(self):
		return self.input0
	def neuron0x2205c4d0(self):
		return self.input1
	def neuron0x2205c810(self):
		return self.input2
	def neuron0x2205cb50(self):
		return self.input3
	def neuron0x2205ce90(self):
		return self.input4
	def neuron0x2205d300(self):
		input = 3.64902
		input = input + self.synapse0x21fd2430()
		input = input + self.synapse0x22064eb0()
		input = input + self.synapse0x2205d5b0()
		input = input + self.synapse0x2205d5f0()
		input = input + self.synapse0x2205d630()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2205d670(self):
		input = 1.50372
		input = input + self.synapse0x2205d9b0()
		input = input + self.synapse0x2205d9f0()
		input = input + self.synapse0x2205da30()
		input = input + self.synapse0x2205da70()
		input = input + self.synapse0x2205dab0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2205daf0(self):
		input = 1.34087
		input = input + self.synapse0x2205de30()
		input = input + self.synapse0x2205de70()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2205deb0(self):
		input = -0.615766
		input = input + self.synapse0x2205e1f0()
		input = input + self.synapse0x2205e230()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2205e270(self):
		input = 3.98207
		input = input + self.synapse0x2205e5b0()
		input = input + self.synapse0x2205e5f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x21fd2430(self):
		return (self.neuron0x2205c190()*-2.90113)
	def synapse0x22064eb0(self):
		return (self.neuron0x2205c4d0()*-1.68057)
	def synapse0x2205d5b0(self):
		return (self.neuron0x2205c810()*7.88095)
	def synapse0x2205d5f0(self):
		return (self.neuron0x2205cb50()*0.186782)
	def synapse0x2205d630(self):
		return (self.neuron0x2205ce90()*-0.317133)
	def synapse0x2205d9b0(self):
		return (self.neuron0x2205c190()*1.0251)
	def synapse0x2205d9f0(self):
		return (self.neuron0x2205c4d0()*-0.261704)
	def synapse0x2205da30(self):
		return (self.neuron0x2205c810()*-0.0407685)
	def synapse0x2205da70(self):
		return (self.neuron0x2205cb50()*0.00374991)
	def synapse0x2205dab0(self):
		return (self.neuron0x2205ce90()*-0.00582011)
	def synapse0x2205de30(self):
		return (self.neuron0x2205d300()*3.54168)
	def synapse0x2205de70(self):
		return (self.neuron0x2205d670()*-6.9041)
	def synapse0x2205e1f0(self):
		return (self.neuron0x2205d300()*-0.513862)
	def synapse0x2205e230(self):
		return (self.neuron0x2205d670()*-0.475211)
	def synapse0x2205e5b0(self):
		return (self.neuron0x2205daf0()*-12.5103)
	def synapse0x2205e5f0(self):
		return (self.neuron0x2205deb0()*-0.3838)
