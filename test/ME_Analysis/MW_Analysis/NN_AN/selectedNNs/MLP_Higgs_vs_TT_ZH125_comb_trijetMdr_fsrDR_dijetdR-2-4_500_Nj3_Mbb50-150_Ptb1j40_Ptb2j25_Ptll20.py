from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_TT_ZH125_comb_trijetMdr_fsrDR_dijetdR-2-4_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4,in5):
		self.input0 = (in0 - 22.3628)/3.40518
		self.input1 = (in1 - 24.8571)/1.64412
		self.input2 = (in2 - 13.3589)/2.81791
		self.input3 = (in3 - 7.75963)/31.5808
		self.input4 = (in4 - 1.78919)/0.803089
		self.input5 = (in5 - 1.96887)/0.681436
		if index==0: return self.neuron0x11b78c60();
		return 0.
	def neuron0x11b75fc0(self):
		return self.input0
	def neuron0x11b76270(self):
		return self.input1
	def neuron0x11b765b0(self):
		return self.input2
	def neuron0x11b768f0(self):
		return self.input3
	def neuron0x11b76c30(self):
		return self.input4
	def neuron0x11b76f70(self):
		return self.input5
	def neuron0x11b773e0(self):
		input = 2.62788
		input = input + self.synapse0x11b77690()
		input = input + self.synapse0x11b776d0()
		input = input + self.synapse0x11b77710()
		input = input + self.synapse0x11b77750()
		input = input + self.synapse0x11b77790()
		input = input + self.synapse0x11b777d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b77810(self):
		input = 0.330282
		input = input + self.synapse0x11b77b50()
		input = input + self.synapse0x11b77b90()
		input = input + self.synapse0x11b77bd0()
		input = input + self.synapse0x11b77c10()
		input = input + self.synapse0x11b77c50()
		input = input + self.synapse0x11b77c90()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b77cd0(self):
		input = 0.518616
		input = input + self.synapse0x11b78010()
		input = input + self.synapse0x11b78050()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b78090(self):
		input = -0.316929
		input = input + self.synapse0x11b783d0()
		input = input + self.synapse0x11b78410()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b78450(self):
		input = 0.928831
		input = input + self.synapse0x11b78790()
		input = input + self.synapse0xea230d0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b788e0(self):
		input = 0.0131023
		input = input + self.synapse0xea23110()
		input = input + self.synapse0x11b78c20()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x11b78c60(self):
		input = -5.95166
		input = input + self.synapse0x11b78e80()
		input = input + self.synapse0x11b78ec0()
		input = input + self.synapse0x11b78f00()
		input = input + self.synapse0x11b78f40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x11b77690(self):
		return (self.neuron0x11b75fc0()*-3.48485)
	def synapse0x11b776d0(self):
		return (self.neuron0x11b76270()*-2.82706)
	def synapse0x11b77710(self):
		return (self.neuron0x11b765b0()*9.76656)
	def synapse0x11b77750(self):
		return (self.neuron0x11b768f0()*0.308223)
	def synapse0x11b77790(self):
		return (self.neuron0x11b76c30()*-0.475155)
	def synapse0x11b777d0(self):
		return (self.neuron0x11b76f70()*-0.738268)
	def synapse0x11b77b50(self):
		return (self.neuron0x11b75fc0()*1.32742)
	def synapse0x11b77b90(self):
		return (self.neuron0x11b76270()*-0.350923)
	def synapse0x11b77bd0(self):
		return (self.neuron0x11b765b0()*-0.0672746)
	def synapse0x11b77c10(self):
		return (self.neuron0x11b768f0()*0.0202848)
	def synapse0x11b77c50(self):
		return (self.neuron0x11b76c30()*-0.0216912)
	def synapse0x11b77c90(self):
		return (self.neuron0x11b76f70()*-0.126896)
	def synapse0x11b78010(self):
		return (self.neuron0x11b773e0()*-1.62919)
	def synapse0x11b78050(self):
		return (self.neuron0x11b77810()*2.86456)
	def synapse0x11b783d0(self):
		return (self.neuron0x11b773e0()*-0.845078)
	def synapse0x11b78410(self):
		return (self.neuron0x11b77810()*3.2039)
	def synapse0x11b78790(self):
		return (self.neuron0x11b773e0()*1.47102)
	def synapse0xea230d0(self):
		return (self.neuron0x11b77810()*-4.31152)
	def synapse0xea23110(self):
		return (self.neuron0x11b773e0()*-1.48961)
	def synapse0x11b78c20(self):
		return (self.neuron0x11b77810()*6.10685)
	def synapse0x11b78e80(self):
		return (self.neuron0x11b77cd0()*0.880602)
	def synapse0x11b78ec0(self):
		return (self.neuron0x11b78090()*1.75315)
	def synapse0x11b78f00(self):
		return (self.neuron0x11b78450()*-5.43143)
	def synapse0x11b78f40(self):
		return (self.neuron0x11b788e0()*7.8027)
