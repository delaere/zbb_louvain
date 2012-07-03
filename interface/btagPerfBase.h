#ifndef _btagPerfBase_h_ 
#define _btagPerfBase_h_

#include <utility>

class btagPerfBase {
  public:
    // defines the possible modes for systematics
    enum SystematicVariation { MIN=-1, MEAN=0, MAX=1 };
    // return value + error
    typedef std::pair<double, double> value;
    // usual constructor and destructor
    btagPerfBase() {}
    virtual ~btagPerfBase() {}
    // public (generic) method to get the SF and efficiencies.
    double getbEffScaleFactor( btagPerfBase::SystematicVariation mode, int flavor, int algo, double pt, double eta) const;
    double getbEfficiency( btagPerfBase::SystematicVariation mode, int flavor, int algo, double pt, double eta) const;
  protected:
    // these virtual methods are where the details are implemented. They return pairs (value,unvertainty)
    virtual btagPerfBase::value getbEffScaleFactor(int flavor, int algo, double pt, double eta) const = 0;
    virtual btagPerfBase::value getbEfficiency(int flavor, int algo, double pt, double eta) const = 0;
};
#endif
