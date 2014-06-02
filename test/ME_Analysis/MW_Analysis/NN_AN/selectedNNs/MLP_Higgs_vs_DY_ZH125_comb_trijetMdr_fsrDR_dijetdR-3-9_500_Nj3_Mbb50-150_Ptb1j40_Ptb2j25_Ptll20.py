from math import exp

from math import tanh

class FinalV4/MLP_Higgs_vs_DY_ZH125_comb_trijetMdr_fsrDR_dijetdR-3-9_500_Nj3_Mbb50-150_Ptb1j40_Ptb2j25_Ptll20:
	def value(self,index,in0,in1,in2,in3,in4,in5,in6):
		self.input0 = (in0 - 19.6877)/1.00516
		self.input1 = (in1 - 20.3334)/0.841532
		self.input2 = (in2 - 24.7404)/1.53228
		self.input3 = (in3 - 13.1628)/1.41155
		self.input4 = (in4 - 7.80632)/30.3041
		self.input5 = (in5 - 1.82521)/0.806727
		self.input6 = (in6 - 2.01039)/0.715387
		if index==0: return self.neuron0x26f17d80();
		return 0.
	def neuron0x26f131d0(self):
		return self.input0
	def neuron0x26f13480(self):
		return self.input1
	def neuron0x26f137c0(self):
		return self.input2
	def neuron0x26f13b00(self):
		return self.input3
	def neuron0x26f13e40(self):
		return self.input4
	def neuron0x26f14180(self):
		return self.input5
	def neuron0x26f144c0(self):
		return self.input6
	def neuron0x26f14930(self):
		input = -0.0791932
		input = input + self.synapse0x26f14be0()
		input = input + self.synapse0x26f14c20()
		input = input + self.synapse0x26f14c60()
		input = input + self.synapse0x26f14ca0()
		input = input + self.synapse0x26f14ce0()
		input = input + self.synapse0x26f14d20()
		input = input + self.synapse0x26f14d60()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f14da0(self):
		input = 0.832154
		input = input + self.synapse0x26f150e0()
		input = input + self.synapse0x26f15120()
		input = input + self.synapse0x26f15160()
		input = input + self.synapse0x26f151a0()
		input = input + self.synapse0x26f151e0()
		input = input + self.synapse0x26f15220()
		input = input + self.synapse0x26f15260()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f152a0(self):
		input = -0.290078
		input = input + self.synapse0x26f155e0()
		input = input + self.synapse0x26f15620()
		input = input + self.synapse0x26f15660()
		input = input + self.synapse0x1a95d2c0()
		input = input + self.synapse0x1a95d300()
		input = input + self.synapse0x26f157b0()
		input = input + self.synapse0x26f157f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f15830(self):
		input = -0.747521
		input = input + self.synapse0x26f15b70()
		input = input + self.synapse0x26f15bb0()
		input = input + self.synapse0x26f15bf0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f15c30(self):
		input = -0.364505
		input = input + self.synapse0x26f15f70()
		input = input + self.synapse0x26f15fb0()
		input = input + self.synapse0x26f15ff0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f16030(self):
		input = 0.245571
		input = input + self.synapse0x26f16370()
		input = input + self.synapse0x26f163b0()
		input = input + self.synapse0x26f163f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f16430(self):
		input = 0.377598
		input = input + self.synapse0x26f16770()
		input = input + self.synapse0x26f167b0()
		input = input + self.synapse0x26f167f0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f16a40(self):
		input = 0.0748596
		input = input + self.synapse0x26f16d80()
		input = input + self.synapse0x26f16dc0()
		input = input + self.synapse0x26f16e00()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f16e40(self):
		input = 1.83033
		input = input + self.synapse0x26f17180()
		input = input + self.synapse0x26f171c0()
		input = input + self.synapse0x26f17200()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f17240(self):
		input = -0.190767
		input = input + self.synapse0x1a95d710()
		input = input + self.synapse0x26eb4fd0()
		input = input + self.synapse0x1a95d110()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f17580(self):
		input = 0.197151
		input = input + self.synapse0x26f178c0()
		input = input + self.synapse0x26f17900()
		input = input + self.synapse0x26f17940()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f17980(self):
		input = 0.590029
		input = input + self.synapse0x26f17cc0()
		input = input + self.synapse0x26f17d00()
		input = input + self.synapse0x26f17d40()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def neuron0x26f17d80(self):
		input = 0.741835
		input = input + self.synapse0x26f180c0()
		input = input + self.synapse0x26f18100()
		input = input + self.synapse0x26f18140()
		input = input + self.synapse0x26f18180()
		input = input + self.synapse0x26f181c0()
		input = input + self.synapse0x26f18200()
		input = input + self.synapse0x26f18240()
		input = input + self.synapse0x26f18280()
		input = input + self.synapse0x26f182c0()
		if input<-709. : return 0
		return ((1/(1+exp(-input)))*1)+0
	def synapse0x26f14be0(self):
		return (self.neuron0x26f131d0()*-0.217271)
	def synapse0x26f14c20(self):
		return (self.neuron0x26f13480()*-0.293244)
	def synapse0x26f14c60(self):
		return (self.neuron0x26f137c0()*0.0372355)
	def synapse0x26f14ca0(self):
		return (self.neuron0x26f13b00()*0.684313)
	def synapse0x26f14ce0(self):
		return (self.neuron0x26f13e40()*-0.708682)
	def synapse0x26f14d20(self):
		return (self.neuron0x26f14180()*-0.254362)
	def synapse0x26f14d60(self):
		return (self.neuron0x26f144c0()*-0.124115)
	def synapse0x26f150e0(self):
		return (self.neuron0x26f131d0()*-0.709187)
	def synapse0x26f15120(self):
		return (self.neuron0x26f13480()*-1.18048)
	def synapse0x26f15160(self):
		return (self.neuron0x26f137c0()*3.67021)
	def synapse0x26f151a0(self):
		return (self.neuron0x26f13b00()*-1.10393)
	def synapse0x26f151e0(self):
		return (self.neuron0x26f13e40()*0.985699)
	def synapse0x26f15220(self):
		return (self.neuron0x26f14180()*-0.0406826)
	def synapse0x26f15260(self):
		return (self.neuron0x26f144c0()*-0.795947)
	def synapse0x26f155e0(self):
		return (self.neuron0x26f131d0()*-0.46398)
	def synapse0x26f15620(self):
		return (self.neuron0x26f13480()*-0.10932)
	def synapse0x26f15660(self):
		return (self.neuron0x26f137c0()*1.53969)
	def synapse0x1a95d2c0(self):
		return (self.neuron0x26f13b00()*-0.492586)
	def synapse0x1a95d300(self):
		return (self.neuron0x26f13e40()*0.71214)
	def synapse0x26f157b0(self):
		return (self.neuron0x26f14180()*0.201821)
	def synapse0x26f157f0(self):
		return (self.neuron0x26f144c0()*-0.0263456)
	def synapse0x26f15b70(self):
		return (self.neuron0x26f14930()*1.72136)
	def synapse0x26f15bb0(self):
		return (self.neuron0x26f14da0()*-0.963301)
	def synapse0x26f15bf0(self):
		return (self.neuron0x26f152a0()*1.47649)
	def synapse0x26f15f70(self):
		return (self.neuron0x26f14930()*0.884488)
	def synapse0x26f15fb0(self):
		return (self.neuron0x26f14da0()*-1.07128)
	def synapse0x26f15ff0(self):
		return (self.neuron0x26f152a0()*1.62929)
	def synapse0x26f16370(self):
		return (self.neuron0x26f14930()*-1.72888)
	def synapse0x26f163b0(self):
		return (self.neuron0x26f14da0()*0.0213662)
	def synapse0x26f163f0(self):
		return (self.neuron0x26f152a0()*-1.95412)
	def synapse0x26f16770(self):
		return (self.neuron0x26f14930()*-1.47743)
	def synapse0x26f167b0(self):
		return (self.neuron0x26f14da0()*0.31491)
	def synapse0x26f167f0(self):
		return (self.neuron0x26f152a0()*-1.63441)
	def synapse0x26f16d80(self):
		return (self.neuron0x26f14930()*0.21085)
	def synapse0x26f16dc0(self):
		return (self.neuron0x26f14da0()*-0.446804)
	def synapse0x26f16e00(self):
		return (self.neuron0x26f152a0()*0.842039)
	def synapse0x26f17180(self):
		return (self.neuron0x26f14930()*-2.52132)
	def synapse0x26f171c0(self):
		return (self.neuron0x26f14da0()*3.2338)
	def synapse0x26f17200(self):
		return (self.neuron0x26f152a0()*-4.40572)
	def synapse0x1a95d710(self):
		return (self.neuron0x26f14930()*1.78929)
	def synapse0x26eb4fd0(self):
		return (self.neuron0x26f14da0()*0.0736811)
	def synapse0x1a95d110(self):
		return (self.neuron0x26f152a0()*1.95629)
	def synapse0x26f178c0(self):
		return (self.neuron0x26f14930()*0.840356)
	def synapse0x26f17900(self):
		return (self.neuron0x26f14da0()*-0.459371)
	def synapse0x26f17940(self):
		return (self.neuron0x26f152a0()*1.39455)
	def synapse0x26f17cc0(self):
		return (self.neuron0x26f14930()*-1.03629)
	def synapse0x26f17d00(self):
		return (self.neuron0x26f14da0()*0.503676)
	def synapse0x26f17d40(self):
		return (self.neuron0x26f152a0()*-1.58736)
	def synapse0x26f180c0(self):
		return (self.neuron0x26f15830()*-2.40138)
	def synapse0x26f18100(self):
		return (self.neuron0x26f15c30()*-2.07782)
	def synapse0x26f18140(self):
		return (self.neuron0x26f16030()*3.3634)
	def synapse0x26f18180(self):
		return (self.neuron0x26f16430()*2.02871)
	def synapse0x26f181c0(self):
		return (self.neuron0x26f16a40()*-1.21972)
	def synapse0x26f18200(self):
		return (self.neuron0x26f16e40()*6.27032)
	def synapse0x26f18240(self):
		return (self.neuron0x26f17240()*-3.40602)
	def synapse0x26f18280(self):
		return (self.neuron0x26f17580()*-1.24328)
	def synapse0x26f182c0(self):
		return (self.neuron0x26f17980()*1.39809)
