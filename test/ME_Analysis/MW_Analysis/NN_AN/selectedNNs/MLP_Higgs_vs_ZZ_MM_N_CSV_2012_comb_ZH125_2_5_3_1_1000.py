from math import exp

from math import tanh

class MLP_Higgs_vs_ZZ_MM_N_CSV_2012_comb_ZH125_2_5_3_1_1000:
	def value(self,index,in0,in1,in2,in3):
		self.input0 = (in0 - 21.1539)/1.32058
		self.input1 = (in1 - 10.9056)/1.12483
		self.input2 = (in2 - 24.8086)/1.23731
		self.input3 = (in3 - 13.3364)/1.43408
		if index==0: return self.neuron0x91363a0();
		return 0.
	def neuron0x91326a0(self):
		return self.input0
	def neuron0x91329e0(self):
		return self.input1
	def neuron0x9132d20(self):
		return self.input2
	def neuron0x9133060(self):
		return self.input3
	def neuron0x91334d0(self):
		input = -4.6461
		input = input + self.synapse0x90d3a00()
		input = input + self.synapse0x9133780()
		input = input + self.synapse0x91337c0()
		input = input + self.synapse0x9133800()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9133840(self):
		input = -2.70191
		input = input + self.synapse0x9133b80()
		input = input + self.synapse0x9133bc0()
		input = input + self.synapse0x9133c00()
		input = input + self.synapse0x9133c40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9133c80(self):
		input = 1.36485
		input = input + self.synapse0x9133fc0()
		input = input + self.synapse0x9134000()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9134040(self):
		input = -0.381182
		input = input + self.synapse0x9134380()
		input = input + self.synapse0x91343c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9134400(self):
		input = -0.284706
		input = input + self.synapse0x9134740()
		input = input + self.synapse0x9134780()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x91347c0(self):
		input = 0.179155
		input = input + self.synapse0x9134b00()
		input = input + self.synapse0x9134b40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9134b80(self):
		input = 0.0387919
		input = input + self.synapse0x9134ec0()
		input = input + self.synapse0x90d3550()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9135010(self):
		input = 0.880776
		input = input + self.synapse0x9135350()
		input = input + self.synapse0x9135390()
		input = input + self.synapse0x91353d0()
		input = input + self.synapse0x9135410()
		input = input + self.synapse0x9135450()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9135490(self):
		input = 0.614782
		input = input + self.synapse0x91357d0()
		input = input + self.synapse0x9135810()
		input = input + self.synapse0x9135850()
		input = input + self.synapse0x9135890()
		input = input + self.synapse0x91358d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9135910(self):
		input = 0.025953
		input = input + self.synapse0x9135c50()
		input = input + self.synapse0x9135c90()
		input = input + self.synapse0x9135cd0()
		input = input + self.synapse0x9135d10()
		input = input + self.synapse0x9135d50()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x9135fa0(self):
		input = 1.61742
		input = input + self.synapse0x91362e0()
		input = input + self.synapse0x9136320()
		input = input + self.synapse0x9136360()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x91363a0(self):
		input = -5.1674
		input = input + self.synapse0x91366e0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x90d3a00(self):
		return (self.neuron0x91326a0()*-0.208856)
	def synapse0x9133780(self):
		return (self.neuron0x91329e0()*-1.64744)
	def synapse0x91337c0(self):
		return (self.neuron0x9132d20()*0.870751)
	def synapse0x9133800(self):
		return (self.neuron0x9133060()*0.918699)
	def synapse0x9133b80(self):
		return (self.neuron0x91326a0()*0.077417)
	def synapse0x9133bc0(self):
		return (self.neuron0x91329e0()*0.544463)
	def synapse0x9133c00(self):
		return (self.neuron0x9132d20()*0.194996)
	def synapse0x9133c40(self):
		return (self.neuron0x9133060()*-1.32701)
	def synapse0x9133fc0(self):
		return (self.neuron0x91334d0()*-3.1224)
	def synapse0x9134000(self):
		return (self.neuron0x9133840()*1.27502)
	def synapse0x9134380(self):
		return (self.neuron0x91334d0()*-1.75918)
	def synapse0x91343c0(self):
		return (self.neuron0x9133840()*1.82139)
	def synapse0x9134740(self):
		return (self.neuron0x91334d0()*0.910201)
	def synapse0x9134780(self):
		return (self.neuron0x9133840()*0.352387)
	def synapse0x9134b00(self):
		return (self.neuron0x91334d0()*1.75034)
	def synapse0x9134b40(self):
		return (self.neuron0x9133840()*-1.76515)
	def synapse0x9134ec0(self):
		return (self.neuron0x91334d0()*-1.55551)
	def synapse0x90d3550(self):
		return (self.neuron0x9133840()*-0.306353)
	def synapse0x9135350(self):
		return (self.neuron0x9133c80()*-2.47365)
	def synapse0x9135390(self):
		return (self.neuron0x9134040()*-1.97223)
	def synapse0x91353d0(self):
		return (self.neuron0x9134400()*0.153109)
	def synapse0x9135410(self):
		return (self.neuron0x91347c0()*2.37891)
	def synapse0x9135450(self):
		return (self.neuron0x9134b80()*0.154376)
	def synapse0x91357d0(self):
		return (self.neuron0x9133c80()*-2.24361)
	def synapse0x9135810(self):
		return (self.neuron0x9134040()*-1.64461)
	def synapse0x9135850(self):
		return (self.neuron0x9134400()*0.366173)
	def synapse0x9135890(self):
		return (self.neuron0x91347c0()*2.21227)
	def synapse0x91358d0(self):
		return (self.neuron0x9134b80()*0.101487)
	def synapse0x9135c50(self):
		return (self.neuron0x9133c80()*0.75679)
	def synapse0x9135c90(self):
		return (self.neuron0x9134040()*1.3409)
	def synapse0x9135cd0(self):
		return (self.neuron0x9134400()*-0.203427)
	def synapse0x9135d10(self):
		return (self.neuron0x91347c0()*-1.34807)
	def synapse0x9135d50(self):
		return (self.neuron0x9134b80()*0.0852285)
	def synapse0x91362e0(self):
		return (self.neuron0x9135010()*-5.20618)
	def synapse0x9136320(self):
		return (self.neuron0x9135490()*-4.08309)
	def synapse0x9136360(self):
		return (self.neuron0x9135910()*2.68076)
	def synapse0x91366e0(self):
		return (self.neuron0x9135fa0()*11.6261)
