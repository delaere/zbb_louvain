double formula(double Mass, double Flav1, double Flav2){
  return ( (abs(Flav1)==5 || abs(Flav2)==5)*(0.135957+0.0042069*Mass-4.74489e-06*Mass*Mass+1.33892e-09*Mass*Mass*Mass) + (abs(Flav1)!=5 && abs(Flav2)!=5)*(0.506381+0.00245601*Mass-2.93631e-06*Mass*Mass+9.19538e-10*Mass*Mass*Mass) );
}
