from math import exp

from math import tanh

class MLP_Higgs_vs_DY_MM_N_CSV_2012_comb_ZH125_3_2_1_600:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 19.4187)/1.13986
		self.input1 = (in1 - 20.1808)/1.02782
		self.input2 = (in2 - 25.0021)/1.84057
		self.input3 = (in3 - 13.943)/1.94542
		if index==0: return self.neuron0xc545ec0();
		return 0.
	def neuron0xc543810(self):
		return self.input0
	def neuron0xc543b50(self):
		return self.input1
	def neuron0xc543e90(self):
		return self.input2
	def neuron0xc5441d0(self):
		return self.input3
	def neuron0xc544640(self):
		input = 2.321
		input = input + self.synapse0xc4e4b70()
		input = input + self.synapse0xc5448f0()
		input = input + self.synapse0xc544930()
		input = input + self.synapse0xc544970()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc5449b0(self):
		input = -5.5918
		input = input + self.synapse0xc544cf0()
		input = input + self.synapse0xc544d30()
		input = input + self.synapse0xc544d70()
		input = input + self.synapse0xc544db0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc544df0(self):
		input = -3.8749
		input = input + self.synapse0xc545130()
		input = input + self.synapse0xc545170()
		input = input + self.synapse0xc5451b0()
		input = input + self.synapse0xc5451f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc545230(self):
		input = -2.2867
		input = input + self.synapse0xc545570()
		input = input + self.synapse0xc5455b0()
		input = input + self.synapse0xc5455f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc545630(self):
		input = -1.0896
		input = input + self.synapse0xc545970()
		input = input + self.synapse0xc5459b0()
		input = input + self.synapse0xc4e46c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc545b00(self):
		input = 3.45277
		input = input + self.synapse0xc545e40()
		input = input + self.synapse0xc545e80()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0xc545ec0(self):
		input = -3.21877
		input = input + self.synapse0xc546200()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0xc4e4b70(self):
		return (self.neuron0xc543810()*-0.556269)
	def synapse0xc5448f0(self):
		return (self.neuron0xc543b50()*0.0235877)
	def synapse0xc544930(self):
		return (self.neuron0xc543e90()*-0.228767)
	def synapse0xc544970(self):
		return (self.neuron0xc5441d0()*1.62826)
	def synapse0xc544cf0(self):
		return (self.neuron0xc543810()*-1.70472)
	def synapse0xc544d30(self):
		return (self.neuron0xc543b50()*-0.0897515)
	def synapse0xc544d70(self):
		return (self.neuron0xc543e90()*5.0335)
	def synapse0xc544db0(self):
		return (self.neuron0xc5441d0()*0.618993)
	def synapse0xc545130(self):
		return (self.neuron0xc543810()*-2.91263)
	def synapse0xc545170(self):
		return (self.neuron0xc543b50()*1.73561)
	def synapse0xc5451b0(self):
		return (self.neuron0xc543e90()*-0.402805)
	def synapse0xc5451f0(self):
		return (self.neuron0xc5441d0()*1.42651)
	def synapse0xc545570(self):
		return (self.neuron0xc544640()*2.27052)
	def synapse0xc5455b0(self):
		return (self.neuron0xc5449b0()*1.82516)
	def synapse0xc5455f0(self):
		return (self.neuron0xc544df0()*2.901)
	def synapse0xc545970(self):
		return (self.neuron0xc544640()*2.05092)
	def synapse0xc5459b0(self):
		return (self.neuron0xc5449b0()*0.873522)
	def synapse0xc4e46c0(self):
		return (self.neuron0xc544df0()*1.73391)
	def synapse0xc545e40(self):
		return (self.neuron0xc545230()*-5.21073)
	def synapse0xc545e80(self):
		return (self.neuron0xc545630()*-2.69348)
	def synapse0xc546200(self):
		return (self.neuron0xc545b00()*9.61136)
