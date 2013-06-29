#######################################################

from ROOT import *

def setStyle() :
 
    gROOT.SetStyle("Plain")
    # For the canvas:
    gStyle.SetCanvasBorderMode(0)
    gStyle.SetCanvasColor(kWhite)
    gStyle.SetCanvasDefH(600) # Height of canvas
    gStyle.SetCanvasDefW(600) # Width of canvas
    gStyle.SetCanvasDefX(0)   # POsition on screen
    gStyle.SetCanvasDefY(0)   #
    # For the Pad:
    gStyle.SetPadBorderMode(0)
    gStyle.SetPadColor(kWhite)
    gStyle.SetPadGridX(false)
    gStyle.SetPadGridY(false)
    gStyle.SetGridColor(0)
    gStyle.SetGridStyle(3)
    gStyle.SetGridWidth(1)
    # For the frame:
    gStyle.SetFrameBorderMode(0);
    gStyle.SetFrameBorderSize(1);
    gStyle.SetFrameFillColor(0);
    gStyle.SetFrameFillStyle(0);
    gStyle.SetFrameLineColor(1);
    gStyle.SetFrameLineStyle(1);
    gStyle.SetFrameLineWidth(1);
    # For the histo:
    gStyle.SetHistLineColor(1);
    gStyle.SetHistLineStyle(0);
    gStyle.SetHistLineWidth(1);
    gStyle.SetEndErrorSize(2);
    gStyle.SetErrorX(0.);
    gStyle.SetMarkerStyle(20);
    # For the fit/function:
    gStyle.SetOptFit(1);
    gStyle.SetFitFormat("5.4g");
    gStyle.SetFuncColor(2);
    gStyle.SetFuncStyle(1);
    gStyle.SetFuncWidth(1);
    # For the date:
    gStyle.SetOptDate(0);
    # For the statistics box:
    gStyle.SetOptFile(0);
    gStyle.SetOptStat(0); #gStyle->SetOptStat("mr");
    gStyle.SetStatColor(kWhite);
    gStyle.SetStatFont(42);
    gStyle.SetStatFontSize(0.04)#---> gStyle->SetStatFontSize(0.025);
    gStyle.SetStatTextColor(1);
    gStyle.SetStatFormat("6.4g");
    gStyle.SetStatBorderSize(1);
    gStyle.SetStatH(0.1);
    gStyle.SetStatW(0.2);#---> gStyle->SetStatW(0.15);
    
    # Margins:
    gStyle.SetPadTopMargin(0.05);
    gStyle.SetPadBottomMargin(0.13);
    gStyle.SetPadLeftMargin(0.16);
    gStyle.SetPadRightMargin(0.02);
    # For the Global title:
    gStyle.SetOptTitle(0);
    gStyle.SetTitleFont(42);
    gStyle.SetTitleColor(1);
    gStyle.SetTitleTextColor(1);
    gStyle.SetTitleFillColor(10);
    gStyle.SetTitleFontSize(0.05);
    
    # For the axis titles:
    gStyle.SetTitleColor(1, "XYZ")
    gStyle.SetTitleFont(42, "XYZ")
    gStyle.SetTitleSize(0.05, "XYZ")
    gStyle.SetTitleXOffset(1.1)
    gStyle.SetTitleYOffset(1.25)
    # For the axis labels:
    gStyle.SetLabelColor(1, "XYZ")
    gStyle.SetLabelFont(42, "XYZ")
    gStyle.SetLabelOffset(0.007, "XYZ")
    gStyle.SetLabelSize(0.045, "XYZ")
    # For the axis:
    gStyle.SetAxisColor(1, "XYZ")
    gStyle.SetStripDecimals(kTRUE)
    gStyle.SetTickLength(0.03, "XYZ")
    gStyle.SetNdivisions(510, "XYZ")
    gStyle.SetPadTickX(1)# To get tick marks on the opposite side of the frame
    gStyle.SetPadTickY(1)#
    # Change for log plots:
    gStyle.SetOptLogx(0);
    gStyle.SetOptLogy(0);
    gStyle.SetOptLogz(0);
    # Postscript options:
    gStyle.SetPaperSize(20.,20.);
    gROOT.ForceStyle();
    gROOT.UseCurrentStyle();
    
