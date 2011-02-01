#include <dirent.h>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <string>
#include <fstream>
#include <algorithm>

// this is a C++ version of the diow perl scrip version 1.6, 
// http://mips.as.arizona.edu/~hdole/diow/

class diowGenerator
{
  public:
    diowGenerator();
    ~diowGenerator() {}
    void setUsername(const char* user) { username_=user; }
    void setTitle(const char* title) { title_=title; }
    void setColors(const char* text="000066", const char* bg="CCCCFF", const char* link="FFFF00",
                   const char* vlink="FF00FF", const char* bar="9999FF") {
      textcolor_=text; bgcolor_=bg; linkcolor_=link; vlinkcolor_=vlink, barcolor_=bar; 
    }
    void setNcols(int N=6) { nCols_=N; }
    void setIconSize(uint32_t size=200) { iconsize_=size; }

    void createWebpage(const char* path = ".", const char* file = "index.html");
    void addItem(const char* filename);
    void finishWebpage();

    static void listdir(const char *path,std::vector<std::string>& files);

  private:
    std::string username_;
    std::string title_;
    std::string path_;
    std::string outhtml_;
    std::string textcolor_;
    std::string bgcolor_;
    std::string linkcolor_;
    std::string vlinkcolor_;
    std::string barcolor_;
    int nCols_;
    uint32_t iconsize_;
    int count_;
    std::ofstream* output_;
};

diowGenerator::diowGenerator() {
    username_ = "";
    title_ = "Digital Images on the Web";
    outhtml_ = "index.html";
    path_ = ".";
    textcolor_ = "000066";
    bgcolor_ = "CCCCFF";
    linkcolor_ = "FFFF00";
    vlinkcolor_ = "FF00FF";
    barcolor_ = "9999FF";
    nCols_ = 6;
    iconsize_ = 200;
    count_ = 0;
    output_ = NULL;
}

void diowGenerator::createWebpage(const char* path, const char* file) {
    path_ = path;
    outhtml_ = path + std::string("/") + std::string(file);
    output_ = new std::ofstream(outhtml_.c_str());
    (*output_) << "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">" << std::endl;
    (*output_) << "<html>\n<head>\n<title>" << title_ << ": " << username_ << " 's Images</title>" << std::endl;
    (*output_) << "</head>\n<BODY TEXT=\"" << textcolor_ 
            << "\" BGCOLOR=\"" << bgcolor_
            << "\" LINK=\"" << linkcolor_ 
            << "\" VLINK=\"" << vlinkcolor_ << "\" >" << std::endl;
    (*output_) << "<P>\n<TABLE WIDTH=\"100%\">\n <TR>\n<TH ALIGN=\"center\" width=\"40%\" BGCOLOR=\"" 
            << barcolor_ << "\"><FONT COLOR=\"#FFFFFF\" SIZE=+1>" 
            << title_ << "</FONT></TH>\n</TABLE>\n</p>" << std::endl;
    (*output_) << "<center><TABLE border=0 cellpadding=5 cellspacing=2>" << std::endl;
}

void diowGenerator::finishWebpage() {
    time_t rawtime;
    time ( &rawtime );
    (*output_) << "</TABLE>\n</center>\n<p>\n<hr width=\"100%\">\n<table border=0 cellspacing=0 cellpadding=0 width=\"100\%\">" << std::endl;
    (*output_) << "<tr><td><em>Created: " << ctime(&rawtime) << "</em></td><td align=right><em>\n<tr><td align=left><em>" << std::endl;
    (*output_) << "using the \"Digital Images On the Web\" C++ script\n</em></td></tr>\n</table>\n</body>\n</html>\n";
    output_->close();
}

void diowGenerator::listdir(const char *path,std::vector<std::string>& files) {
    // open the directory
    DIR *pdir = NULL; 
    pdir = opendir (path);
    struct dirent *pent = NULL;
    if (pdir == NULL) { 
        printf ("\nERROR! could not open the directory.");
        return;
    }
    // loop over files
    while ((pent = readdir (pdir))) {
        if (pent == NULL) {
            printf ("\nERROR! could not read the directory.");
            return;
        }
        files.push_back(std::string(pent->d_name));
    }
    // finally, let's close the directory
    closedir (pdir);
}

void diowGenerator::addItem(const char* filename) {
   // name of the icon file
   std::string smallfilename(filename);
   smallfilename.replace (smallfilename.size()-4,4,"_small.png");
   // create the icon file
   char command[1024];
   sprintf(command,"cd %s;convert -geometry x%d \'%s\' \'%s\'",path_.c_str(),iconsize_,filename,smallfilename.c_str());
   system(command);
   // insert in the HTML code the image and its icon
   std::string prefix = " ";
   std::string suffix = " ";
   if (count_==nCols_-1) { 
     prefix = " ";
     suffix = "</TR>";
     count_ = -1;
   }
   if (count_==0) {
     prefix = "<TR>";
     suffix = " ";
   }
   (*output_) << prefix << "<TD align=center> <a href=\"" << filename 
           << "\"><img src=\"" << smallfilename << "\"hspace=5 vspace=5 border=0 ALT=\"" 
           << filename << "\"></a>\n<br>" << filename << "</TD>" << suffix << std::endl;
   count_++;
}

void diow(const char* inpath=".", const char* outputFile="index.html")
{
   diowGenerator generator;
   generator.createWebpage(inpath,outputFile);
   std::vector<std::string> files;
   diowGenerator::listdir(inpath, files);
   std::sort(files.begin(),files.end());
   std::string extensions[3] = {".jpg",".png",".gif"};
   for(std::vector<std::string>::const_iterator file = files.begin(); file<files.end(); ++file) {
      // we use the extension to identify pictures... not very elegant.
      // look for *.jpg, *.png, *.gif
      for(unsigned i=0;i<3;++i) {
         size_t found = file->rfind(extensions[i]);
         if(found != std::string::npos && found == file->size()-4) {
           generator.addItem(file->c_str());
         }
      }
   }
   generator.finishWebpage();
}

