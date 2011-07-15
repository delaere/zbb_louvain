#include <vector>

class btagPerfFWLiteInterface;

// jet info class
class JetInfo {
  public:
    JetInfo(float mceffSSVHE=1.,float datasfSSVHE=1., float mceffSSVHP=1.,float datasfSSVHP=1., int mcflavor=5): 
      eff_SSVHEM(mceffSSVHE), sf_SSVHEM(datasfSSVHE), eff_SSVHPT(mceffSSVHP), sf_SSVHPT(datasfSSVHP),flavor(mcflavor) {}
    ~JetInfo() {}
    float eff_SSVHEM;
    float sf_SSVHEM;
    float eff_SSVHPT;
    float sf_SSVHPT;
    int   flavor;
};

// a vector of jetsets, easily handled in python
class JetSet {
  public:
    JetSet(const char* infile);
    ~JetSet();
    void addJet(int flavor, double et, double eta);
    void addJet(JetInfo jet);
    const std::vector<JetInfo>& getJets() const { return jets_; }
    void reset() { jets_.clear(); }
  private:
    std::vector<JetInfo> jets_;
    btagPerfFWLiteInterface* interface_;
};

// the algorithm.
// TODO: that version only works for one or two jets of the same kind.
class BTagWeight 
{
 public:
   BTagWeight(int jmin, int jmax): maxTags(jmax), minTags(jmin) {}
   virtual ~BTagWeight() {}
   bool filter(int t);
   float weight(std::vector<JetInfo> jets, int algo, int ntags);
   float weight(JetSet jets, int algo, int ntags) { return weight(jets.getJets(),algo,ntags); }
 private:
   int maxTags;
   int minTags;
};

