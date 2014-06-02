from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_ZZ_ZH125_comb-2-4_750_Nj2_Mbb80-150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 21.1193)/1.28039
		self.input1 = (in1 - 10.8967)/1.04615
		self.input2 = (in2 - 24.4553)/1.1302
		self.input3 = (in3 - 12.6886)/0.870338
		if index==0: return self.neuron0x2a6a63a0();
		return 0.
	def neuron0x2a6a3ec0(self):
		return self.input0
	def neuron0x2a6a4200(self):
		return self.input1
	def neuron0x2a6a4540(self):
		return self.input2
	def neuron0x2a6a4880(self):
		return self.input3
	def neuron0x2a6a4cf0(self):
		input = -1.14901
		input = input + self.synapse0x2a67ca50()
		input = input + self.synapse0x2a6a4fa0()
		input = input + self.synapse0x2a6a4fe0()
		input = input + self.synapse0x2a6a5020()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2a6a5060(self):
		input = -1.19692
		input = input + self.synapse0x2a6a53a0()
		input = input + self.synapse0x2a6a53e0()
		input = input + self.synapse0x2a6a5420()
		input = input + self.synapse0x2a6a5460()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2a6a54a0(self):
		input = -7.26315
		input = input + self.synapse0x2a6a57e0()
		input = input + self.synapse0x2a6a5820()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2a6a5860(self):
		input = 2.08904
		input = input + self.synapse0x2a6a5ba0()
		input = input + self.synapse0x2a6a5be0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2a6a5c20(self):
		input = 1.47028
		input = input + self.synapse0x2a6a5f60()
		input = input + self.synapse0x2a6a5fa0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2a6a5fe0(self):
		input = -0.0858749
		input = input + self.synapse0x2a6a6320()
		input = input + self.synapse0x2a6a6360()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x2a6a63a0(self):
		input = 0.303812
		input = input + self.synapse0x2a6a66e0()
		input = input + self.synapse0x293ac0f0()
		input = input + self.synapse0x293ac130()
		input = input + self.synapse0x2a6a4bc0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x2a67ca50(self):
		return (self.neuron0x2a6a3ec0()*0.116502)
	def synapse0x2a6a4fa0(self):
		return (self.neuron0x2a6a4200()*-0.982646)
	def synapse0x2a6a4fe0(self):
		return (self.neuron0x2a6a4540()*0.606143)
	def synapse0x2a6a5020(self):
		return (self.neuron0x2a6a4880()*0.141795)
	def synapse0x2a6a53a0(self):
		return (self.neuron0x2a6a3ec0()*0.099688)
	def synapse0x2a6a53e0(self):
		return (self.neuron0x2a6a4200()*-1.08078)
	def synapse0x2a6a5420(self):
		return (self.neuron0x2a6a4540()*-0.913825)
	def synapse0x2a6a5460(self):
		return (self.neuron0x2a6a4880()*1.90247)
	def synapse0x2a6a57e0(self):
		return (self.neuron0x2a6a4cf0()*12.6531)
	def synapse0x2a6a5820(self):
		return (self.neuron0x2a6a5060()*-2.39328)
	def synapse0x2a6a5ba0(self):
		return (self.neuron0x2a6a4cf0()*1.20778)
	def synapse0x2a6a5be0(self):
		return (self.neuron0x2a6a5060()*-5.32313)
	def synapse0x2a6a5f60(self):
		return (self.neuron0x2a6a4cf0()*0.703596)
	def synapse0x2a6a5fa0(self):
		return (self.neuron0x2a6a5060()*0.342612)
	def synapse0x2a6a6320(self):
		return (self.neuron0x2a6a4cf0()*7.8293)
	def synapse0x2a6a6360(self):
		return (self.neuron0x2a6a5060()*4.66366)
	def synapse0x2a6a66e0(self):
		return (self.neuron0x2a6a54a0()*-10.958)
	def synapse0x293ac0f0(self):
		return (self.neuron0x2a6a5860()*3.09474)
	def synapse0x293ac130(self):
		return (self.neuron0x2a6a5c20()*6.35123)
	def synapse0x2a6a4bc0(self):
		return (self.neuron0x2a6a5fe0()*-7.5753)
